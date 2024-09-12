# Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток. Программа должна подсказывать “больше” или “меньше” после каждой попытки. Для генерации случайного числа используйте код:
# from random import randintnum = randint(LOWER_LIMIT, UPPER_LIMIT)

from random import randint


def guess_number():
    LOWER_LIMIT = 0
    UPPER_LIMIT = 1000
    number_to_guess = randint(LOWER_LIMIT, UPPER_LIMIT)
    ATTEMPTS = 10
    STEP = 1

    print("Попробуйте угадать число от 0 до 1000. У вас 10 попыток.")

    for attempt in range(ATTEMPTS):
        guess = int(input("Введите вашу догадку: "))

        if guess < LOWER_LIMIT or guess > UPPER_LIMIT:
            print(f"Пожалуйста, введите число в диапазоне от {LOWER_LIMIT} до {UPPER_LIMIT}.")
            continue

        if guess < number_to_guess:
            print("Больше.")
        elif guess > number_to_guess:
            print("Меньше.")
        else:
            print(f"Поздравляю! Вы угадали число {number_to_guess} за {attempt + STEP} попыток!")
            break
    else:
        print(f"К сожалению, вы не угадали. Загаданное число было {number_to_guess}.")

# Запуск игры
guess_number()
