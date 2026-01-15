# makeastar

별 찍기 패턴을 출력하기 위한 **초경량** 파이썬 패키지입니다.  
복잡한 반복문 없이, 임포트하고 호출하기만 하면 됩니다.

## 특징

- **최적화**: 제너레이터 표현식과 f-string을 사용하여 효율성을 극대화했습니다.
- **사용 편의성**: 직관적인 함수 이름 (예: `star.pyramid(5)`).
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

# 1. 삼각형 (Triangle)
star.triangle(5)

# 2. 역삼각형 (Inverted Triangle)
star.inverted(5)

# 3. 피라미드 (Pyramid)
star.pyramid(5)

# 4. 다이아몬드 (Diamond)
star.diamond(5)

# 5. 모래시계 (Hourglass)
star.hourglass(5)

# 6. 화살표 (Arrow)
star.arrow(5)
```

## 지원하는 패턴

| 함수 | 설명 |
|----------|-------------|
| `triangle(n)` | 왼쪽 정렬된 직각 삼각형을 출력합니다. |
| `inverted(n)` | 역 직각 삼각형을 출력합니다. |
| `pyramid(n)` | 중앙 정렬된 피라미드를 출력합니다. |
| `diamond(n)` | 다이아몬드 모양을 출력합니다. |
| `hourglass(n)` | 모래시계 모양을 출력합니다. |
| `arrow(n)` | 오른쪽 화살표 모양을 출력합니다. |

## 라이선스

이 프로젝트는 MIT 라이선스를 따릅니다.
