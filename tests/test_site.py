from pathlib import Path
R=Path(__file__).parents[1]
def test_real_complete_frontend():
 h=(R/'site/index.html').read_text();j=(R/'site/app.js').read_text();c=(R/'site/styles.css').read_text()
 assert all(x in j for x in ('fund_pact','accept_pact','submit_observations','waitForTransactionReceipt'))
 assert 'role="status"' in h and '__CONTRACT__' not in j and len(c)>4000
def test_four_demo_records_exist():assert len(list((R/'evidence').glob('*.json')))==4
