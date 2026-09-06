# CanopyPact

CanopyPact turns ecological outcome grants into evidence-bound public agreements. A sponsor funds measurable goals, a named steward accepts the protocol, and later observations are evaluated against the original baseline. GenLayer is used only for the irreducibly semantic question: does heterogeneous field evidence support each declared outcome?

## Protocol

- `fund_pact` locks GEN with a place, at least two goals, a detailed measurement protocol, two distinct HTTPS baseline sources, and a named steward. In that same funding transaction, validators fetch the baseline and commit its exact snapshots and SHA-256 digests.
- The freeze validator recomputes every leader-returned snapshot digest and rejects mismatched snapshot/digest arrays before state can be stored.
- `accept_pact` prevents anyone except that steward from taking responsibility.
- Acceptance opens a 30-day evidence window. If the pact remains unresolved, the sponsor can call `recover_expired` and recover the full grant without depending on the steward.
- `submit_observations` makes every validator compare independently fetched later observations with the immutable baseline snapshots captured at funding, then recompute the bounded outcome, exact unmet-goal indexes and observation digests.
- Baseline and observation URLs are parsed as HTTPS origins and normalized paths; malformed sources, duplicate slots, and reused observation origins are rejected.
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

- Contract: `0x493A0Afb7440a0f403C8E9D560F8CdB3FDbE783D`
- Deploy tx: `0x39274688c014d7ac309f9a00cc244819b74b42d7717a2959a7c04d7a54f243cb`
- Reviewed source: `656ae3f30493cd3cddbfdd44a265a975439b3af4`
- Live app: `https://canopypact.pages.dev/`

## Proven StudioNet lifecycle

- Sponsor funding and validator-checked baseline freeze: `0x0930369f31b572919e3d50abbb4b27118b6307f3acd5ece9e21080937c5b5f2c`
- Named steward acceptance from a different wallet: `0xd2ee681b97573f5c411d33871f293c38cb380661b5624888471b336a3b7a0c89`
- Observation consensus, stored content digests and VERIFIED settlement: `0x3c68de83e415de0653c664324a3d61525b3b464555cd28a357c9bfa0e51b9f4d`

The funded state stores two baseline SHA-256 digests before acceptance. Direct behavioral tests prove forged leader snapshot/digest pairs are rejected and exact pairs are accepted. The final state stores two separate observation digests and an empty unmet-goal set. The complete accepted run is recorded in `evidence/network-run.json`.
