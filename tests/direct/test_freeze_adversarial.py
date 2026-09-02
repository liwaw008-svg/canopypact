from conftest import CONTRACT

def test_validator_rejects_mismatched_snapshot_digest_pair(direct_vm,direct_deploy):
    c=direct_deploy(CONTRACT)
    direct_vm.mock_web(r'baseline-a\.example',{'status':200,'body':'parcel=C7 trees=120 date=2026-03-01'})
    direct_vm.mock_web(r'baseline-b\.example',{'status':200,'body':'parcel=C7 rows=6 method=transect'})
    result=c._freeze(['https://baseline-a.example/record','https://baseline-b.example/record'])
    forged={'snapshots':['tampered snapshot',result['snapshots'][1]],'digests':result['digests']}
    assert direct_vm.run_validator(leader_result=forged) is False

def test_validator_accepts_exact_snapshot_digest_pair(direct_vm,direct_deploy):
    c=direct_deploy(CONTRACT)
    direct_vm.mock_web(r'baseline-a\.example',{'status':200,'body':'parcel=C7 trees=120 date=2026-03-01'})
    direct_vm.mock_web(r'baseline-b\.example',{'status':200,'body':'parcel=C7 rows=6 method=transect'})
    result=c._freeze(['https://baseline-a.example/record','https://baseline-b.example/record'])
    assert direct_vm.run_validator(leader_result=result) is True
