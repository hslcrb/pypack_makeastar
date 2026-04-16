# Feature Enhancement & Refactoring Plan

Refactor `makeastar` to improve shape naming, add a "gem-style" diamond, enhance Korean support, and introduce a flexible composition system.

## Proposed Changes

### Documentation
#### [DELETE] [README_ko.md](file:///home/rheehose/문서/개발프로젝트/pypack_makeastar/README_ko.md)
#### [MODIFY] [README.md](file:///home/rheehose/문서/개발프로젝트/pypack_makeastar/README.md)
- Replace content with a comprehensive Korean version.
- Add sections for the new extensible system and aliases.

---

### Core Logic (`src/star`)
#### [MODIFY] [__init__.py](file:///home/rheehose/문서/개발프로젝트/pypack_makeastar/src/star/__init__.py)
- **Shape Refactoring**:
    - Rename current `diamond` to `rhombus` (마름모).
    - Implement new `diamond` (gem-style).
- **Extension System**:
    - Implement a `Pattern` class or a registry that allows combining shapes (e.g., `triangle(5) + inverted(5)`).
    - Add a `custom` function to register user-defined patterns.
- **Alias Enhancement**:
    - Add `별`, `그려`, `모양` as aliases for `draw`.
    - Add more thorough choseong aliases for all new shapes.
    - Ensure `star.별(5)` works as a shortcut for a default pattern (maybe `pyramid`).

---

### Verification Plan

#### Automated Tests
- Run `PYTHONPATH=src python3 tests/test_star.py` to ensure existing shapes still work (after updating test to expect `rhombus` if needed).
- Add new test cases in `tests/test_new_features.py` for:
    - Gem diamond shape.
    - Composite patterns.
    - Korean aliases.

#### Manual Verification
- Verify that `import star; star.별(5)` works.
- Verify that `star.draw("rhombus 5")` works.
- Check the generated documentation for clarity.
