class Point:
    x = 0
    y = 0
    def coordinates(self):
        print(f'Координаты: x {self.x}, y {self.y}','\n')

my_point = Point()
my_point.coordinates()
print('\n')

my_point.x = 10
my_point.y = -5

my_point.coordinates()
print('\n')

class toint:
    def __init__(sel, z, w):
        sel.z = z
        sel.w = w

    def coordinates(sel):
        print(f'Координаты: z {sel.z}, w {sel.w}')

my_toint = toint(15,10)
my_toint.coordinates()

print('\n')

class soint:
    def __init__(set, r, t):
        set.r = r
        set.t = t

    def coordinates(set):
        print(f'Координаты: r {set.r}, t {set.t}')

    def __repr__(set):
        return f'<Point r: {set.r}, t: {set.t}>'

my_soint = soint(100, 500)

print(my_soint,'\n')

# Инкапсуляция

# товар в магазине может быть классом

class Product:
    def __init__(self, name, price, stock, discount, max_discount=20):
        self.name = name.strip() # удаление пробелов в начале и конце
        if len(self.name) < 2:
            raise ValueError('Название не может быть таким коротким')
        self.price = abs(float(price))
        self.stock = abs(int(stock))
        self.discount = abs(float(discount))
        self.max_discount = abs(float(max_discount))
        if self.max_discount > 99:
            raise ValueError('Слишком большая скидка')
        if self.discount > self.max_discount:
            self.discount = self.max_discount

    def discounted(self):
        return self.price - (self.price * self.discount / 100)

    def sell(self, items_count = 1):
        if items_count > self.stock:
            raise ValueError('Недостаточно товара на складе')
            # Здесь мы можем как-то взаимодействовать с учетной/бухгалтерской системой
        self.stock -= items_count
    
    def get_color(self):
        raise NotImplementedError

    def __repr__(self):
        return f'<Product name: {self.name}, price: {self.price}, stock: {self.stock}>'

product1 = Product('Товар', 100, 4, 0)

product1.sell(3)

print(product1,'\n')

# Наследование

class Phone(Product):
    def __init__(self, name, price, color, stock=0, discount=0, max_discount=20.0):
        super().__init__(name, price, stock, discount, max_discount)
        self.color = color
    
    def get_color(self):
        return f'Цвет корпуса: {self.color}'

    def get_memory_size(self):
        # Выводим размер памяти
        pass
    
    def __repr__(self):
        return f'<Phone name: {self.name},price: {self.price},stock: {self.stock}>'

phone = Phone('iPhone Xs', 100000, 'черный', 10)
print(phone.get_color())
phone.sell(5)
print(phone,'\n')

# добавляем диван

class Sofa(Product):
    def __init__(self, name, price, color, material, stock=0, discount=0, max_discount=20.0):
        super().__init__(name, price, stock, discount, max_discount)
        self.color = color
        self.material = material
    
    def get_color(self):
        return f'Цвет обивки: {self.color}, тип ткани: {self.material}'
    
    def __repr__(self):
        return f'<Sofa name: {self.name},price: {self.price},stock: {self.stock}>'

sofa = Sofa('Облака', 50000, 'красный', 'синтетика', 3)
print(sofa.get_color())
sofa.sell(1)
print(sofa,'\n')






