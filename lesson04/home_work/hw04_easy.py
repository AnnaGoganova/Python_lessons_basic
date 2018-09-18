# Все задачи текущего блока решите с помощью генераторов списков!

# Задание-1:
# Дан список, заполненный произвольными целыми числами. 
# Получить новый список, элементы которого будут
# квадратами элементов исходного списка
# [1, 2, 4, 0] --> [1, 4, 16, 0]
def make_square(iterable):
    return {x*x for x in iterable}

print(make_square(range(100)))


# Задание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.
def check_fruits(iterable1, iterable2):
    return {x for x in iterable1 if x in iterable2}

fruit_list_1 = ["apple", "limone", "plum", "peach"]
fruit_list_2 = ["banana", "plum", "cherry"]

print(check_fruits(fruit_list_1, fruit_list_2))


# Задание-3:
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4
def check_conditions(iterable):
    return {x for x in iterable if (x > 0 and x%3 == 0 and x%4 != 0)}

print(check_conditions(range(-20,100)))
