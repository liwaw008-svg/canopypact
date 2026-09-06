from conftest import CONTRACT

GOALS=['Keep at least 100 viable trees','Preserve all six transect rows']
PROTOCOL='Compare the dated baseline and field observations using the same six-row transect and preserve uncertainty.'
BASELINE=['https://baseline-a.example/parcel/C7','https://baseline-b.example/parcel/C7']

def test_invalid_and_duplicate_sources_are_rejected(direct_vm,direct_deploy,direct_bob):
    c=direct_deploy(CONTRACT);direct_vm.value=100
    with direct_vm.expect_revert('valid HTTPS source required'):
        c.fund_pact('BAD','0x'+direct_bob.hex(),'Parcel C7',GOALS,PROTOCOL,['https://baseline-a.example/one','http://baseline-b.example/two'])
    with direct_vm.expect_revert('independent HTTPS baseline sources required'):
        c.fund_pact('SAME','0x'+direct_bob.hex(),'Parcel C7',GOALS,PROTOCOL,[BASELINE[0],BASELINE[0]])

def test_sponsor_recovers_only_after_active_timeout(direct_vm,direct_deploy,direct_alice,direct_bob):
    direct_vm.warp('2030-01-01T00:00:00+00:00');c=direct_deploy(CONTRACT);direct_vm.sender=direct_alice;direct_vm.value=100
    direct_vm.mock_web(r'baseline-a\.example',{'status':200,'body':'trees=120 rows=6'});direct_vm.mock_web(r'baseline-b\.example',{'status':200,'body':'parcel=C7 method=transect'})
    c.fund_pact('RECOVER','0x'+direct_bob.hex(),'Parcel C7',GOALS,PROTOCOL,BASELINE);direct_vm.value=0;direct_vm.sender=direct_bob;c.accept_pact('RECOVER');direct_vm.sender=direct_alice
    with direct_vm.expect_revert('expired active sponsor pact required'):c.recover_expired('RECOVER')
    direct_vm.warp('2030-02-01T00:00:01+00:00');c.recover_expired('RECOVER')
    assert c.get_pact('RECOVER')['status']=='RECOVERED'
