# CanopyPact

CanopyPact turns ecological outcome grants into evidence-bound public agreements. A sponsor funds measurable goals, a named steward accepts the protocol, and later observations are evaluated against the original baseline. GenLayer is used only for the irreducibly semantic question: does heterogeneous field evidence support each declared outcome?

## Protocol

- `fund_pact` locks GEN with a place, at least two goals, a detailed measurement protocol, two distinct HTTPS baseline sources, and a named steward. In that same funding transaction, validators fetch the baseline and commit its exact snapshots and SHA-256 digests.
- The freeze validator recomputes every leader-returned snapshot digest and rejects mismatched snapshot/digest arrays before state can be stored.
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

- Contract: `0xbB65Bd3ffE609873fCf26ABa6aC8B5383b2B2e5d`
- Deploy tx: `0x311cc47bd2a78bd85e389e19ff913a202715b209ffab6e93aa49e55bcd774ad9`
- Live app: `https://canopypact.pages.dev/`

## Proven StudioNet lifecycle

- Sponsor funding and validator-checked baseline freeze: `0x260555b6abeccff0d37e3ee8ac283c1a75b94429aedc1a456212ed28778146a6`
- Named steward acceptance from a different wallet: `0x7fa3957ebbcd2abff0bbf87d74eac6ae19e22b52e2c48fd6be81ffbb2c99c157`
- Observation consensus, stored content digests and VERIFIED settlement: `0xe802789f40560461fa173ecc99bb5f9a8e30d60dcbe719024c493ca7a0738c22`

The funded state stores two baseline SHA-256 digests before acceptance. Direct behavioral tests prove forged leader snapshot/digest pairs are rejected and exact pairs are accepted. The final state stores two separate observation digests and an empty unmet-goal set.
