# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 23:58:42 2024

@author: aoalj
Python mini project on classes and methods
"""
class Menu:
  def __init__(self, name, items, start_time, end_time):
    self.name = name
    self.items = items
    self.start_time = start_time
    self.end_time = end_time
  def __repr__(self):
    return self.name + " between " + str(self.start_time) + " and " + str(self.end_time)
  def calculate_bill(self, purchased_items):
    total_bill = 0
    for item in purchased_items:
      if item in self.items:
        total_bill += self.items[item]
    return total_bill
class Franchise:
  def __init__(self, address, menus):
    self.address = address
    self.menus = menus

  def __repr__(self):
    return self.address

  def available_menus(self, hour):
    menu_names = []
    if 11 <= hour < 16:
        menu_names.append("brunch")
    if 15 <= hour < 18:
        menu_names.append("early_bird")
    if 17 <= hour < 23:
        menu_names.append("dinner")
    if 11 <= hour < 21:
        menu_names.append("kids")
    return menu_names or ["Sorry, no menu available at this time."]

class Business:
  def __init__(self, name, franchises):
    self.name = name
    self.franchises = franchises
  def __repr__(self):
    return self.name + str(self.franchises)

brunch = Menu("brunch", {'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50}, 11, 16)
print(brunch)

early_bird = Menu("early_bird", {'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00}, 15, 18)
print(early_bird)
dinner = Menu("dinner", {'crostini with eggplant caponata': 13.00, 'caesar salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00}, 17, 23)
print(dinner)
kids = Menu("kids", {'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00}, 11, 21)
print(kids)

arepas_menu = Menu("arepas_menue", {'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50}, 10, 200)
print(arepas_menu)

menus = [{'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50}, {'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00},
{'crostini with eggplant caponata': 13.00, 'caesar salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00},
{'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00}]
print(brunch.calculate_bill(['pancakes', 'coffee','home fries']))
print(early_bird.calculate_bill(['salumeria plate', 'mushroom ravioli (vegan)']))

flagship_store = Franchise("1232 West End Road", menus)
new_installment = Franchise("12 East Mulberry Street", menus)
arepas_place = Franchise("189 Fitzgerald Avenue", arepas_menu)

print(flagship_store.available_menus(17))

business1 = Business("Basta Fazoolin' with my Heart", [flagship_store, new_installment])
business2 = Business("Take a' Arepa", arepas_place)
print(business1)

