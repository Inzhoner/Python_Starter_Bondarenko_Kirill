# +Змінна

apples = 10  # 140720754779336
var_1 = 10  # 140720754779336
var_2 = 1  # 140720754779048

# //перші два id однакові, бо мають одне посилання
# //на один і той же об'єкт'

#! Python для ефективності використовує один об’єкт для
#! однакових маленьких цілих чисел (від -5 до 256).
#! Це називається інтернування чисел.

print(id(apples))
print(id(var_1))
print(id(var_2))

# +Рядок (str)

a = "hello"

b = "hello"

#  багато рядковий запис--- використовуємо потрійні лапки
d = """hello
world and
hello
you"""

print(a)
print(b)
print(d)

# -методи рядків

# //Оператори +(конкатенація) та * (повторювання)
str_1 = "My name is "
str_2 = "Andrii"
total_str = str_1 + str_2  # Конкатенація строк
print(total_str * 3)  # Повторюємо строку 3 рази

# //Функції len(), upper(), lower()
print(len(total_str))  # Довжина строки (17 символів)

# //Увага: upper() не приймає аргументів!
print(total_str.upper())  # Перетворює всю строку у верхній регістр
print(total_str.lower())  # Перетворює всю строку у нижній регістр

# //lower upper не змінює значення змінної


# //Корисні додатки:
part_upper = total_str[:3].upper() + total_str[3:]
part_upper1 = total_str[:12] + total_str.upper()[12:]
print(part_upper)  # "MY name is Andrii"
print(part_upper1)  # "My name is ANDRII"

# Як це працює:
# total_str[:3] – бере зріз строки (перші 3 символи): "My "
# .upper() – переводить цей зріз у верхній регістр: "MY "
# total_str[3:] – бере решту ст1роки (від 3-го символа до кінця): "name is Andrii"
#  – об'єднує дві частини: "MY " + "name is Andrii"

# Результат:

print(part_upper)  # "MY name is Andrii"

# //Для перевірки регістру:
print(total_str.isupper())  # False
print("HELLO".isupper())  # True

#! Особливості цих методів:
# //Враховують тільки літери (A-Z/a-z).
# //Ігнорують цифри, пробіли та спецсимволи:
print("123".isupper())  # False
print("A B C".isupper())  # True (пробіли ігноруються)

#! Рядки в Python незмінні (immutable).
#! Методи upper(), lower() повертають новий рядок, а не змінюють оригінал.


#  +Числа - (int-15.14)

q = 2
w = 5

print(q + w, q - w, q * w, q / w, q % w, q % w)


#  +Логічні типи (False  True)

x = True
y = False

print(x, y)

print(bool(1))  # True
print(bool(10))  # True
print(bool(0))  # False
print(bool())  # False

# // Оператори порівняння
# ==
# _ !=
# >
# <
# <=
# >=
