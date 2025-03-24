num = int(input("출력할 구구단 숫자를 입력하세요: "))

print(f"\n--- {num}단 ---")
for i in range(1, 10):
    print(f"{num} x {i} = {num * i}")