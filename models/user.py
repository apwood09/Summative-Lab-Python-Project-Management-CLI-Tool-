from .base import Person

class User(Person): 
    _id_counter = 1 # class attribute: auto-incrementing IDs

    def __init__(self, name, email=None, id=None, **kwargs):
        super().__init__(name)
        self.id = id or kwargs.get('id') or User._id_counter
        self.email = email or kwargs.get('_email')
        if not id and not kwargs.get('id'):
            User._id_counter += 1
    
    @property
    def email(self): 
        return self._email 

    @email.setter
    def email(self, value): 
        if "@" not in value:
            raise ValueError("Invalid email format")
        self._email = value

    def __repr__(self): 
        return f"User(id={self.id}, name='{self.name}')"