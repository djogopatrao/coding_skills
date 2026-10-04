---
name: bonsai-c
description: Apply C correctness, compiler, ABI and target constraints while implementing or debugging host, embedded or cross-compiled C.
---

# C
Read `bonsai-core`; use with one workflow.
1. Identify the existing build command, compiler, C standard, flags and target. Distinguish host utilities from target code. For SDCC/embedded targets, verify actual widths, memory model, address spaces, endianness and available runtime; host compilation is insufficient.
2. Inspect declarations and target types before writing a harness; reuse the target build and fixtures. Do not infer C behavior from Python or host-only tests. Inspect touched paths for bounds, termination, signedness/promotions, overflow, shifts, pointer validity, aliasing, alignment, lifetime and ownership. Check allocation/error cleanup where applicable. Preserve target-specific documented behavior.
3. Keep declarations, definitions and callers consistent. Preserve linkage, ABI/struct layout and target qualifiers. Avoid macro side effects and new unsupported language features. Do not hide warnings with casts or changed flags.
4. Add a focused behavior/regression test where feasible. Build the smallest affected target using the project toolchain; then run relevant tests and required broader checks.
5. Use sanitizers/Valgrind only on compatible host builds when useful. Report compiler diagnostics, exact build/test commands and outstanding device/emulator checks. Never equate host diagnostics with target validation.
