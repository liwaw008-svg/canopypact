import json,re,time
from pathlib import Path
from genlayer_py import create_client,create_account
from genlayer_py.chains import studionet

ROOT=Path(__file__).parents[1]; ENV=(ROOT.parents[3]/'accounts.env').read_text()
def secret(n):return re.search(rf'^ACCOUNT_{n}_GENLAYER_PRIVATE_KEY\s*=\s*"?([^"\r\n]+)',ENV,re.M).group(1).strip()
def wait(c,h):
    r=c.wait_for_transaction_receipt(transaction_hash=h,status='ACCEPTED',retries=120,interval=10000)
    t=c.get_transaction(transaction_hash=h)
    if t.get('status_name')!='ACCEPTED' or t.get('result') not in (6,'6'):raise RuntimeError({'status':t.get('status_name'),'result':t.get('result')})
    return r

sponsor=create_account(account_private_key=secret(3)); steward=create_account(account_private_key=secret(4))
sc=create_client(chain=studionet,account=sponsor); wc=create_client(chain=studionet,account=steward)
address=json.loads((ROOT/'deployment.json').read_text())['contract']; pact='CP-FROZEN-'+str(int(time.time()))
base='https://raw.githubusercontent.com/liwaw008-svg/canopypact/2557aec/evidence/'
baseline=[base+'demo-baseline-a.json',base+'demo-baseline-b.json']; observations=[base+'demo-observation-a.json',base+'demo-observation-b.json']
goals=['At least 85 percent of planted trees remain viable at observation','Mulched soil coverage is visible across every declared row','Public records identify the date, parcel and six-row sampling method']
protocol='Compare the frozen dated baseline with later public observations using the same six-row transect. Verify location and capture date, count visible viable trees and documented losses, and preserve uncertainty when a record cannot be authenticated.'
funded=sc.write_contract(address=address,function_name='fund_pact',args=[pact,steward.address,'North bank community orchard parcel C7',goals,protocol,baseline],value=10**16);print('fund',funded,flush=True);wait(sc,funded)
frozen=sc.read_contract(address=address,function_name='get_pact',args=[pact])
if len(frozen['baseline_digests'])!=2:raise RuntimeError('baseline was not frozen')
accepted=wc.write_contract(address=address,function_name='accept_pact',args=[pact]);print('accept',accepted,flush=True);wait(wc,accepted)
reviewed=wc.write_contract(address=address,function_name='submit_observations',args=[pact,observations]);print('review',reviewed,flush=True);wait(wc,reviewed)
state=wc.read_contract(address=address,function_name='get_pact',args=[pact]);print(json.dumps({'id':pact,'sponsor':sponsor.address,'steward':steward.address,'transactions':{'fund':funded,'accept':accepted,'review':reviewed},'state':state},indent=2),flush=True)
if state['status']!='SETTLED' or state['outcome'] not in ('VERIFIED','PARTIAL') or len(state['observation_digests'])!=2:raise RuntimeError(state)
