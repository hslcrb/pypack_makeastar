<div align="center">
  <img src="logo.png" width="300" alt="makeastar logo" />
</div>

# makeastar

반복문 없이 별 찍기 패턴을 생성하는 초경량 파이썬 패키지

## 개요

**makeastar**는 ASCII 별 패턴을 만들 때 반복적인 반복문 작성을 없애줍니다. 반복문을 배우는 파이썬 초보자나 빠른 ASCII 아트가 필요한 개발자에게 완벽합니다.

## 특징

- **제로 보일러플레이트**: 복잡한 중첩 루프를 단일 함수 호출로 대체
- **타입 안전성**: Union 타입을 사용한 완전한 타입 힌트로 유연한 입력 지원
- **최적화된 성능**: `sys.stdout.write`, 제너레이터 표현식, 효율적인 알고리즘 사용
- **다국어 지원**: 영어 및 한국어 별칭 (발음, 초성 변형 포함)
- **유연한 입력**: 정수, 실수, 문자열 입력 가능 - 쉼표, 점, 공백 등을 자동 처리
- **프로덕션 준비 완료**: 포괄적인 유닛 테스트, GitHub Actions CI/CD
- **경량화**: 최소한의 의존성, 순수 파이썬 구현

## 요구 사항

- Python 3.8 이상

## 설치

PyPI에서 설치 (권장):
```bash
pip install makeastar
```

소스에서 설치:
```bash
git clone https://github.com/hslcrb/pypack_makeastar.git
cd pypack_makeastar
pip install .
```

### Docker

Docker를 사용하여 makeastar를 실행할 수도 있습니다:
```bash
docker pull ghcr.io/hslcrb/makeastar:latest
docker run ghcr.io/hslcrb/makeastar:latest
```

## 빠른 시작

```python
import star

# 기본 사용법
star.pyramid(5)
star.diamond(7)
star.triangle(10)

# 한국어 별칭
star.피라미드(5)
star.다이아몬드(7)

# 유연한 입력 처리
star.pyramid("5")           # 문자열 입력
star.pyramid(5.8)           # 실수 입력 (자동 변환)
star.draw("pyramid 5")      # 명령어 문자열 파싱
star.draw("triangle, 10, 5") # 다양한 구분자 처리
```

## 지원하는 패턴

모든 함수는 사용자 지정 가로/세로 크기 및 문자 파라미터를 지원합니다.

### 1. 삼각형 (왼쪽 정렬)
```python
star.triangle(5)
# 출력:
# *
# **
# ***
# ****
# *****
```
**별칭**: `samgak`, `tri`, `삼각형`, `삼`, `ㅅㄱ`, `ㅅㄱㅎ`

### 2. 우측 삼각형 (오른쪽 정렬)
```python
star.right_triangle(5)
# 출력:
#     *
#    **
#   ***
#  ****
# *****
```
**별칭**: `usamgak`, `rtri`, `우측삼각형`, `오른쪽삼각형`, `우삼`, `ㅇㅅㄱ`, `ㅇㅊㅅㄱㅎ`, `ㅇㄹㅉㅅㄱㅎ`

### 3. 역삼각형
```python
star.inverted(5)
# 출력:
# *****
# ****
# ***
# **
# *
```
**별칭**: `yeoksamgak`, `inv`, `역삼각형`, `역삼`, `ㅇㅅ`, `ㅇㅅㄱㅎ`

### 4. 우측 역삼각형
```python
star.inverted_right(5)
# 출력:
# *****
#  ****
#   ***
#    **
#     *
```
**별칭**: `yeokusamgak`, `rtinv`, `rinv`, `우측역삼각형`, `오른쪽역삼각형`, `우역`, `ㅇㅇ`, `ㅇㅊㅇㅅㄱㅎ`, `ㅇㄹㅉㅇㅅㄱㅎ`

### 5. 피라미드
```python
star.pyramid(5)
# 출력:
#     *
#    ***
#   *****
#  *******
# *********
```
**별칭**: `pyra`, `피라미드`, `피라`, `ㅍㄹ`, `ㅍㄹㅁㄷ`

### 6. 다이아몬드
```python
star.diamond(5)
# 출력:
#     *
#    ***
#   *****
#  *******
# *********
#  *******
#   *****
#    ***
#     *
```
**별칭**: `dia`, `다이아몬드`, `다이아`, `다`, `ㄷㅇ`, `ㄷㅇㅇㅁㄷ`

### 7. 모래시계
```python
star.hourglass(5)
# 출력:
# *********
#  *******
#   *****
#    ***
#     *
#    ***
#   *****
#  *******
# *********
```
**별칭**: `morae`, `모래시계`, `모`, `ㅁㄹ`, `ㅁㄹㅅㄱ`

### 8. 화살표
```python
star.arrow(5)
# 출력:
# *
# **
# ***
# ****
# *****
# ****
# ***
# **
# *
```
**별칭**: `hwasal`, `화살표`, `화`, `ㅎㅅ`, `ㅎㅅㅍ`

## 고급 사용법

### 사용자 지정 크기
```python
# 가로와 세로를 다르게 설정한 삼각형
star.triangle(10, 5)   # 가로=10, 세로=5

# 세로를 생략하면 가로와 동일하게 설정됨
star.triangle(7)       # 가로=7, 세로=7
```

### 사용자 지정 문자
```python
star.pyramid(5, char='#')
star.diamond(7, char='@')
```

### 유연한 입력 타입
```python
# 다음은 모두 동일하게 작동합니다
star.pyramid(5)
star.pyramid("5")
star.pyramid(5.0)
star.pyramid(5.9)  # 자동으로 5로 변환
```

### 명령어 문자열 파싱
`draw()` 함수는 유연한 명령어 문자열을 받습니다:
```python
star.draw("pyramid 5")
star.draw("triangle, 10, 5")
star.draw("diamond.7")
star.draw("arrow 3")
```

### 한국어 별칭 사용
```python
# 전체 한국어 이름
star.피라미드(5)
star.다이아몬드(7)

# 줄임말
star.피라(5)
star.다(7)

# 초성 (자음)
star.ㅍㄹ(5)
star.ㄷㅇ(7)

# 한국어 패키지 이름 사용
import 별
별.피라미드(5)
```

## API 레퍼런스

### 삼각형 함수
모든 삼각형 함수는 다음을 받습니다:
- `width` (int | str | float): 삼각형의 가로 크기
- `height` (int | str | float | None): 세로 크기 (None이면 width와 동일)
- `char` (str): 사용할 문자 (기본값: '*')

함수:
- `triangle(width, height=None, char='*')` - 왼쪽 정렬
- `right_triangle(width, height=None, char='*')` - 오른쪽 정렬
- `inverted(width, height=None, char='*')` - 역삼각형 왼쪽 정렬
- `inverted_right(width, height=None, char='*')` - 역삼각형 오른쪽 정렬

### 대칭 도형 함수
모든 대칭 함수는 다음을 받습니다:
- `n` (int | str | float): 크기 파라미터 (기본값: 5)
- `char` (str): 사용할 문자 (기본값: '*')

함수:
- `pyramid(n=5, char='*')` - 중앙 정렬 피라미드
- `diamond(n=5, char='*')` - 다이아몬드
- `hourglass(n=5, char='*')` - 모래시계
- `arrow(n=5, char='*')` - 오른쪽 화살표

### 유틸리티 함수
- `draw(command: str)` - 명령어 문자열 파싱 및 실행

## 테스트

테스트 스위트 실행:
```bash
python -m unittest discover tests
```

## 기여

기여를 환영합니다! 가이드라인은 [CONTRIBUTING_ko.md](CONTRIBUTING_ko.md)를 참조하세요.

## 작성자

**Rheehose (Rhee Creative)**
- 이메일: rheehose@rheehose.com
- GitHub: [@hslcrb](https://github.com/hslcrb)
- Copyright 2008-2026

## 라이선스

이 프로젝트는 MIT 라이선스를 따릅니다. 자세한 내용은 [LICENSE](LICENSE)를 참조하세요.

## 변경 이력

### v1.0 (2026-01-15)
- 첫 안정 버전 출시
- 8가지 패턴 타입과 완전한 한국어/영어 별칭
- 유연한 입력 파싱 (문자열, 실수, 다양한 구분자)
- 타입 힌트 및 최적화된 성능
- 포괄적인 유닛 테스트
- GitHub Actions CI/CD
