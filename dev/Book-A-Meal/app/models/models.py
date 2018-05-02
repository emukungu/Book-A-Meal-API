class User(object):
    def __init__(self, firstName=None, lastName=None, password = None):
        self._firstName = firstName
        self._lastName = lastName
        self._password = password
    
    def firstName(self):
        return self._firstName

    def lastName(self):
        return self._lastName
    
    def password(self):
        return self._password

class User_logged_in(object):
    def __init__(self, username=None, password = None):
        self._username = username
        self._password = password
    
    def username(self):
        return self._username

    def password(self):
        return self._password  


class Meals(object): #get all meals
    def __init__(self, meal_name = None, price = None,):
        self._meal_name = meal_name
        self._price = price
    
    
    def meal_name(self):
        return self._meal_name
    
    def price(self):
        return self._price
        

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

