# Extreme Optimization Plan

Improve the performance and resource efficiency of `makeastar` through caching, memory management, and algorithmic refinement.

## User Review Required

> [!NOTE]
> All core functionalities remain unchanged. `functools.lru_cache` will be used, which depends on the inputs being hashable (already true for [int](file:///home/rheehose/%EB%AC%B8%EC%84%9C/%EA%B0%9C%EB%B0%9C%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8/pypack_makeastar/src/star/__init__.py#43-52), [str](file:///home/rheehose/%EB%AC%B8%EC%84%9C/%EA%B0%9C%EB%B0%9C%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8/pypack_makeastar/src/star/__init__.py#14-16)).

## Proposed Changes

### Core Logic ([src/star/__init__.py](file:///home/rheehose/%EB%AC%B8%EC%84%9C/%EA%B0%9C%EB%B0%9C%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8/pypack_makeastar/src/star/__init__.py))

#### [MODIFY] [__init__.py](file:///home/rheehose/문서/개발프로젝트/pypack_makeastar/src/star/__init__.py)
- **Caching Layer**:
    - Wrap shape functions ([triangle](file:///home/rheehose/%EB%AC%B8%EC%84%9C/%EA%B0%9C%EB%B0%9C%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8/pypack_makeastar/src/star/__init__.py#53-59), [pyramid](file:///home/rheehose/%EB%AC%B8%EC%84%9C/%EA%B0%9C%EB%B0%9C%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8/pypack_makeastar/src/star/__init__.py#81-87), etc.) with `@functools.lru_cache` to store pre-computed [Pattern](file:///home/rheehose/%EB%AC%B8%EC%84%9C/%EA%B0%9C%EB%B0%9C%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8/pypack_makeastar/src/star/__init__.py#9-32) objects.
    - Add `_cached_str` and `_cached_lines_str` to the [Pattern](file:///home/rheehose/%EB%AC%B8%EC%84%9C/%EA%B0%9C%EB%B0%9C%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8/pypack_makeastar/src/star/__init__.py#9-32) class to avoid repeating `'\n'.join(lines)`.
- **Memory Optimization**:
    - Implement `__slots__ = ('lines', '_cached_str')` for the [Pattern](file:///home/rheehose/%EB%AC%B8%EC%84%9C/%EA%B0%9C%EB%B0%9C%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8/pypack_makeastar/src/star/__init__.py#9-32) class.
- **Algorithmic Tweak**:
    - Optimize string generation by pre-calculating character repeats where possible.
    - Inline simple calculations.

## Verification Plan

### Automated Tests
- Run existing [tests/test_star.py](file:///home/rheehose/%EB%AC%B8%EC%84%9C/%EA%B0%9C%EB%B0%9C%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8/pypack_makeastar/tests/test_star.py) to ensure no regression.
- Benchmarking: Create a script to compare the speed of 1000 pattern generations before and after optimization.

### Manual Verification
- Verify that `Pattern + Pattern` still works and uses the cache where possible.
