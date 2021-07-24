
class StorageError(Exception):
    pass

class Storage():

    def __init__(self) -> None:
        self.products = []

    def _check_uniqu(self, articul):
        """Проверка на уикальность артикула продукта"""
        for product in self.products:
            if product.get('articul') == articul:
                raise StorageError('Артикул продукта должен быть уникальным')

    def set_product(self, product: 'Techman') -> None:
        """Добавление нового продукта"""
        self._check_uniqu(product.articul)

        self.products.append({
            'category':    product.category.lower(),
            'articul':     product.articul,
            'name':        product.name,
            'price':       product.price,
            'description': product.description,
            'quantity':    product.quantity,
        })

    def get_by_art(self, articul: str) -> dict or None:
        """Получение продукта по уникальному артиклу"""
        for product in self.products:
            if product.get('articul') == articul:
                return product

    def print_products_list(self) -> None:
        """Вывод на печать списка продуктов"""
        for product in self.products:
            print(product)

class TechmanError(Exception):
    pass

class Techman(Storage):

    def __init__(self, articul, name, price, description, quantity) -> None:
        self.articul     = articul
        self.name        = name
        self.price       = price
        self.description = description
        self.quantity    = quantity

        if self.check_num():
            raise TechmanError('Необходимо использовать числовые значения')

    def check_num(self) -> bool:
        """Проверка на соответствие числу int, float"""
        articul  = isinstance(self.articul, int)
        price    = isinstance(self.price, int) or isinstance(self.price, float) 
        quantity = isinstance(self.quantity, int)

        return not articul and price and quantity


class Printer(Techman):
    category = 'printers'


class Scanner(Techman):
    category = 'scaners'


class Copier(Techman):
    category = 'copiers'

def main():
    storage = Storage()

    product1 = {
        'articul': 1,
        'name': 'Название 1',
        'price': 100,
        'description': 'описание 1',
        'quantity': 10,
    }

    printer1 = Printer(**product1)

    storage.set_product(printer1)
    storage.set_product(Printer(2, 'Название 2', 200, 'описание 2', 20))

    storage.set_product(Scanner(3, 'Название 1', 300, 'описание 1', 30))
    storage.set_product(Scanner(4, 'Название 2', 400, 'описание 2', 40))

    storage.set_product(Copier(5, 'Название 1', 500, 'описание 1', 50))
    storage.set_product(Copier(6, 'Название 2', 600, 'описание 2', 60))

    product = storage.get_by_art(1)
    if product:
        print(product)
    else:
        storage.print_products_list()

if __name__ == '__main__':
    try:
        main()
    except StorageError as e:
        print(e)
    except TechmanError as e:
        print(e)
    except Exception as e:
        print(e)
