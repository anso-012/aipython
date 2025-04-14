# rich 기반 예쁘게 출력되는 동물 아스키 아트 프로그램 (오류 수정 버전)
from rich import print
from rich.panel import Panel

def get_cat():
    return r"""
/\_/\
( o.o )
 > ^ <
"""

def get_dog():
    return r"""
  /  \__
 (  •ㅅ•  )
 (   ‾‾  )ノ
  ""  ""
"""

def get_rabbit():
    return r"""
  (\_/)
  (o.o)
  ( > )
"""

def print_animal(name, art, color="cyan"):
    print(f"\n[bold {color}]🐾 {name}가 등장했어요! 🐾[/bold {color}]")
    print(Panel.fit(art, title=f"[bold {color}]{name} 등장!", border_style=color))

# ▶ 무한 반복 + 종료 조건
while True:
    print("[bold yellow]그림 출력 프로그램[/bold yellow]")
    print("[green]===================[/green]")
    print("[cyan]1. 고양이[/cyan]")
    print("[cyan]2. 강아지[/cyan]")
    print("[cyan]3. 토끼[/cyan]")
    print("[cyan]0. 종료[/cyan]")
    print("[green]===================[/green]")

    try:
        n = int(input("선택(0을 입력하면 종료): "))
    except ValueError:
        print("[red]❌ 숫자를 입력해주세요![/red]")
        continue

    if n == 0:
        print("[bold red]프로그램을 종료합니다.[/bold red]")
        break
    elif n == 1:
        print_animal("고양이", get_cat(), "magenta")
    elif n == 2:
        print_animal("강아지", get_dog(), "blue")
    elif n == 3:
        print_animal("토끼", get_rabbit(), "green")
    else:
        print("[red]❌ 잘못입력하셨습니다. 1~3 또는 0만 입력 가능합니다.[/red]")
        