# 1. Создать программный файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных будет свидетельствовать пустая строка.
text = ''

while True:
    t = input('введите текст: ')
    text = text + t + '\n'
    if t == '':
        break

with open('text.txt', 'w+', encoding='utf-8') as f:
    f.write(text)
    f.seek(0)
    content = f.read()
    print(content)



# 2. Создать текстовый файл (не программно), сохранить в нём несколько строк,
# выполнить подсчёт строк и слов в каждой строке.

with open("for_2.txt", "r", encoding='utf-8') as my_f:
    lines = 0
    words = 0
    letters = 0
    q = ''
    for line in my_f:
        lines += 1
        letters += len(line)
        q += line
    qwe = q.split()
    words = len(qwe)

    print("Lines (строки) :", lines)
    print("Words (слова) :", words)
    print("Letters (символы) :", letters)

# 3. Создать текстовый файл (не программно). Построчно записать фамилии сотрудников и величину
# их окладов (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тысяч,
# вывести фамилии этих сотрудников. Выполнить подсчёт средней величины дохода сотрудников.

# Пример файла:

# Иванов 23543.12
# Петров 13749.32

sal = {}    # Словарь сотрудник : оклад
sal_less_20k = {}   # Словарь сотрудник : оклад с зп меньше 20000
ppl_ls_20 = []  # Список сотрудников с зп меньше 20000
sal_only = []   # Список всех зарплат
sal_avg = 0     # Средняя зп
with open('salary.txt', 'r', encoding='utf-8') as my_sal:
    info = {}
    for line in my_sal:
        ls = line.split()
        name = ls[0]
        salary = float(ls[1])
        info = {name: salary}
        sal.update(info)
        if info.get(name) < 20000:
            sal_less_20k.update(info)
for el in sal_less_20k.keys():
    ppl_ls_20.append(el)
for el in sal.values():
    sal_only.append(el)
sal_avg = round(sum(sal_only) / len(sal_only), 2)
print(f'Список сотрудников, чей оклад меньше 20000: {ppl_ls_20}')
print(f'Средняя зарплата всех сотрудников: {sal_avg}')

# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Напишите программу, открывающую файл на чтение и считывающую построчно данные. При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Напишите программу, открывающую файл на чтение и считывающую построчно данные. При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

translater = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
my_list = []
with open('for_4.txt', 'r') as f4:
    qwe = f4.read()
for key in translater.keys():
    qwe = qwe.replace(key, str(translater[key]))
with open('for4a.txt', 'w', encoding='utf-8') as f4a:
    f4a.write(qwe)

# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделённых пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить её на экран.
with open('for5.txt', 'w') as f5:
    a = ''
    while True:
        b = input('вВЕДИТЕ число: ')
        if b.isdigit() == True:
            a = a + b + ' '
            c = input('Продолжить? Y/N: ').upper()
            while c != 'N' and c != 'Y':
                c = input('Продолжить? Y/N: ').upper()
                continue
            if c == 'N':
                break
            elif c == 'Y':
                continue
        if b.isdigit() == False:
            print('Число!')
    f5.write(a)

with open('for5.txt', 'r') as f5r:
    qwe = f5r.read()
    b = []
    for el in qwe.split():
        b.append(int(el))
    c = sum(b)
    print(f'Сумма цифр в файле = {c}')


# 6. Сформировать (не программно) текстовый файл. В нём каждая строка должна описывать учебный предмет и наличие лекционных,
# практических и лабораторных занятий по предмету. Сюда должно входить и количество занятий. Необязательно, чтобы для каждого предмета были все типы занятий.
# Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести его на экран.
# Примеры строк файла: Информатика: 100(л) 50(пр) 20(лаб).
# Физика: 30(л) — 10(лаб)
# Физкультура: — 30(пр) —
# Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}

with open('for_6.txt', 'r', encoding='utf-8') as file:
    onstring = file.read().split('\n')

dict = {}
for item in onstring:
    key = item.split(':')[0]
    value = item.split(': ')[1]
    v = []
    for i in value:
        if i.isdigit() == True:
            v.append(i)
        if i.isdigit() == False:
            v.append(' ')
    val = []
    val.append("".join(v))
    q = ''.join(map(str, val))
    q = q.split(' ')
    qwe = []
    for el in q:
        if el != '':
            qwe.append(el)
    qwe = list(map(int, qwe))
    qwe = sum(qwe)
    dict[key] = qwe
print(f' Общее количество часов по предметам: \n{dict}')


# 7. Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая строка будет содержать данные о фирме: название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
#
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. Если фирма получила убытки, в расчёт средней прибыли её не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью. Если фирма получила убытки, также добавить её в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
#
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
# Подсказка: использовать менеджер контекста.
import json
profit = {}
pr = {}
prof = 0
prof_aver = 0
i = 0
with open('for_7.txt', 'r') as file:
    for line in file:
        name, firm, earning, damage = line.split()
        profit[name] = int(earning) - int(damage)
        if profit.setdefault(name) >= 0:
            prof = prof + profit.setdefault(name)
            i += 1
    if i != 0:
        prof_aver = prof / i
        print(f'Прибыль средняя - {prof_aver:.2f}')
    else:
        print(f'Прибыль средняя - отсутсвует. Все работают в убыток')
    pr = {'средняя прибыль': round(prof_aver)}
    profit.update(pr)
    print(f'Прибыль каждой компании - {profit}')

with open('file_7.json', 'w') as write_js:
    json.dump(profit, write_js)

    js_str = json.dumps(profit)
    print(f'Создан файл с расширением json со следующим содержимым: \n '
          f' {js_str}')