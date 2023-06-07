import shutil

'''
Задача №49. Решение в группах
Создать телефонный справочник с
возможностью импорта и экспорта данных в
формате .txt. Фамилия, имя, отчество, номер
телефона - данные, которые должны находиться
в файле.
1. Программа должна выводить данные
2. Программа должна сохранять данные в
текстовом файле
3. Пользователь может ввести одну из
характеристик для поиска определенной
записи(Например имя или фамилию
человека)
4. Использование функций. Ваша программа
не должна быть линейной
фамилия имя отчество телефон
'''
name = None


def start():
    global name
    name = input('Введите имя текстового файла  для работы справочника или exit для выхода: ')
    if name == 'exit':
        return "exit"
    return name


def show_menu():
    print("\nВыберите необходимое действие:\n"
          "0. Создать справочник\n"
          "1. Отобразить весь справочник\n"
          "2. Найти абонента по фамилии\n"
          "3. Найти абонента по номеру телефона\n"
          "4. Добавить абонента в справочник\n"
          "5. Сохранить справочник в текстовом формате\n"
          "6. Удалить абонента\n"
          "7. Изменение данных\n"
          "8. Завершить работу\n")
    choice = int(input('Введите номер действия: ').strip())

    while choice > 8:
        print('Введенный номер не соответствует командам!!!')
        print("\nВыберите необходимое действие:\n"
              "0. Создать справочник\n"
              "1. Отобразить весь справочник\n"
              "2. Найти абонента по фамилии\n"
              "3. Найти абонента по номеру телефона\n"
              "4. Добавить абонента в справочник\n"
              "5. Сохранить справочник в текстовом формате\n"
              "6. Удалить абонента\n"
              "7. Изменение данных\n"
              "8. Завершить работу\n")

        choice = int(input('Введите номер действия: ').strip())
    return choice


def zero():
    with open(f'{name}.txt', 'w+', encoding='utf=8') as f:
        f.write('Мой справочник:\n')
        print(f' Файл и именем {name}.txt успешно создан !')


def funk_1():
    with open(f'{name}.txt', 'r', encoding='utf=8') as n:
        [print(x, end='') for x in n]


def funk_2():
    cursor = input('Введите фамилию: ').strip()
    with open(f'{name}.txt', 'r+', encoding='utf=8') as f:
        [print(x[:-1]) if '\n' in x else print(x) for x in f if cursor.casefold() in x.casefold()]


def funk_3():
    cursor = input('Введите телефон: ').strip()
    with open(f'{name}.txt', 'r+', encoding='utf=8') as f:
        [print(x[:-1]) if '\n' in x else print(x) for x in f if cursor.casefold() in x.casefold()]


def funk_4():
    with open(f'{name}.txt', 'a+', encoding='utf=8') as f:
        first_name = input('Введите Имя: ').strip()
        second_name = input('Введите Фамилию: ').strip()
        three_name = input('Введите Отчество: ').strip()
        number_name = input('Введите номер: ').strip()
        ls = [first_name, second_name, three_name, number_name]
        [f.write(f'{x}\n') if x == number_name else f.write(f'{x}, ') for x in ls]
        print('Запись добавлена')


def funk_5():
    second_name = input('Введите имя файла клона: ').strip()
    with open(f'{second_name}.txt', 'w+', encoding='utf=8') as f:
        return shutil.copy(f'{name}.txt', f'{second_name}.txt')


def funk_6():
    one_flag = input('Введите имя абонента: ').strip()
    two_flag = input('Введите фамилию абонента: ').strip()
    with open(f'{name}.txt', 'r+', encoding='utf=8') as f:
        d = f.readlines()
    with open(f'{name}.txt', 'r+', encoding='utf=8') as f:

        for number, line in enumerate(d, 1):
            if one_flag in line and two_flag in line:
                print(f'{number}: {line}', end='') if number != len(d) else print(f'{number}: {line}', end='\n')
    delete = int(input("Введите норме записи для удаление: ").strip())
    with open(f'{name}.txt', 'w+', encoding='utf=8') as f:
        for number, line in enumerate(d, 1):
            if number != delete:
                f.write(line)
                print('Запись была удалена')


def funk_7():
    global first_names
    print('Выберите номер желаемого изменения\n'
          '1. Изменить Имя\n'
          '2. Изменить Фамилию\n'
          '3. Изменить Отчество\n'
          '4. Изменить Номер телефона\n')

    flag = int(input('Введите номер изменения: ').strip())
    if flag == 1:
        first_names = input('Введите имя которое хотели бы поменять: ').strip()
        second_names = input('Введите имя на которое хотели бы поменять: ').strip()
    elif flag == 2:
        first_names = input('Введите фамилию которую хотели бы поменять: ').strip()
        second_names = input('Введите фамилию на которую хотели бы поменять: ').strip()
    elif flag == 3:
        first_names = input('Введите отчество которое хотели бы поменять: ').strip()
        second_names = input('Введите отчество на которое хотели бы поменять: ').strip()
    elif flag == 4:
        first_names = input('Введите номер телефона который хотели бы поменять: ').strip()
        second_names = input('Введите номер телефона на который хотели бы поменять: ').strip()
    while flag > 4:
        print('Введённый номер не существует')
        print('Выберите номер желаемого изменения\n'
              '1. Изменить Имя\n'
              '2. Изменить Фамилию\n'
              '3. Изменить Отчество\n'
              '4. Изменить Номер телефона\n')
        if flag == 1:
            first_names = input('Введите имя которое хотели бы поменять: ').strip()
            second_names = input('Введите имя на которое хотели бы поменять: ').strip()
        elif flag == 2:
            first_names = input('Введите фамилию которую хотели бы поменять: ').strip()
            second_names = input('Введите фамилию на которую хотели бы поменять: ').strip()
        elif flag == 3:
            first_names = input('Введите отчество которое хотели бы поменять: ').strip()
            second_names = input('Введите отчество на которое хотели бы поменять: ').strip()
        elif flag == 4:
            first_names = input('Введите номер телефона который хотели бы поменять: ').strip()
            second_names = input('Введите номер телефона на который хотели бы поменять: ').strip()

    with open(f'{name}.txt', 'r+', encoding='utf=8') as f:
        d = f.readlines()
    with open(f'{name}.txt', 'r+', encoding='utf=8') as f:
        for numbers, search in enumerate(d, 1):
            if first_names in search:
                print(f'{numbers}: {search}', end='') if numbers != len(d) else print(f'{numbers}: {search}', end='\n')
        num = int(input("Введите номер позиции заменяемой строки: "))
        while num > 4:
            print('Введенный номер не существует!!!')
            num = int(input("Введите номер позиции заменяемой строки: "))
    with open(f'{name}.txt', 'w+', encoding='utf=8') as f:
        for numbers, search in enumerate(d, 1):
            if numbers != num:
                f.write(f'{search}')
            else:
                if numbers == num:
                    new_search = search.replace(first_names, second_names)
                    f.write(f'{new_search}')
                    print(f"в строке {numbers} заменено {first_names} на {second_names}")


def all_functional(menu_number):
    if menu_number == 0:
        return zero()
    elif menu_number == 1:
        return funk_1()
    elif menu_number == 2:
        return funk_2()
    elif menu_number == 3:
        return funk_3()
    elif menu_number == 4:
        return funk_4()
    elif menu_number == 5:
        return funk_5()
    elif menu_number == 6:
        return funk_6()
    elif menu_number == 7:
        return funk_7()


def main():
    print('Приветствую Вас в справочнике')
    s = start()
    if s == 'exit':
        print('Завершение программы.')
    else:
        sh = 0
        while sh < 8:
            sh = show_menu()
            all_functional(sh)

        print('Завершение программы.')


try:
    main()

except Exception as ex:
    while ex:
        print(f'{ex}')
        main()