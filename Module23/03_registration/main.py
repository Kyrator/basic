# TODO здесь писать код
line = list()
error_list = list()
right_list = list()

with open('registrations.txt', 'r') as registrations:
    for i_line in registrations:
        try:
            line = i_line.split()
            if len(line) < 3:
                raise IndexError
            name, email, age = line
            if not name.isalpha():
                raise NameError
            if not ('@' in email and '.' in email):
                raise SyntaxError
            if 10 > int(age) > 100:
                raise ValueError
            right_list.append(f"{name} {email} {age}")
        except IndexError:
            error_list.append("{name} {email} {age}\t\tНЕ присутствуют все три поля"
                              .format(name=name, email=email, age=age))
        except NameError:
            error_list.append("{name} {email} {age}\t\tПоле «Имя» содержит НЕ только буквы:"
                              .format(name=name, email=email, age=age))
        except SyntaxError:
            error_list.append("{name} {email} {age}\t\tПоле «Имейл» НЕ содержит @ и . (точку): "
                              .format(name=name, email=email, age=age))
        except ValueError:
            error_list.append('{name} {email} {age}\t\tПоле «Возраст» НЕ является числом от 10 до 99'
                              .format(name=name, email=email, age=age))

with open('registrations_good.log', 'w') as registrations_good:
    for i_right_list in right_list:
        registrations_good.write(str(i_right_list) + '\n')

with open('registrations_bad.log', 'w') as registrations_bad:
    for i_error_list in error_list:
        registrations_bad.write(str(i_error_list) + '\n')

with open('registrations_bad.log', 'w') as registrations_bad:
    print("Содержимое файла registrations_bad.log:")
    for i_error_list in error_list:
        print(i_error_list)
print()
with open('registrations_good.log', 'w') as registrations_good:
    print("Содержимое файла registrations_good.log:")
    for i_right_list in right_list:
       print(i_right_list)


