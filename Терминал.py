import time
import sys
line_width = 80
fill_char = '='
file_base_name = 'database.txt'
students_list = [] 

print(''.center(line_width, fill_char))
print(' students manager '.upper().center(line_width, fill_char))
print(''.center(line_width, fill_char))

time.sleep(2)
with open(file_base_name, 'r', encoding='utf-8') as r_base_file:
    
    for line in r_base_file:
        in_student = line.split(';')
        del in_student[-1]
        students_list.append(in_student)
    print('<<ДАННЫЕ ЗАГРУЖЕНЫ УСПЕШНО>>'.center(line_width, fill_char))
                
time.sleep(2)
while True:
    print(' МЕНЮ '.center(line_width, '='))
    print('\t1. Добавить студента\n\t2. Удалить студента\n\t3. Обзор всех студентов\n\t4. Сохранить студентов \
в базу данных\n\t0. Выход')

    user_select = input('ВВОД>> ')

    if user_select == '0':
        print("ЗАВЕРШЕНИЕ РАБОТЫ...")
        for i in range(1, 101):
            sys.stderr.write(f'{i * "#"} {i} %\r')
            time.sleep(.05)
            
        print('\n<<РАБОТА ЗАВЕРШЕНА УСПЕШНО>>')
        exit()
    if user_select == '1':
        login = input('ВВЕДИТЕ ЛОГИН>> ')
        fio = input('ВВЕДИТЕ ПОЛНОЕ ИМЯ>> ')        
        while True:
            email = input('ВВЕДИТЕ ПОЧТУ>> ')
            print("ПРОВЕРКА ПОЧТЫ...")
            for i in range(1, 101):
                sys.stderr.write(f'{i * "#"} {i} %\r')
                time.sleep(.05)
            if "@" in email:
                print("\n<<ПОЧТА ПРАВИЛЬНА>>")
                break
            else:
                time.sleep(2)
                print("\n<<ПОЧТА НЕПРАВИЛЬНА>>")
                continue
        birth_date = input('ВВЕДИТЕ ВАШУ ДАТУ РОЖДЕНИЯ (дд.мм.гггг)>> ')
        new_student = [fio, birth_date, email, login]
        print("ДОБАВЛЕНИЕ СТУДЕНТА...")
        for i in range(1, 101):
            sys.stderr.write(f'{i * "#"} {i} %\r')
            time.sleep(.05)
        students_list.append(new_student)
        print("\n<<СТУДЕНТ ДОБАВЛЕН УСПЕШНО>>")
    
    if user_select == '2':
        del_index = int(input('Введите номер студента для удаления>> '))
        del_index = del_index - 1

        if del_index < 0 or del_index > len(students_list) - 1:
            print('<<НЕПРАВИЛЬНЫЙ НОМЕР>>')
            continue
        else:
            del students_list[del_index]
            for i in range(1, 101):
                sys.stderr.write(f'{i * "#"} {i} %\r')
                time.sleep(.05)
            print(f'\n<<СТУДЕНТ С НОМЕРОМ {del_index + 1} УСПЕШНО УДАЛЕН>>')

    if user_select == '3':
        counter = 1
        for student in students_list:
            print(f'\n{counter}.\tЛОГИН: {student[3]}\tПОЧТА: {student[2]}\tПОЛНОЕ ИМЯ: {student[0]}\tДАТА РОЖДЕНИЯ: {student[1]}')
            counter += 1
    
    if user_select == '4':
        with open(file_base_name, 'w', encoding='utf-8') as base_file:
            for i in range(1, 101):
                sys.stderr.write(f'{i * "#"} {i} %\r')
                time.sleep(.05)
            for student in students_list:
                for elem in student:
                    base_file.write(elem + ';')
                base_file.write('\n')
            print('\n<<СТУДЕНТЫ УСПЕШНО СОХРАНЕНЫ>>')