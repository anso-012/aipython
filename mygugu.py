# 숫자 두개를 입력을 받아서
# +, -. *, / 를 출력 하는 프로그램을 만들어 보자
while True:
    try:
        # 사용자 입력 받기
        a = float(input("첫 번째 숫자를 입력하세요: "))
        b = float(input("두 번째 숫자를 입력하세요: "))

        # 사칙연산 수행
        print(f"\n🔹 덧셈: {a} + {b} = {a + b}")
        print(f"🔹 뺄셈: {a} - {b} = {a - b}")
        print(f"🔹 곱셈: {a} * {b} = {a * b}")

        # 0으로 나누기 방지
        if b != 0:
            print(f"🔹 나눗셈: {a} / {b} = {a / b:.2f}")  # 소수점 2자리까지 표시
        else:
            print("❌ 0으로 나눌 수 없습니다!")

        break  # 정상적으로 계산 완료되면 종료

    except ValueError:
        print("❌ 숫자를 정확히 입력해주세요!")
