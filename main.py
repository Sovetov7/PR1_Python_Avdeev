print("Введите сколько строк данных вы хотите записать в файл")
count = int(input())
i=0;
def isint(m):
    try:
        int(m)
        return True
    except ValueError:
        return False
while (i<count):
    i+=1
    if (i != 1):
        print("Введите данные снова")
    else:
        print("Введите фамилию, имя, отчество и год рождения")
    try:
        lastname, name, patronymic, year = (i for i in input().split(' '))
        file = open('data.txt', 'a', encoding='utf8')
        try:
            if ((lastname.isalpha() or name.isalpha() or patronymic.isalpha() or lastname == '-' or name == '-' or patronymic == '-') == False):
                print('Корректно введите данные, для правильной работы')
                i-=1
            elif isint(year) and len(year) == 4:
                file.write(str(lastname) + ' ' + str(name) + ' ' + str(patronymic) + ' ' + str(year) + ' ' + '\n')
            else:
                print('Год рождения должен состоять из четырех цифр')
        except ValueError:
            print('Корректно введите данные, для правильной работы')
        finally:
            file.close()
    except:
        print('Произошла ошибка при открытии файла')
print('\n' + 'Фамилия ' + ' Имя ' + ' Отчество ' + ' Год рождения ' + '\n')
import time

try:
    file = open('data.txt', 'r', encoding='utf8')
    while True:
        time.sleep(1)
        line = file.readline()
        if not line:
            break
        print(str(line))
except:
    print('Произошла ошибка при открытии файла')
finally:
    file.close()

