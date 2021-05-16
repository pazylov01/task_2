class Factory:
    money = 0
    def __init__(self, name, lastname, id):
        self.name = name
        self.lastname = lastname
        self.id = id
    
    def info(self):
        print(f"Имя - {self.name} {self.lastname}, ID - {self.id}")
    
    def salary(self,fixed_salary, hours):
        self.hours = hours
        self.fixed_salary = fixed_salary
        print(f'Зарплата – {self.fixed_salary}\nКоличество проработанных часов за последнюю неделю - {self.hours} часов')
        Factory.money += self.fixed_salary
    
    def salary_1(self, salary_2, sales, hours_2, komissiya=50):
        self.salary_2 = salary_2
        self.sales = sales
        self.hours_2 = hours_2
        self.salary_2 = self.salary_2 + (komissiya * self.sales)
        print(f'Фиксированная зарплата – {self.salary_2}, Кол-во произведенных продаж – {self.sales}\nКоличество проработанных часов за последнюю неделю - {self.hours_2} часов') 
        Factory.money += self.salary_2
    
    def salary_2(self, hour_work, hours=100):
        self.hour_work = hour_work
        hour_work = self.hour_work * hours
        print(f'Количество проработанных часов за последнюю неделю: {self.hour_work}\nПочасовой оклад {hour_work}')
        Factory.money += hour_work
    
    def howMany():
        print(f'{ Factory.money} придётся потратить компании.')


class Manager(Factory):
    def __init__(self, name, lastname, id):
        super().__init__(name, lastname, id)

class Secretary(Factory):
    def __init__(self, name, lastname, id):
        super().__init__(name, lastname, id)

    def salary(self, fixed_salary, hours):
        self.hours = hours
        self.fixed_salary = fixed_salary
        print(f'Зарплата – {self.fixed_salary}\nКоличество проработанных часов за последнюю неделю - {self.hours} часов')
        Factory.money += self.fixed_salary

class Seller(Factory):
    def __init__(self, name, lastname, id):
        super().__init__(name, lastname, id)

class Worker(Factory):
    def __init__(self, name, lastname, id):
        super().__init__(name, lastname, id)

print('Менеджер:')
manager = Manager("Барсбек", "Канаткулов", 1)
manager.info()
manager.salary(45000, 18)
print('Секретарь:')
secretary = Secretary('Алымкул', 'Тилекбаев', 2)
secretary.info()
secretary.salary(45000, 38)
print("Продавец:")
seller = Seller('Айпери', 'Шалымбекова', 3)
seller.info()
seller.salary_1(20000, 20, 38)
print('Два работника цеха:')
worker = Worker('Бакыт', 'Рустамов', 4)
worker.info()
worker.salary_2(25)
worker = Worker('Алтынай', 'Ширинбаева', 5)
worker.info()
worker.salary_2(40)
print('Секретарь на замену:')
worker = Worker('Жанар', 'Рыскулов', 6)
worker.info()
worker.salary_2(33)
print('Трата компании:')
Factory.howMany()



