import re

# Книга
class Book:
    def __init__(self, id, name, author, price, shop_id):
        self.id = id
        self.name = name
        self.author = author
        self.price = price
        self.shop_id = shop_id

# Книжный магазин
class Shop:
    def __init__(self, id, name):
        self.id = id
        self.name = name

# Cвязь многие ко многим
class ShopBook:
    def __init__(self, shop_id, book_id):
        self.shop_id = shop_id
        self.book_id = book_id

# Магазины
shops = [
    Shop(1, 'Лабиринт'),
    Shop(2, 'Переплет'),
    Shop(3, 'Читай-город'),
    Shop(4, 'Чайка'),
    Shop(5, 'Азбука'),
    Shop(6, 'Перемена'),
    Shop(7, 'Многобукаф'),
    Shop(8, 'Мастер'),
    Shop(9, 'Прогресс'),
    Shop(10, 'Карандаш'),
]

# Книги
books = [
	Book(1, 'Заклинание', 'Иванов', 1209, 2),
	Book(2, 'Тайник', 'Смирнов', 1055, 3),
	Book(3, 'Одиссея', 'Кузнецов', 1099, 4),
	Book(4, 'Страсть', 'Попов', 299, 5),
	Book(5, 'Расследование', 'Васильев', 2509, 6),
	Book(6, 'Ад', 'Петров', 1055, 7),
	Book(7, 'Эльфы', 'Соколов', 1275, 8),
	Book(8, 'Трагедия', 'Михайлов', 425, 9),
	Book(9, 'Империя', 'Новиков', 1395, 10),
	Book(10, 'Гипотеза', 'Федоров', 1880, 1),
	Book(11, 'Мудрость', 'Морозов', 1039, 2),
	Book(12, 'Смех', 'Волков', 409, 3),
	Book(13, 'Катастрофа', 'Алексеев', 1150, 4),
	Book(14, 'Загадка', 'Лебедев', 425, 5),
	Book(15, 'Вера', 'Семенов', 575, 6),
	Book(16, 'Путешественник', 'Егоров', 1465, 7),
	Book(17, 'Страсть', 'Павлов', 1795, 8),
	Book(18, 'Кровь', 'Козлов', 2069, 9),
	Book(19, 'Биография', 'Степанов', 260, 10),
	Book(20, 'Фейри', 'Николаев', 400, 1),
	Book(21, 'Легенды', 'Орлов', 1310, 2),
	Book(22, 'Хроники', 'Андреев', 1039, 3),
	Book(23, 'Мелодия', 'Макаров', 1585, 4),
	Book(24, 'Чудо', 'Никитин', 1110, 5),
	Book(25, 'Напряжение', 'Захаров', 1069, 6),
	Book(26, 'Ужас', 'Зайцев', 2560, 7),
	Book(27, 'История', 'Соловьев', 555, 8),
	Book(28, 'Эпос', 'Борисов', 1010, 9),
	Book(29, 'Битва', 'Яковлев', 710, 10),
	Book(30, 'Поиск', 'Григорьев', 1940, 1),
]

# Связь многие-ко-многим
shops_books = [
    ShopBook(2, 1),
	ShopBook(3, 2),
	ShopBook(4, 3),
	ShopBook(5, 4),
	ShopBook(6, 5),
	ShopBook(7, 6),
	ShopBook(8, 7),
	ShopBook(9, 8),
	ShopBook(10, 9),
	ShopBook(1, 10),
	ShopBook(2, 11),
	ShopBook(3, 12),
	ShopBook(4, 13),
	ShopBook(5, 14),
	ShopBook(6, 15),
	ShopBook(7, 16),
	ShopBook(8, 17),
	ShopBook(9, 18),
	ShopBook(10, 19),
	ShopBook(1, 20),
	ShopBook(2, 21),
	ShopBook(3, 22),
	ShopBook(4, 23),
	ShopBook(5, 24),
	ShopBook(6, 25),
	ShopBook(7, 26),
	ShopBook(8, 27),
	ShopBook(9, 28),
	ShopBook(10, 29),
	ShopBook(1, 30),
]
def main():
    # Соединение данных один-ко-многим
    one_to_many = [(b.name, b.author, b.price, s.name)
                   for s in shops
                   for b in books
                   if b.shop_id == s.id]

    # Соединение данных многие-ко-многим
    many_to_many_temp = [(s.name, sb.shop_id, sb.book_id)
                         for s in shops
                         for sb in shops_books
                         if s.id == sb.shop_id]

    many_to_many = [(b.name, b.price, shop_name)
                    for shop_name, shop_id, book_id in many_to_many_temp
                    for b in books if b.id == book_id]

	# Список всех книг, фамилия автора которых заканчивается на "ев" и их магазины
    print('Задание Д1')
    res_11 = []
    for book_name, book_author, book_price, shop_name in one_to_many:
        flag = re.findall(r'\b\w+ев\b', book_author)
        if flag:
            res_11.append((book_name, book_author, shop_name))
    print(res_11)

	# Средняя цена книги в магазине
    print('\nЗадание Д2')
    res_12 = {}
    for shop in shops:
        l_books = list(filter(lambda i: i[3] == shop.name, one_to_many))
        if len(l_books) > 0:
            s_prices = [book[2] for book in l_books]
            res_12[shop.name] = int(sum(s_prices)/len(s_prices))
    print(sorted(res_12.items(), key=lambda item: item[1]))

	# Список всех магазинов, у которых название начинается с буквы «П», и список книг в них
    print('\nЗадание Д3')
    res_13 = {}
    for shop in shops:
        if shop.name[0] == 'П':
            l_books = list(filter(lambda i: i[2] == shop.name, many_to_many))
            l_books_names = [x for x, _, _ in l_books]
            res_13[shop.name] = l_books_names
    print(res_13)
    
if __name__ == '__main__':
    main()