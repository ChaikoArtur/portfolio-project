import json

class Portfolio:
    def __init__(self, file_path):
        with open(file_path, "r", encoding="utf-8") as f:
            self.data = json.load(f)

    def show_about(self):
        a = self.data["about"]
        print("\n👤 О СЕБЕ")
        print(f"Имя: {a['name']}")
        print(f"Возраст: {a['age']}")
        print(f"Роль: {a['role']}")
        print(f"Описание: {a['description']}")
        print("Факты:")
        for fact in a["facts"]:
            print("-", fact)

    def show_goal(self):
        g = self.data["goal"]
        print("\n🎯 МОЯ ЦЕЛЬ")
        print("Главная цель:", g["main_goal"])
        print("Краткосрок:", g["short_term"])
        print("Мотивация:", g["motivation"])

    def show_story(self):
        s = self.data["story"]
        print("\n📖 ИСТОРИЯ")
        print(s["start"])
        print(s["development"])
        print(s["now"])

    def show_mentor(self):
        m = self.data["mentor"]
        print("\n🧑‍🏫 МЕНТОР")
        print("Имя:", m["name"])
        print("Роль:", m["role"])
        print("Чему научился:")
        for i in m["what_learned"]:
            print("-", i)

    def show_progress(self):
        p = self.data["progress"]
        print("\n📈 ПРОГРЕСС")
        print("Было:", p["before"])
        print("Стало:", p["after"])
        print("Итог:", p["growth"])

    def show_hobbies(self):
        print("\n🎮 ХОББИ")
        for h in self.data["hobbies"]:
            print("-", h)

    def show_works(self):
        print("\n💼 РАБОТЫ")
        for w in self.data["works"]:
            print(f"\nНазвание: {w['title']}")
            print(f"Описание: {w['description']}")
            print(f"Технологии: {w['tech']}")

    def show_github(self):
        g = self.data["github"]
        print("\n🔗 GITHUB")
        print(g["url"])
        print(g["description"])