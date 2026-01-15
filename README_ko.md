# makeastar

별 찍기 패턴을 출력하기 위한 **초경량** 파이썬 패키지입니다.  
복잡한 반복문 없이, 임포트하고 호출하기만 하면 됩니다.

## 특징

- **최적화**: 제너레이터 표현식과 f-string을 사용하여 효율성을 극대화했습니다.
- **쉬운 사용**: 직관적인 함수 이름과 **한국어 발음 별칭** 지원 (예: `star.samgak(5)`).
- **유연성**: 삼각형의 가로와 세로 길이를 자유롭게 조절 가능.
- **경량화**: 코드가 매우 간결합니다.

## 설치

```bash
pip install makeastar
```

(또는 로컬 설치)

```bash
pip install .
```

## 사용법

```python
import star

# 1. 삼각형 (별칭: samgak, tri)
star.triangle(5)       # 가로=5, 기본 높이=5
star.samgak(5, 10)     # 가로=5, 높이=10
star.tri(5)

# 2. 우측 정렬 삼각형 (별칭: usamgak, rtri)
star.right_triangle(5)
star.usamgak(5)

# 3. 역삼각형 (별칭: yeoksamgak, inv)
star.inverted(5)
star.yeoksamgak(5)

# 4. 우측 정렬 역삼각형 (별칭: yeokusamgak, rinv)
star.inverted_right(5)

# 5. 피라미드 (별칭: pyra)
star.pyramid(5)

# 6. 다이아몬드 (별칭: dia)
star.diamond(5)

# 7. 모래시계 (별칭: morae)
star.hourglass(5)

# 8. 화살표 (별칭: hwasal)
star.arrow(5)
```

## 함수 및 별칭 목록

| 함수 (Function) | 별칭 (Alias) | 설명 | 매개변수 |
|----------|-------|-------------|------------|
| `triangle` | `samgak`, `tri` | 좌측 정렬 직각 삼각형 | `(width, height=5, char='*')` |
| `right_triangle` | `usamgak`, `rtri` | 우측 정렬 직각 삼각형 | `(width, height=5, char='*')` |
| `inverted` | `yeoksamgak`, `inv` | 역 직각 삼각형 | `(width, height=5, char='*')` |
| `inverted_right` | `yeokusamgak`, `rtinv`| 우측 정렬 역 직각 삼각형 | `(width, height=5, char='*')` |
| `pyramid` | `pyra` | 중앙 정렬 피라미드 | `(n, char='*')` |
| `diamond` | `dia` | 다이아몬드 | `(n, char='*')` |
| `hourglass` | `morae` | 모래시계 | `(n, char='*')` |
| `arrow` | `hwasal` | 화살표 | `(n, char='*')` |

## 라이선스

이 프로젝트는 MIT 라이선스를 따릅니다.
