from portfolio import Portfolio

def menu():
    print("""
========================
   ПОРТФОЛИО "ОБО МНЕ"
========================
1. О себе
2. Цель
3. История
4. Ментор
5. Прогресс
6. Хобби
7. Работы
8. GitHub
0. Выход
""")

def main():
    p = Portfolio("data.json")

    while True:
        menu()
        choice = input("Выберите пункт: ")

        if choice == "1":
            p.show_about()
        elif choice == "2":
            p.show_goal()
        elif choice == "3":
            p.show_story()
        elif choice == "4":
            p.show_mentor()
        elif choice == "5":
            p.show_progress()
        elif choice == "6":
            p.show_hobbies()
        elif choice == "7":
            p.show_works()
        elif choice == "8":
            p.show_github()
        elif choice == "0":
            print("Выход...")
            break
        else:
            print("Неверный ввод!")

        input("\nEnter чтобы продолжить...")

if __name__ == "__main__":
    main()