import os
import time
from portfolio import Portfolio


def loading():
    print("\n🚀 Запуск портфолио...")
    for i in range(3):
        print("Загрузка" + "." * (i + 1))
        time.sleep(0.5)
    print("Готово!\n")
    time.sleep(0.5)


def progress_bar():
    print("\n📈 Прогресс: Точка А → Точка Б\n")

    for i in range(1, 21):
        bar = "█" * i + "-" * (20 - i)
        print(f"\r[{bar}] {i * 5}%", end="")
        time.sleep(0.08)

    print("\n")


def menu():
    print("\n" + "=" * 45)
    print("        📌 ПОРТФОЛИО 'ОБО МНЕ'")
    print("=" * 45)
    print("1. 👤 О себе")
    print("2. 🎯 Цель")
    print("3. 📖 История")
    print("4. 🧑‍🏫 Ментор")
    print("5. 📈 Прогресс (текст)")
    print("6. 🎮 Хобби")
    print("7. 💼 Работы")
    print("8. 🔗 GitHub")
    print("9. 🚀 Прогресс-бар (вау)")
    print("0. ❌ Выход")
    print("=" * 45)


def main():
    p = Portfolio("data.json")

    loading()

    while True:
        os.system("cls" if os.name == "nt" else "clear")
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
        elif choice == "9":
            progress_bar()
        elif choice == "0":
            print("Выход...")
            break
        else:
            print("Неверный ввод!")

        input("\nEnter чтобы продолжить...")


if __name__ == "__main__":
    main()