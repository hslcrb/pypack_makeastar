<div align="center">
  <img src="logo.png" width="250" alt="makeastar logo" />
  <h1 align="center">makeastar (별)</h1>
  <p align="center">반복문 없이 별을 찍는 가장 우아하고 빠른 방법</p>
</div>

---

## 🚀 개요

**makeastar**는 파이썬에서 ASCII 별 패턴을 생성하기 위한 초경량, 고성능 패키지입니다. 직관적인 함수 호출, 무한한 패턴 조합, 그리고 한국어 사용자를 위한 완벽한 로컬라이징을 제공합니다.

---

## 🛠 모든 문법 소개

### 1. 기본 사용법 (Basic Shapes)

모든 함수는 `width` (또는 `n`)와 `char` (기본값: `'*'`) 파라미터를 지원합니다.

```python
import star

star.triangle(5)       # 왼쪽 정렬 삼각형
star.right_triangle(5) # 오른쪽 정렬 삼각형
star.pyramid(5)        #Centered 피라미드
star.diamond(5)        #보석 모양 다이아몬드 (New!)
star.rhombus(5)        #마름모 (기존 다이아몬드)
star.hourglass(5)      #모래시계
star.arrow(5)          #화살표
```

### 2. 한국어 별칭 및 초성 (K-Localization)

한국어 사용자를 위해 풀 네임, 줄임말, 초성 별칭을 모두 지원합니다.

| 구분 | 예시 |
| :--- | :--- |
| **전체 이름** | `star.삼각형(5)`, `star.피라미드(5)`, `star.다이아몬드(5)` |
| **줄임말** | `star.삼(5)`, `star.피라(5)`, `star.다(5)` |
| **초성** | `star.ㅅㄱ(5)`, `star.ㅍㄹ(5)`, `star.ㄷㅇ(5)`, `star.ㅁㄹㅁ(5)` |

### 3. 무한 조합 시스템 (Pattern Composition)

`Pattern` 객체 간의 연산을 통해 새로운 모양을 창조할 수 있습니다.

- **수직 합치기 (`+`)**: 두 패턴을 위아래로 붙입니다.
- **수직 반복 (`*`)**: 패턴을 N번 반복합니다.

```python
# 삼각형 위에 역삼각형 붙이기
custom = star.삼(5) + star.역삼(5)
custom.draw()

# 피라미드 3번 반복
triple = star.피라(3) * 3
triple.draw()
```

### 4. 범용 실행 함수 (`draw()`, `별()`)

문자열 명령어나 숫자를 통해 즉시 별을 그릴 수 있습니다.

```python
star.별(5)              # 기본 피라미드 출력
star.그려("삼각형 10")   # 문자열 명령 실행
star.모양(star.dia(5))  # Pattern 객체 출력
```

---

## ⚡ 극단적 최적화 (Extreme Performance)

`makeastar`는 단순한 출력을 넘어 속도와 자원 효율을 극한으로 끌어올렸습니다.

- **LRU Cache**: 동일한 설정의 패턴은 단 한 번만 계산하고 메모리에서 즉시 불러옵니다.
- **Memory Slots**: `__slots__`를 적용하여 객체 생성 메모리 오버헤드를 최소화했습니다.
- **Lazy String Buffering**: 출력 직전에만 문자열 합성을 수행하며, 결과물을 캐싱하여 재사용합니다.

---

## 📦 설치 및 라이선스

```bash
pip install makeastar
```

이 프로젝트는 **MIT 라이선스**를 따릅니다. 대한민국 개발자의 창의력을 응원합니다! 🇰🇷
