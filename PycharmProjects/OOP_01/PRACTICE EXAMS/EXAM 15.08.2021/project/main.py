from project.bakery import Bakery

bakery = Bakery('Хлебарница')
print(bakery.add_food('Cake', 'CarrotCakes', 3.4))
print(bakery.add_food('Bread', 'BananaBread', 2.5))
print(bakery.add_food('Cake', 'ChocolateCakes', 4))
print(bakery.add_drink('Water', 'Mineral Water', 300.0, "Bankia"))
print(bakery.add_drink('Water', 'Soda', 330.0, "Coca Cola"))
print(bakery.add_drink('Tea', 'Gorski', 250.0, "BG"))
print(bakery.add_table('OutsideTable', 55, 15))
print(bakery.add_table('OutsideTable', 56, 10))
print(bakery.reserve_table(11))
print(bakery.order_food(55, 'CarrotCakes', "BananaBread", 'ChocolateCakes', 'RicePudding', "Pancakes"))
print(bakery.order_drinks(55, 'Mineral Water', 'Gorski', 'Soda', "BB"))
print(bakery.leave_table(55))
print(bakery.get_free_tables_info())
print(bakery.get_total_income())



