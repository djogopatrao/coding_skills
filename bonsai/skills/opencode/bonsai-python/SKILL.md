---
name: bonsai-python
description: Apply Python environment, version, import, resource and test conventions while implementing or debugging Python code.
---

# Python
Read `bonsai-core`; use with one workflow.
1. Inspect the relevant manifest/lock, supported Python versions and existing runner. Reuse the configured venv, uv, Poetry, Conda or container. Do not create parallel environments, install globally or upgrade dependencies just to start.
2. Run tests through that interpreter, e.g. `.venv/bin/python -m pytest tests/test_feature.py` only if the project uses pytest. Inspect configured markers/fixtures; do not assume offline/live selection syntax.
3. Before reproductions, inspect parser inputs, dataclass/slots definitions and nested result fields. Do not assume `vars()` works or payload fields are top-level. Reuse fixtures; distinguish harness errors from product failures. Preserve package layout, API, typing and exception conventions. Diagnose imports through package installation/module invocation; do not patch `sys.path` to mask the problem. Use only syntax/APIs supported by the declared versions.
4. Check touched paths for resource cleanup, mutable defaults/shared state, broad exception handling and blocking work in async code. Test relevant failure paths. Make tests deterministic; mock external I/O boundaries.
5. Use existing lint/type/format tools and dependency policy. If a dependency is required, update the project's manifest/lock. Run affected tests and configured required checks; do not claim import or compilation checks validate behavior.
