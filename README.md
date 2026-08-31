# CanopyPact

CanopyPact turns ecological outcome grants into evidence-bound public agreements. A sponsor funds measurable goals, a named steward accepts the protocol, and later observations are evaluated against the original baseline. GenLayer is used only for the irreducibly semantic question: does heterogeneous field evidence support each declared outcome?

## Protocol

- `fund_pact` locks GEN with a place, at least two goals, a detailed measurement protocol, two or more HTTPS baseline sources, and a named steward.
- `accept_pact` prevents anyone except that steward from taking responsibility.
- `submit_observations` makes every validator independently re-fetch baseline and observation records, then recompute the bounded outcome and exact unmet-goal indexes.
- `VERIFIED` pays the steward, `FAILED` refunds the sponsor, `PARTIAL` splits the grant equally, and `UNVERIFIABLE` retains all funds for resubmission.
- Transfers occur only on finalized consensus.

The LLM never determines amounts or recipients. A `VERIFIED` result containing any unmet goal is rejected before consensus. External, transient and malformed-model errors have explicit validator behavior.

## Fieldbook application

The frontend is a complete responsive transaction surface with editable goals, protocol, baseline, observation URLs and grant amount. It supports wallet connection, funding, steward acceptance, observation review, receipt polling and public pact reads. Its editorial field-notebook identity is deliberately unrelated to DockSure's logistics control room.

## Test and audit

```bash
genvm-lint check contracts/contract.py
python -m pytest -q
```

Four public demo records support a real baseline-to-observation StudioNet lifecycle.

## Deployment

- Contract: `0x9dC61fb04F541A94EF38340e0bd1A89e4e33aB59`
- Deploy tx: `0xe805e3470fd64f603e011e820c27fc3ef6756be8c9f4d726ea80df098c540d89`
- Live app: `https://canopypact.pages.dev/`

## Proven StudioNet lifecycle

- Fund pact: `0xce303efe5c3061436cef4a499b0a941dc034add24d6358dd588513c668b356ea`
- Steward acceptance: `0xcf0b651268dfa9f8298ba9300ce1146f84f31790ab82417f256bfb2485f057d7`
- Observation consensus and VERIFIED settlement: `0x4ed35fa53fd557b7ae385b21f4a304123e50c6fcb8cfe6118b0b1010d86be520`
