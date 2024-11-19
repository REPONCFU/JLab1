# ИИ-комик
import random

def main():
    print("Привет! Я ИИ-комик. Задай мне вопрос или дай команду, связанную с ML или ИИ!")
    user_input = input("Ты: ")
    respond(user_input)

JOKES = [
    "Почему нейронная сеть не пошла гулять? Она боялась переобучиться!",
    "Как ИИ пишет любовное письмо? С использованием LSTM!",
    "Почему алгоритм решил стать комиком? Потому что ему нравится делать людей счастливыми с помощью точности!",
    "Что сказал машинный обучающийся крокодил? Я векторизуюсь!"
]

def respond(command):
    if "привет" in command.lower():
        print("ИИ-комик: Привет! Готов поделиться нейронными шутками.")
    elif "как дела" in command.lower():
        print("ИИ-комик: Отлично обучен и готов к шуткам!")
    elif "шутка" in command.lower() or "joke" in command.lower():
        joke = random.choice(JOKES)
        print(f"ИИ-комик: {joke}")
    else:
        print("ИИ-комик: Хм, не знаю такой команды. Попробуй что-то связанное с ML или ИИ!")


if __name__ == "__main__":
    main()