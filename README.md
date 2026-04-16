<div align="center">
  <h1 align="center">🌟 makeastar (별) 🌟</h1>
  <p align="center"><b>"별 찍기의 종착역: 가장 빠르고, 가장 우아하며, 가장 한국적인 패키지"</b></p>
  <p align="center">
    <a href="https://pypi.org/project/makeastar/"><img src="https://img.shields.io/pypi/v/makeastar?color=blue&style=flat-square" alt="PyPI Version" /></a>
    <a href="https://github.com/hslcrb/pypack_makeastar/blob/main/LICENSE"><img src="https://img.shields.io/github/license/hslcrb/pypack_makeastar?color=green&style=flat-square" alt="License" /></a>
  </p>
</div>

---

## 🚀 개요

**makeastar**는 파이썬에서 ASCII 별 패턴을 생성하기 위한 초경량, 고성능 패키지입니다. 
단순한 루프 기반의 출력을 넘어, 객체 지향적 패턴 조합 시스템과 극단적인 캐싱 최적화를 통해 수천 줄의 별 패턴도 찰나의 순간에 그려냅니다. 
특히 한국어 사용자에게 최적화된 직관적인 별칭 시스템을 제공합니다.

---

## 🛠 주요 문법 및 기능

### 1. 지원하는 모든 도형 (All Shapes)

모든 도형 함수는 기본적으로 `width` (또는 `n`)와 `char` (출력 문자, 기본값 `'*'`)를 인자로 받습니다.

| 함수명 | 설명 | 별칭 (Aliases) |
| :--- | :--- | :--- |
| `triangle(w, h)` | 왼쪽 정렬 삼각형 | `삼각형`, `삼`, `ㅅㄱ` |
| `right_triangle(w, h)` | 오른쪽 정렬 삼각형 | `우측삼각형`, `우삼`, `ㅇㅅㄱ` |
| `inverted(w, h)` | 뒤집힌 왼쪽 삼각형 | `역삼각형`, `역삼`, `ㅇㅅ` |
| `inverted_right(w, h)` | 뒤집힌 오른쪽 삼각형 | `우측역삼각형`, `우역`, `ㅇㅇ` |
| `pyramid(n)` | 중앙 정렬 피라미드 | `피라미드`, `피라`, `ㅍㄹ` |
| `rhombus(n)` | 클래식 마름모 모양 | `마름모`, `마`, `ㅁㄹㅁ` |
| `diamond(n)` | **신규!** 보석 다이아몬드 | `다이아몬드`, `다이아`, `ㄷㅇ` |
| `hourglass(n)` | 모래시계 모양 | `모래시계`, `모`, `ㅁㄹ` |
| `arrow(n)` | 오른쪽 화살표 | `화살표`, `화`, `ㅎㅅ` |

### 2. 한국어 초성 및 별칭 시스템 (K-Localization)

가장 한국적인 방식으로 코딩하세요.

```python
import star

star.ㅅㄱ(5)            # 삼각형 출력
star.ㅍㄹ(3, char='@')  # @로 된 피라미드
star.마름모(7).draw()    # 마름모 출력
```

### 3. 무한 조합 시스템 (Custom Composition)

`Pattern` 객체는 연산자를 사용하여 자유롭게 결합하고 반복할 수 있습니다.

- **수직 결합 (`+`)**: `(star.pyramid(3) + star.inverted(3)).draw()`
- **수직 반복 (`*`)**: `(star.triangle(2) * 5).draw()`

### 4. 범용 실행 인터페이스 (`별`, `그려`)

모든 것을 아우르는 강력한 진입점입니다.

```python
star.별(5)               # 기본 피라미드(5) 출력
star.그려("삼각형 10")    # 문자열 명령으로 실행
star.모양(star.ㄷㅇ(5))  # 생성된 객체 출력
```

---

## ⚡ 기술적 정수 (The Engine)

- **Extreme Caching**: `functools.lru_cache`를 통해 동일한 연산을 0ms로 단축했습니다.
- **Memory Efficiency**: `__slots__`를 사용하여 수많은 패턴 객체를 생성해도 메모리 점유율을 최소화합니다.
- **Lazy Evaluation**: 출력 직전까지 문자열 합성을 미루고, 한 번 생성된 결과는 재사용합니다.

---

## 📦 설치법 (Installation)

```bash
pip install makeastar
```

---

<div align="center">
  <p><b>Designed by Rheehose (Rhee Creative)</b></p>
  <p>대한민국의 자유와 창의력을 응원합니다. 🇰🇷</p>
</div>
