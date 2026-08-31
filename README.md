# CanopyPact

CanopyPact turns ecological outcome grants into evidence-bound public agreements. A sponsor funds measurable goals, a named steward accepts the protocol, and later observations are evaluated against the original baseline. GenLayer is used only for the irreducibly semantic question: does heterogeneous field evidence support each declared outcome?

## Protocol

- `fund_pact` locks GEN with a place, at least two goals, a detailed measurement protocol, two distinct HTTPS baseline sources, and a named steward. In that same funding transaction, validators fetch the baseline and commit its exact snapshots and SHA-256 digests.
- `accept_pact` prevents anyone except that steward from taking responsibility.
- `submit_observations` makes every validator compare independently fetched later observations with the immutable baseline snapshots captured at funding, then recompute the bounded outcome, exact unmet-goal indexes and observation digests.
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

- Contract: `0x10A9d04dEf8cD65a0BB4dc6a7fcee804Eb5cbAdb`
- Deploy tx: `0x26a5b64b77e5b5126d446ca66e261c1a16796130363d0a5522efec5e6438fdb6`
- Live app: `https://canopypact.pages.dev/`

## Proven StudioNet lifecycle

The replacement deployment is live. Fresh cross-wallet lifecycle transactions are recorded after the final source commit so baseline snapshots are tied to immutable public records.
