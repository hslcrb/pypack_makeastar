<div align="center">
  <h1 align="center">🌟 makeastar (별) v2.0 🌟</h1>
  <p align="center"><b>"별 찍기의 종착역: 진정한 그래픽 엔진으로의 진화"</b></p>
  <p align="center">
    <a href="https://pypi.org/project/makeastar/"><img src="https://img.shields.io/pypi/v/makeastar?color=blue&style=flat-square" alt="PyPI Version" /></a>
    <a href="https://github.com/hslcrb/pypack_makeastar/blob/main/LICENSE"><img src="https://img.shields.io/github/license/hslcrb/pypack_makeastar?color=green&style=flat-square" alt="License" /></a>
  </p>
</div>

---

## 🚀 개요

**makeastar**는 파이썬에서 ASCII 별 패턴을 생성하기 위한 최첨단 그래픽 엔진입니다. 
단순한 텍스트 출력을 넘어, **비트마스크(Bitmask) 최적화**와 **기하학적 연산자**를 통해 무한한 조합과 변형을 지원합니다. 
이제 원, 하트, 커스텀 수식까지 단 한 줄로 구현하세요.

---

## 🛠 주요 문법 및 기능

### 1. 지원하는 모든 도형 (All Shapes)

| 함수명 | 설명 | 한국어 별칭 |
| :--- | :--- | :--- |
| `triangle(w, h)` | 왼쪽 정렬 삼각형 | `삼각형`, `ㅅㄱ` |
| `right_triangle(w, h)` | 오른쪽 정렬 삼각형 | `우측삼각형`, `ㅇㅅㄱ` |
| `pyramid(n)` | 중앙 정렬 피라미드 | `피라미드`, `ㅍㄹ` |
| `rhombus(n)` | 마름모 모양 | `마름모`, `ㅁㄹㅁ` |
| `diamond(n)` | 보석 다이아몬드 | `다이아몬드`, `ㄷㅇ` |
| `circle(r)` | **New!** 기하학적 원 | `원`, `ㅇ` |
| `heart(n)` | **New!** 하트 모양 | `하트`, `ㅎㅌ` |
| `custom(func, w, h)` | **God!** 수식 기반 커스텀 | - |

> [!TIP]
> `custom` 함수를 사용하면 `lambda x, y: x == y` 처럼 수식을 직접 입력하여 상상하는 모든 모양을 그릴 수 있습니다.

### 2. 무한 조합 시스템 (God-Layer Operators)

v2.0부터 지원하는 강력한 비트 연산자들입니다.

- **수직 결합 (`+`)**: 위아래로 이어 붙입니다.
- **수평 결합 (`|`)**: 좌우로 나란히 배치합니다. (높이 자동 패딩)
- **오버레이 결합 (`&`)**: 두 모양을 한 자리에 겹칩니다.
- **배타적 결합 (`^`)**: 겹치는 부분만 지우거나 반전시킵니다 (XOR).
- **마스킹 (`-`)**: 첫 번째 모양에서 두 번째 모양을 깎아냅니다.
- **반전 (`~`)**: 별과 공백을 뒤바꿉니다 (Negative).

```python
# 피라미드 안에 구멍 뚫린 마름모를 겹치고 돌리기
p = (star.pyramid(10) ^ star.rhombus(5)).rotate(90)
p.draw()
```

### 3. 변형 및 변환 (Transformation)

생성된 패턴을 자유자재로 요리하세요.

- `.rotate(angle)`: 90, 180, 270도 회전
- `.flip_h()`: 좌우 반전
- `.flip_v()`: 상하 반전
- `.replace(char)`: 별(*) 대신 원하는 문자로 교체

---

## ⚡ 기술적 정수 (The Engine)

- **Bitmask Core**: 모든 라인을 정수 비트로 처리하여 연산 속도를 CPU 한계치까지 끌어올렸습니다.
- **LRU Cache & Slots**: 메모리와 연산 자원을 극단적으로 아껴 대규모 패턴도 즉각 처리합니다.
- **K-Localization**: `원()`, `하트()`, `별()` 등 친숙한 한국어와 초성 입력을 완벽하게 지원합니다.

---

## 📦 설치법 (Installation)

```bash
pip install makeastar
```

---

<div align="center">
  <p><b>Designed by Rheehose (Rhee Creative)</b></p>
  <p>대한민국의 자유와 창의력을 응원합니다. 🇰🇷👊</p>
</div>
