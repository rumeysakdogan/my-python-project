"""
Classes
- class is like an object constructor
- all classes have a __init__() function
- __init__() is executed automatically, whenever we create the objects from the class
"self" Parameter
- self is a reference to the current instance of the class
- is used to access variables that belong to the class
Methods
- Functions that belong to an object are called methods.
"""

class User:
    def __init__(self, user_email, name, password, current_job_title):
        self.email = user_email
        self.name = name
        self.password = password
        self.current_job_title = current_job_title

    def change_password(self, new_password):
        self.password = new_password

    def change_job_title(self, new_job_title):
        self.current_job_title = new_job_title

    def get_user_info(self):
       print(f"User {self.name} currently works as a {self.current_job_title}. You can contact them at {self.email}")


