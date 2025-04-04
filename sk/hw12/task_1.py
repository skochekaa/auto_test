# Создать классы цветов: общий класс для всех цветов и классы для нескольких видов.
class Flower:
    def __init__(self, name_flower, freshness, color, stem_length, price, life_time):
        self.name_flower = name_flower
        self.freshness = freshness
        self.color = color
        self.stem_length = stem_length
        self.price = price
        self.life_time = life_time


# Собрать букет (букет - еще один класс) с определением его стоимости
class Bunch:
    def __init__(self, list_flowers: list):
        self.list_flowers = list_flowers

    def get_price(self):
        price = 0
        for flower in self.list_flowers:
            price += flower.price
        return price

    # Для букета создать метод, который определяет время его увядания
    # по среднему времени жизни всех цветов в букете.
    def bunch_life_time(self):
        life_time_list = [price.life_time for price in self.list_flowers]
        return round(sum(life_time_list) / len(life_time_list), 2)

    # Позволить сортировку цветов в букете на основе различных параметров
    # (свежесть/цвет/длина стебля/стоимость)(это тоже методы)
    def sort(self, order_by: str):
        if order_by == "Свежесть":
            return sorted([value.freshness for value in self.list_flowers])
        elif order_by == "Цвет":
            return sorted([value.color for value in self.list_flowers])
        elif order_by == "Длина":
            return sorted([value.stem_length for value in self.list_flowers])
        elif order_by == "Цена":
            return sorted([value.price for value in self.list_flowers])

    # Реализовать поиск цветов в букете по каким-нибудь параметрам
    # (например, по среднему времени жизни) (и это тоже метод).
    def search(self, life_time: int):
        for flower in self.list_flowers:
            if life_time == 5:
                return f"Цветок: {flower.name_flower}, время жизни: {flower.life_time}"
            elif life_time == 7:
                return f"Цветок: {flower.name_flower}, время жизни: {flower.life_time}"
            elif life_time == 10:
                return f"Цветок: {flower.name_flower}, время жизни: {flower.life_time}"
            else:
                return "Нет цветка с таким временем жизни"


# Создать экземпляры (объекты) цветов разных видов.
rose = Flower("Роза", 1, "Красный", 80, 100, 7)
tulpan = Flower("Тюльпан", 2, "Белый", 70, 90, 5)
orchidea = Flower("Орхидея", 3, "Белый", 50, 85, 10)

# В букете цветы пусть хранятся в списке. Это будет список объектов.
my_bunch = Bunch([rose, tulpan, orchidea])

print(my_bunch.get_price())
print(my_bunch.bunch_life_time())
print(my_bunch.sort("Свежесть"))
print(my_bunch.sort("Цвет"))
print(my_bunch.sort("Длина"))
print(my_bunch.sort("Цена"))
print(my_bunch.search(5))
