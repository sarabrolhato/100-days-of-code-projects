### Day 17 - The Quiz Project and the Benefits of OPP
- Day 16 Project: Geography Quiz using the Open Trivia Database API

### Day 17 Resources
- [Open Trivia Database](https://opentdb.com/)

### Working with Attributes, Class Constructors and the __init__() Function

```
class User:
    def __init__(self):
        print("New user being created...") # This will be run every time a new object is created

user_1 = User()
```

#### Creating class attributes for an object

```
user_1.id = "001"
user_1.username = "angela"
print(user_1.username)

user_2 = User()
user_2.id = "002"
user_2.username = "bob"
```

Tip: If you declase a class or a function and do not write anything indented in the content, python will show an error. To prevent this error when you don't want to write anything for now, you can use the "pass" keyword.

```
def function():
    pass
```

When we create a class, we write it using the Pascal Case.

Case types:
- PascalCase (for classes).
- camelCase
- snake_case (for functions).

#### Initializing a class: set the starting values

```
class Car:
    def __init__(self, seats):
     # initialize attributes
    self.seats = seats
```
Because creating new attributes every time an object is created is a lot of work and prone to errors, we can specify them at the time of creation.

```
class UserNew:
    def __init__(self, user_id, username):
        #print("New user being created...") # This will be run every time a new object is created
        self.id = user_id
        self.username = username
        self.followers = 0

user_3 = UserNew("007", "Sara")
print(user_3.username)
print(user_3.id)
```

You can also set an attribute to a value without having to specify it when creating an object.
```
user_3 = UserNew("007", "Sara")
print(user_3.followers)
```

#### Adding Methods to a Class

```
class Car:

    def __init__(self, seats):
    # initialize attributes
        self.seats = seats

    def enter_race_mode(self):
        self.seats = 2

volvo = Car("5")
print(volvo.seats)
volvo.enter_race_mode()
print(volvo.seats)
```
```
class UserInstagram:

    def __init__(self, user_id, username):
        #print("New user being created...") # This will be run every time a new object is created
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1

user_4 = UserInstagram("004", "angela123")
user_5 = UserInstagram("005", "jackbauer")

user_4.follow(user_5)

print(user_4.followers)
print(user_4.following)
print(user_5.followers)
print(user_5.following)
```