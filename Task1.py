# Таблица умножения

# Условие
# На вход подается число n.
# ● Задача
# Написать скрипт в любой парадигме, который выводит на экран таблицу умножения всех чисел от 1 до n.
# Обоснуйте выбор парадигм.

# Для решения задачи выбрана структурная и процедурная парадигма.
# Процедурная парадигма использована вследствие необходимости использования функций проверки входящего числа и вывода результатов умножения.
# Структурная парадигма выбрана по причине необходимости использования циклов и отсутствия целесообразности использования оператора goto.

def check():
    n = int(input('Enter a number: '))
    while not 1 <= n <= 10:
        print('Wrong value, try again')
        n = int(input('Enter a number: '))
    return int(n)


def mult_table(number):
    for i in range(1, number+1):
        print()
        for j in range(1, number+1):
            print(f'{i} * {j} = {i*j}')


def main():
    number = check()
    mult_table(number)


if __name__ == "__main__":
    main()
