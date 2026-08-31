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

