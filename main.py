# ИИ-комик
def main():
    print("Привет! Я ИИ-комик. Задай мне вопрос или дай команду, связанную с ML или ИИ!")
    user_input = input("Ты: ")
    respond(user_input)

def respond(command):
    if "привет" in command.lower():
        print("ИИ-комик: Привет! Готов поделиться нейронными шутками.")
    elif "как дела" in command.lower():
        print("ИИ-комик: Отлично обучен и готов к шуткам!")
    else:
        print("ИИ-комик: Хм, не знаю такой команды. Попробуй что-то связанное с ML или ИИ!")

if __name__ == "__main__":
    main()