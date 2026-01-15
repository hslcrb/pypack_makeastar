def print_star_pyramid(lines):
    print("1. 기본 삼각형 (Left-aligned Triangle)")
    for i in range(1, lines + 1):
        print('*' * i)
    
    print("\n2. 역삼각형 (Inverted Triangle)")
    for i in range(lines, 0, -1):
        print('*' * i)

    print("\n3. 피라미드 (Pyramid)")
    for i in range(1, lines + 1):
        # 공백 출력 + 별 출력
        # 공백은 (총 줄 수 - 현재 줄 수) 만큼
        # 별은 (2 * 현재 줄 수 - 1) 만큼
        print(' ' * (lines - i) + '*' * (2 * i - 1))

if __name__ == "__main__":
    n = 5
    print(f"줄 수: {n}\n")
    print_star_pyramid(n)
