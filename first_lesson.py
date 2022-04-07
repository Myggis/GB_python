# 1. Поработайте с переменными, создайте несколько, выведите на экран.
# Запросите у пользователя некоторые числа и строки и сохраните в переменные, затем выведите на экран.


name = 'Игнатий'
age = 27
print(f'Меня зовут {name} и мне {age} лет')

name = input('Введите своё имя: ')
age = int(input('Введите сколько Вам лет: '))
print(f'Вас зовут {name} и вам {age} лет (года)')

# 2. Пользователь вводит время в секундах.
# Переведите время в часы, минуты, секунды и выведите в формате чч:мм:сс. Используйте форматирование строк
time_sec = int(input('Как долго вы учите python в секундах? '))
time_h = time_sec // 3600
time_m = (time_sec - time_h * 3600) // 60
time_sec = time_sec - (time_sec // 60 * 60)

result = f'{time_h}:{time_m}:{time_sec}'

print(result)

# 3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369

number = int(input('Введите число n: '))
t = str(number)
t1 = t+t
t2 = t+t+t
result = number + int(t1) + int(t2)
print(result)

# 4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

number = int(input('Введите целое положительное число: '))
max_numb = number % 10
number = number // 10
while number >= 1:
    if number % 10 > max_numb:
        max_numb = number % 10
    number = number // 10
print(max_numb)

# 5. Запросите у пользователя значения выручки и издержек фирмы. Определите, с каким финансовым результатом работает фирма.
# Например, прибыль — выручка больше издержек, или убыток — издержки больше выручки. Выведите соответствующее сообщение.
# 6. Если фирма отработала с прибылью, вычислите рентабельность выручки. Это отношение прибыли к выручке.
# Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчёте на одного сотрудника.

a = int(input('Введите размер Вашей выручки: ')) # выручка
b = int(input('Введите размер Ваших издержек: ')) # издержки

if a > b:
    c = a - b
    print(f'Ваша выручка больше издержек на {a - b}. Рентабильность составила: {a / b}')
    d = int(input('Введите сколько у Вас работников: '))
    print(f'Прибыль в расчете на одного работника: {c / d}')
elif a < b:
    print(f'Ваши издержки больше выручки на {b - a}')
else:
    print('Вы вышли в ноль!')

# 7 (Дополнительно). Спортсмен занимается ежедневными пробежками. В первый день его результат составил a километров.
# Каждый день спортсмен увеличивал результат на 10% относительно предыдущего.
# Требуется определить номер дня, на который результат спортсмена составит не менее b километров.
# Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.

a = int(input('Введите результат первого дня: ')) # Со скольки стартовал
b = int(input('Введите желаемый результат ')) # Что надо достигнуть
count = 1 # Дни

while a < b:
    count += 1
    a = a + a * 0.1
    print(f'день № {count}. Пробежал {a} километров(а)')




