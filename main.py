    # 1
class Box:
    def __init__(self, cat=None):
        self.cat = cat
        self.nextcat = None

class LinkedList:
    def __init__(self):
        self.head = None

    def contains(self, cat):  # Проверка на кота в коробке, есть ли он
        lastbox = self.head
        while (lastbox):
            if cat == lastbox.cat:
                return True  # Нашли кота
            else:
                lastbox = lastbox.nextcat
        return False  # Не нашли кота в коробке

    # Добавляем в конец котика и коробку
    def addToEnd(self, newcat):
        newbox = Box(newcat)
        if self.head is None:  # Если нет первого элемента
            self.head = newbox
            return
        lastbox = self.head
        while (lastbox.nextcat):  # Двигаемся по списку
            lastbox = lastbox.nextcat
        lastbox.nextcat = newbox  # Ссылка на новый элемент в конце

    # Поиск по индексу кота
    def get(self, catIndex):
        lastbox = self.head
        boxIndex = 0
        while boxIndex <= catIndex:  # Пока не найдем нужный элемент
            if boxIndex == catIndex:  # Если нашли
                return lastbox.cat  # Сообщаяем, что нашли кота
            boxIndex = boxIndex + 1  # Не находим - двигаемся дальше
            lastbox = lastbox.nextcat  # Не находим - двигаемся дальше
        return False  # Сообщаем, что не нашли котика


    # Вывод котиков из коробок
    def printcat(self):
            headcat = self.head
            l = []
            l.append(headcat.cat)
            while headcat is not None:
                headcat.nextcat
                l.append(headcat.cat)
            print(l)

    # Выселяем котика из коробки
    def removeBox(self, rmcat):
        headcat = self.head
        if headcat is not None:  # Проверка на пустоту
            self.head = headcat.nextcat
            headcat = None
            return
        while headcat is not None:  # Двигаемся по списку коробок
            if headcat.cat == rmcat:
                break
            lastcat = headcat
            headcat = headcat.nextcat
        if headcat == None:  # Дошли до конца списка
            return
        lastcat.nextcat = headcat.nextcat  # передаем значение новой коробки
        headcat = None  # Текущую обнуляем

menu_choice = None
linkedlist = LinkedList()

while menu_choice != 0:
    print("Выберите действие:")
    print("1. Добавить элемент в список")
    print("2. Удалить элемент из списка")
    print("3. Показать содержимое списка")
    print("4. Проверить есть ли значение в списке")
    print("5. Заменить значение в списке")
    print("0. Выход")
    menu_choice = int(input("Введите номер пункта: "))

    if menu_choice == 1:
        cat = input("Введите имя кота: ")
        linkedlist.addToEnd(cat)
    elif menu_choice == 2:
        cat = input("Введите имя кота: ")
        if linkedlist.contains(cat):
            linkedlist.removeBox(cat)
            print(cat, "выселен из коробки")
        else:
            print(cat, "не найден в коробке")
    elif menu_choice == 3:
        linkedlist.printcat()
    elif menu_choice == 4:
        cat = input("Введите имя кота: ")
        if linkedlist.contains(cat):
            print(cat, "найден в коробке")
        else:
            print(cat, "не найден в коробке")
    elif menu_choice == 5:
        cat = input("Введите имя кота: ")
        newcat = input("Введите новое имя кота: ")
        if linkedlist.contains(cat):
            linkedlist.removeBox(cat)
            linkedlist.addToEnd(newcat)
            print(cat, "заменен на", newcat)
        else:
            print(cat, "не найден в коробке")
    elif menu_choice == 0:
        print("Выход")
    else:
        print("Такого пункта нет, выберите другое значение")

    # 2
class Box:      # двухсвязный список
    def __init__(self, cat = None):
        self.cat = cat
        self.nextcat = None
        self.prefcat = None

class DoubleLinkedList:
    def __init__(self):
        self.head = None
    def insert_in_emptyList(self, newcat):     # вставка в пустой список
        if self.head is None:                       # проверка на пустоту
            new_box = Box(newcat)
            self.head = new_box
        else:
            print("Список не пустой.")

    def insert_at_head(self, newcat):        # вставка котика в начало списка
        if self.head is None:                       # проверка на пустоту
            new_box = Box(newcat)
            self.head = new_box
            print("Котик встал в 1 коробоку")
            return
        new_box = Box(newcat)
        new_box.nextcat = self.head
        self.head.prefcat = new_box
        self.head = new_box

    def insert_at_end(self, newcat):        # вставка в конец
        if self.head is None:                       # проверка на пустоту
            new_box = Box(newcat)
            self.head = new_box
            print("Котик встал в 1 коробоку")
            return
        n = self.head
        while n.nextcat is not None:                # проход по всему списку
            n = n.nextcat
        new_box = Box(newcat)
        n.nextcat = new_box
        new_box.prefcat = n

    def delete_cat_at_start(self):          # удаление элементов с начала и до конца
        if self.head is None:                       # если список пуст
            print("Лист не содержит коробок с котиками")
            return
        if self.head.nextcat is None:             # если в списке 1 элемент
            self.head = None
        self.head = self.head.nextcat               # передвигаем голову
        self.prefcat = None                         # очищаем предыдущий

    def delete_cat_at_end(self):             # удаление элементов с конца и до начала
        if self.head is None:                       # если список пуст
            print("Лист не содержит коробок с котиками")
            return
        if self.head.nextcat is None:             # если в списке 1 элемент
            self.head = None
        n = self.head
        while n.nextcat is not None:
            n = n.nextcat
        n.prefcat.nextcat = None
        n.prefcat = None
    def Print_boxcat(self):                 # вывод котиков
        if self.head is None:                       # если список пуст
            print("Лист не содержит коробок с котиками")
            return
        else:
            n = self.head
            while n is not None:
                print(n.cat, " ")
                n = n.nextcat
    #     # Выселяем котика из коробки
    def removeBox(self, rmcat):
        headcat = self.head
        if headcat is not None:  # Проверка на пустоту
            self.head = headcat.nextcat
            headcat = None
            return
        while headcat is not None:  # Двигаемся по списку коробок
            if headcat.cat == rmcat:
                break
            lastcat = headcat
            headcat = headcat.nextcat
        if headcat == None:  # Дошли до конца списка
            return
        lastcat.nextcat = headcat.nextcat  # передаем значение новой коробки
        headcat = None  # Текущую обнуляем
    def contains(self, cat):  # Проверка на кота в коробке, есть ли он
        lastbox = self.head
        while (lastbox):
            if cat == lastbox.cat:
                return True  # Нашли кота
            else:
                lastbox = lastbox.nextcat
        return False  # Не нашли кота в коробке

double_linked_list = DoubleLinkedList()
while True:
    print("1. Добавить элемент в список.")
    print("2. Удалить элемент из списка (с начала).")
    print("3. Удалить элемент из списка (с конца).")
    print("4. Показать содержимое списка.")
    print("5. Проверить есть ли значение в списке.")
    print("6. Заменить значение в списке.")
    print("0. Выход.")
    choice = int(input("Введите ваш выбор: "))
    if choice == 0:
        break
    elif choice == 1:
        cat = input("Введите имя кота: ")
        double_linked_list.insert_at_end(cat)
        print("Кот успешно добавлен в коробку!")
    elif choice == 2:
        double_linked_list.delete_cat_at_start()
        print("Кот успешно удален из коробки!")
    elif choice == 3:
        double_linked_list.delete_cat_at_end()
        print("Кот успешно удален из коробки!")
    elif choice == 4:
        double_linked_list.Print_boxcat()
    elif choice == 5:
        cat = input("Введите имя кота, которого нужно найти: ")
        if double_linked_list.__contains__(cat):
            print("Кот с таким именем есть в коробке.")
        else:
            print("Кота с таким именем нет в коробке.")
    elif choice == 6:
        cat = input("Введите имя кота: ")
        newcat = input("Введите новое имя кота: ")
        if double_linked_list.contains(cat):
            double_linked_list.removeBox(cat)
            double_linked_list.insert_at_end(newcat)
            print(cat, "заменен на", newcat)
        else:
            print(cat, "не найден в коробке")
    else:
        print('Такого пункта нет, выберите другое значение.')



    # 3, 4
class StackCat: # работа со стеком
    def __init__(self):
        self.stackcat = []

    def pop(self):          # удаление
        if len(self.stackcat) == 0:                     # проверка на пустоту
            return f'В стеке нет элементов'
        removedcat = self.stackcat.pop
        return f'{removedcat} удален'


    def push(self, cat):         # добавление
        self.stackcat.append(cat)


    def pop_all(self):
        l = ""
        if len(self.stackcat) == 0:                     # проверка на пустоту
            return f'В стеке нет элементов'
        else:
            for i in range(len(self.stackcat)):
                removedcat = self.stackcat.pop()
                l += str(removedcat) + " "
        return f'Удалены элементы из стека: {l}'


stack = StackCat()
while True:
    print("Меню:")
    print("1. Помещение целого значения в стек;")
    print("2. Извлечь целое значение из стека;")
    print("4. Проверить пустой ли стек;")
    print("5. Проверить полный ли стек;")
    print("6. Очистить стек;")
    print("7. Получить верхнее значение без его выталкивания;")
    print("0. Выйти")
    choise = int(input("Выберите опцию: "))
    if choise == 0:
        break
    elif choise == 1:
        value = int(input("Введите целое значение для добавления в стек: "))
        stack.push(value)
        print(f"Значение {value} добавлено в стек")
    elif choise == 2:
        value = stack.pop()
        print(value)
    elif choise == 3:
        count = len(stack.stackcat)
        print(f"Количество целых чисел в стеке: {count}")
    elif choise == 4:
        if len(stack.stackcat) == 0:
            print("Стек пустой")
        else:
            print("Стек не пустой")
    elif choise == 5:
        if len(stack.stackcat) == 10:
            print("Стек полный")
        else:
            print("Стек не полный")
    elif choise == 6:
        stack.stackcat.clear()
        print("Стек очищен")
    elif choise == 7:
        if len(stack.stackcat) == 0:
            print("Стек пустой")
        else:
            top_value = stack.stackcat[-1]
            print(f"Верхнее значение стека: {top_value}")
    elif choise == 0:
        break
    else:
        print('Такого пункта нет, выберите другое значение.')





