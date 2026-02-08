class InvalidAgeError(Exception):
    pass

try:
    age = int(input("Enter age: "))
    if age < 18:
        raise InvalidAgeError("Age must be 18 or older!")
except InvalidAgeError as e:
    print(f"Error: {e}")
