def print_ascii_art(choice):
    ascii_art = {
        "1": """
        (\\_/)
        (o.o)
        (> <)  - 토끼
        """,
        "2": """
        /\\_/\\  
       ( o.o ) 
        > ^ <  - 고양이
        """,
        "3": """
         ,--.
        (o  o)  
        |  /\|  - 올빼미
        """,
    }

    # 입력값이 존재하면 출력, 없으면 오류 메시지 출력
    print(ascii_art.get(choice, "❌ 잘못된 입력입니다. 1, 2, 3 중 하나를 입력하세요!"))

# 사용자 입력받기
user_input = input("숫자를 입력하세요 (1, 2, 3): ")
print_ascii_art(user_input)

for i in range(3):
    print(i)
    print_cat()

#    print_cat()