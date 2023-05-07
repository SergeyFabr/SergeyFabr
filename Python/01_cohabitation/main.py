import random


class Home:
    """
    Базовый класс описывает дом.
    Args:
        meal (int): Значение еды, изначально = 50
        money (int): Значение денег, изначально = 100
        meal_cat (int): Значение еды кота, изначально = 30
        dirt (int): Значение грязи в доме, изначально = 0
    Methods:
        Геттеры:
            get_meal():
            get_meal_cat():
            get_money():
            get_dirt():
        Сеттары:
            set_meal():
            set_meal_cat():
            set_dirt():
            set_money():

        info(): Информация о показателях дома
    """
    def __init__(self, meal=30, money=100, meal_cat=30, dirt=0):
        self.__meal = meal
        self.__money = money
        self.__meal_cat = meal_cat
        self.__dirt = dirt

    def get_meal(self):
        return self.__meal

    def get_meal_cat(self):
        return self.__meal_cat

    def get_money(self):
        return self.__money

    def get_dirt(self):
        return self.__dirt

    def set_meal(self, quantity):
        if quantity == 0:
            self.__meal = 0
        else:
            self.__meal += quantity

    def set_meal_cat(self, quantity):
        if quantity == 0:
            self.__meal_cat = 0
        else:
            self.__meal_cat += quantity

    def set_dirt(self, quantity):
        if quantity == 0:
            self.__dirt = 0
        else:
            self.__dirt += quantity

    def set_money(self, quantity):
        self.__money += quantity

    def info(self):
        print('\nДанные по ресурсам семьи:'
              '\nЕда - {}'
              '\nДеньги - {}'
              '\nЕда кота - {}'
              '\nПоказатель грязи - {}'.format(self.__meal, self.__money, self.__meal_cat, self.__dirt))


class Person:
    """
    Базовый класс описывает человека.
    Args:
        name (str): Имя человека
        home (int): Экземпляр класса Home
        satiety (int): Значение сытости, изначально = 30
        happy (int): Значение счастья, изначально = 100
    Methods:
        Геттеры:
            get_name()
            get_satiety()
            get_happy()
        Сеттары:
            set_satiety()
            set_happy()
        petting_cat(): Реализует возможность гладить кота
        eat(): Реализует прием пищи человеком
        info_human(): выводит информацию о человеке
    """
    def __init__(self, name, home=None, satiety=30, happy=100):
        self.__name = name
        self.home = home
        self.__satiety = satiety
        self.__happy = happy

    def get_name(self):
        return self.__name

    def get_satiety(self):
        return self.__satiety

    def get_happy(self):
        return self.__happy

    def set_satiety(self, quantity):
        if self.__satiety + quantity > 0:
            self.__satiety += quantity
        else:
            self.__satiety = 0

    def set_happy(self, quantity):
        if self.__happy + quantity > 0:
            self.__happy += quantity
        else:
            self.__happy = 0

    def petting_cat(self):
        if self.__satiety - 10 > 0:
            self.__satiety -= 10
            self.__happy += 5
        else:
            self.__satiety -= self.__satiety

    def eat(self):
        quantity_eat = random.randint(10, 30)
        if self.home.get_meal() - quantity_eat >= 0:
            self.__satiety += quantity_eat
            self.home.set_meal(-quantity_eat)
        else:
            self.__satiety += self.home.get_meal()
            self.home.set_meal(0)

    def info_human(self):
        print('\nПоказатели, {}:'
              '\nСытость - {}'
              '\nСчастье - {}'.format(self.__name, self.__satiety, self.__happy))


class Husband(Person):
    """
    Производный класс от Person описывает мужа.
    Methods:
        play(): Муж играет
        work(): Поход на работу
    """

    def play(self):
        self.set_satiety(-10)
        self.set_happy(20)

    def work(self):
        self.set_satiety(-10)
        self.home.set_money(150)


class Wife(Person):
    """
    Производный класс от Person описывает жену.
    Methods:
        buy_food(self): Покупка еды в дом
        buy_coat(self): Покупка шубы
        cleaning(self): Уборка в доме
    """

    def buy_food(self):
        quantity = random.randint(20, 80)
        self.set_satiety(-10)
        if self.home.get_money() - quantity >= 0:
            self.home.set_money(-quantity)
            self.home.set_meal_cat(quantity // 2)
            self.home.set_meal(quantity // 2)
        else:
            self.home.set_money(-self.home.get_money())
            self.home.set_meal_cat(self.home.get_money() // 2)
            self.home.set_meal(self.home.get_money() // 2)

    def buy_coat(self):
        self.home.set_money(-350)
        self.set_happy(60)
        self.set_satiety(-10)

    def cleaning(self):
        clean_dirt = random.randint(-100, -10)
        self.set_satiety(-10)
        if self.home.get_dirt() + clean_dirt >= 0:
            self.home.set_dirt(clean_dirt)
        else:
            self.home.set_dirt(0)


class Cat:
    """
    Базовый класс описывает кота.
    Args:
        name (str): кличка кота
        home (int): Экземпляр класса Home
        satiety (int): Значение сытости, изначально = 30

    """

    def __init__(self, name, home=None, satiety=30):
        self.__name = name
        self.__satiety = satiety
        self.home = home

    def eat(self):
        quantity_eat = random.randint(2, 10)
        if self.home.get_meal_cat() == 0:
            self.__satiety = 0
        elif self.home.get_meal_cat() - quantity_eat < 0:
            self.__satiety += (self.home.get_meal_cat() * 2)
            self.home.set_meal_cat(0)
        else:
            self.__satiety += (quantity_eat * 2)
            self.home.set_meal_cat(-quantity_eat)

    def get_satiety(self):
        return self.__satiety

    def sleep(self):
        self.__satiety -= 10

    def tear_wallpaper(self):
        self.__satiety -= 10
        self.home.set_dirt(5)

    def info_cat(self):
        print('\nПоказатели, {}:'
              '\nСытость - {}'.format(self.__name, self.__satiety))


def one_day_husband():
    """
    Функции описывающие один день мужа
    """
    if husband.get_satiety() < 10:
        if my_home.get_meal() == 0 and wife.get_satiety():
            husband.play()
        else:
            husband.eat()
    elif husband.home.get_money() < 50:
        husband.work()
    elif husband.get_happy() < 20:
        husband.play()
    else:
        husband.petting_cat()


def one_day_wife():
    """
    Функции описывающие один день жены
    """
    if wife.get_satiety() <= 10:
        if my_home.get_money() > 0:
            wife.eat()
        else:
            wife.petting_cat()
    elif my_home.get_meal() < 40 or my_home.get_meal_cat() < 20:
        wife.buy_food()
    elif wife.get_happy() < 20 or my_home.get_money() > 2000:
        if my_home.get_money() > 350:
            wife.buy_coat()
        else:
            wife.petting_cat()
    else:
        wife.cleaning()


def one_day_cat():
    """
    Функции описывающие один день мужа
    """
    if cat.get_satiety() > 0:
        if cat.get_satiety() < 10:
            cat.eat()
        elif random.randint(1, 6) == 3:
            cat.tear_wallpaper()
        else:
            cat.sleep()


my_home = Home()
husband = Husband('Ivan', my_home)
wife = Wife('Maria', my_home)
cat = Cat('Barsik', my_home)

for day in range(1, 366):
    my_home.set_dirt(5)
    if my_home.get_dirt() > 90:
        husband.set_happy(-10)
        wife.set_happy(-10)

    one_day_husband()
    one_day_wife()
    one_day_cat()

    if (husband.get_satiety() == 0 or husband.get_happy() <= 10) \
            and (wife.get_happy() <= 10 or wife.get_satiety() <= 0) \
            and (cat.get_satiety() <= 0):
        print(f'Эксперемент прерван на {day} день! все умерли.\n')
        break

print('Итоги:')
husband.info_human()
wife.info_human()
cat.info_cat()
cat.home.info()

