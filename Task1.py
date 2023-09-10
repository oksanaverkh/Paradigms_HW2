# Таблица умножения

# Условие
# На вход подается число n.
# ● Задача
# Написать скрипт в любой парадигме, который выводит на экран таблицу умножения всех чисел от 1 до n.
# Обоснуйте выбор парадигм.


def mult_table(number):
    for i in range(1, number+1):
        print(f'1 * {i} = {i}')


def main():
    number = int(input('Enter a number: '))
    mult_table(number)


if __name__ == "__main__":
    main()
