class User(object):
    def __init__(self, user_id = None, firstName=None, lastName=None, password = None, username = None):
        self._user_id = user_id
        self._firstName = firstName
        self._lastName = lastName
        self._password = password
        self._username = username
    
    def firstName(self):
        return self._firstName

    def lastName(self):
        return self._lastName
    
    def password(self):
        return self._password

    def __id__(self):
        return self._user_id

    def username(self):
        return self._username

class Meals(object): #get all meals
    def __init__(self, meal_name = None, price = None):
        self._meal_name = meal_name
        self._price = price
        self._meal_id = 0
    
    
    def meal_name(self):
        return self._meal_name
    
    def price(self):
        return self._price

    def meal_id(self):
        return self._meal_id
        

class Menu(object):
    def __init__(self, menu_title=None, menu_items=[]):
        self._menu_title = menu_title
        self._menu_items = menu_items

    def menu(self): #structure in which data is stored
        return {
            "name": self._menu_title,
            "items": self._menu_items
        }

class Orders(object):
    def __init__(self, items = []):
        self._items = items
        self._total = 0.0

    def orders(self):
        return self._items
    
    def total(self):
        return self._total

