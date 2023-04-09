


global data, columns #список с данными, поля(колонки,слобцы)

columns = ('id','name','lastname','age','height','weight')
data = []    #Данные

def read(filename):
    with open(filename,'r')as file:
        for line in file:
            line = line.split(', ')
            line = (int(line[0]),line[1],line[2],int(line[3]),int(line[4]),int(line[5]))
            if line not in data:
                data.append(line)


def write(filename):
    with open(filename,'w')as file:
        for line in data:
            line.write(', '.join([str[i] for i in line])+'\n')


def add(line:str):
    line = line.split(', ')
    line = (int(line[0]), line[1], line[2], int(line[3]), int(line[4]), int(line[5]))
    if line not in data:
        data.append(line)


def remove(key,value):
    col = columns.index(key)
    row = -1
    for i in range(len(data)):
        if data[i][col] == value:
            row = i
            break
    if row -1:
        print('No matches found')
    else:
        data.pop(row)

def print_data():
    for line in data:
        print(', '.join([str[i]for i in line]))
read ('text.txt')
write('text.txt')
add('1 Ivan Ivanov')
remove(1,)
print_data()
'''
Задача создать базу данных учеников
line[1]
data = [(1,'Ivan','Ivanov'),(2,'Sasha','Sidorov')]

1)Список, в котором строки данных хранятся в виде кортежей
2)Переменные глобальные(чтобы они были доступны в функциях)
3) Создаем функции чтения из файла,записи в файл
4) Функци для добовления элемента (т.е кортежа) и после форматирования добовлять его в БД
5) Функция для удаление элемента по ключу(допустим, что элементы хрнаятся в виде ключ-значение)
6) Реализация функции, которая выведет данные на экран
Если ключа нет, то элемент не будет удален
OPEN-TO-WRITE
arr=[['a','b','c','d','e'],['1','2','3','4']]
with open('my_file.txt','w')as file:
    for i in arr:
        file.write(', '.join(i)+'\n')




with open('text.txt','r')as file:
    for line in file:
print(line.split('4',2))


Синтаксис .split и .join

Пример использования Join
btb=['bread', 'candy', 'lime']
print(':'.join(btb))


Пример split
with open('text.txt','r')as file:
   for line in file:
        print(line.split('4'))
'''