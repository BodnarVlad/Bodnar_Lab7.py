Завдання 1
import random

answers = ["папуга", "пилосос", "єдиноріг"]
correct_answer = random.choice(answers)
hints = {
    "папуга": "Я можу повторювати твої слова.",
    "пилосос": "Я люблю шуміти та прибирати.",
    "єдиноріг": "У мене є ріг і я з казки."
}

print("Вгадай, хто я: живий, неживий чи вигаданий об'єкт?")
attempts = 5

while attempts > 0:
    try:
        guess = input("Твоя версія: ").strip().lower()
        if not guess.isalpha():
            raise ValueError("Введи слово!")
        if guess == correct_answer:
            print("Так, це я! Перемога!")
            break
        else:
            if random.choice([True, False]):
                print("Підказка:", hints[correct_answer])
            else:
                print("Не вгадав. Спробуй ще.")
            attempts -= 1
    except ValueError as e:
        print("Помилка:", e)
else:
    print("Ти програв. Я був -", correct_answer)

Завдання 2
import random

character = "Леонардо да Вінчі"
hints = [
    "Я жив у епоху Відродження.",
    "Я малював, але також конструював машини.",
    "Мою найвідомішу картину всі знають.",
    "Я народився в Італії."
]

print("Вгадай, хто я? Відома особа.")
random.shuffle(hints)

for i in range(random.randint(3, 4)):
    if input("Хочеш підказку? (так/ні): ").lower() == "так":
        print("Підказка:", hints[i])

guess = input("Твоя остаточна відповідь: ").strip().lower()

if "да вінчі" in guess or "леонардо" in guess:
    if random.choice([True, False]):
        print("Ого! Ти вгадав! А може й ні...")
    else:
        print("Ну, майже. Але ні.")
else:
    print("Невдача. Це був Леонардо да Вінчі.")

Завдання 3 
import random

print("Вітаю в дивній грі!")
print("Обери категорію: їжа, місто, предмет, птах")

категорія = input("Твій вибір: ").lower()

варіанти = {
    "їжа": ["піца", "борщ", "бургер"],
    "місто": ["львів", "київ", "харків"],
    "предмет": ["стіл", "ручка", "книга"],
    "птах": ["ворона", "синиця", "лелека"]
}

if категорія not in варіанти:
    print("Цікава категорія... Але продовжимо.")
    категорія = random.choice(list(варіанти.keys()))

правильна = random.choice(варіанти[категорія])
спроби = 0

while True:
    спроба = input("Введи свій варіант: ").lower()
    спроби += 1

    if спроба.strip() == "":
        print("Незрозуміло. Напиши щось інше.")
        continue

    правдива = random.choice([True, False])

    if правдива:
        if спроба == правильна:
            print("Можливо, це правильна відповідь.")
        else:
            print("Можливо, це не вона.")
    else:
        інше = random.choice(sum(варіанти.values(), []))
        print("А може, це", інше)

    if random.randint(1, 10) == 3:
        print("\nГра раптово завершилась.")
        break

print("\nКінець гри.")
if спроба == правильна:
    print("Якщо ти уважний — ти виграв.")
else:
    print("Спробуй ще якось.")
