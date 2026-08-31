from pathlib import Path
import ast
S=(Path(__file__).parents[1]/'contracts/contract.py').read_text()
def test_parses_and_lifecycle_is_complete():
    ast.parse(S)
    for n in ('fund_pact','accept_pact','cancel_unaccepted','submit_observations','get_pact','list_pacts'):assert f'def {n}' in S
def test_validator_refetches_and_recomputes():
    assert 'gl.nondet.web.get(url)' in S and 'mine=run()' in S and "mine['unmet']==theirs.get('unmet')" in S
def test_no_e025_nested_equivalence_call():assert 'prompt_non_comparative' not in S and 'eq_principle' not in S
def test_deterministic_settlement_rails():
    assert "if out=='VERIFIED':self._pay(p.steward,amount)" in S
    assert "elif out=='FAILED':self._pay(p.sponsor,amount)" in S
    assert "on='finalized'" in S
def test_verified_cannot_hide_unmet_goals():assert "if out=='VERIFIED' and unmet" in S
def test_baseline_is_frozen_during_funding():
    fund=S.index('def fund_pact'); accept=S.index('def accept_pact')
    assert 'frozen=self._freeze(urls)' in S[fund:accept]
    assert 'baseline_snapshots' in S and 'baseline_digests' in S
    assert 'hashlib.sha256' in S and "mine['digests']==theirs.get('digests')" in S
def test_review_uses_frozen_baseline_not_live_baseline_urls():
    review=S[S.index('def _review'):S.index('def submit_observations')]
    assert 'frozen=json.loads(p.baseline_snapshots)' in review
    assert 'records=list(frozen)' in review
    assert 'for url in observations' in review
    assert 'for url in baseline' not in review
def test_duplicate_baseline_and_observation_sources_are_rejected():
    assert S.count('urls[0]==urls[1]')>=2
