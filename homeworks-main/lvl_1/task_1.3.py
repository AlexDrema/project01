# Задача 1.3.

# Напишите скрипт, который принимает от пользователя номер месяца, 
# а возвращает количество дней в нем.
# Результат проверки вывести на консоль
# Допущение: в феврале 28 дней
# Если номер месяца некорректен - сообщить об этом

# Например,
    # Введите номер месяца: 3
    # Вы ввели март. 31 дней

    # Введите номер месяца: 2
    # Вы ввели февраль. 28 дней

    # Введите номер месяца: 15
    # Такого месяца нет!

months = ['', 'январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь', 'декабрь']

x = int(input('Введите номер месяца: '))
if 1 > x or x > 12:
    print("Такого месяца нет!")
elif x == 2:
    print("Вы ввели февраль. 28 дней.")
elif x in [1, 3, 5, 7, 8, 10, 12]:
    print(f"Вы ввели {months[x]}. 31 день.")
else:
    print(f"Вы ввели {months[x]}. 30 дней.")
