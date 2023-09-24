from pydantic import BaseModel, EmailStr, ValidationError
#defining class Models
class User(BaseModel):
    username: str
    email: EmailStr
    age: int

# Creating a User instance and validating data
user_data = {
    "username": "johndoe",
    "email": "johndoe@example.com",
    "age": 30,
}

user = User(**user_data)
print(user)

#Validations, here email should have been a Email String defined in class User
try:
    invalid_data = {"username": "johndoe", "email": "invalid_email", "age": "30"}
    user = User(**invalid_data)
except ValidationError as e:
    print(e)


# Parsing JSON data into a Pydantic model
json_data = '{"username": "johndoe", "email": "johndoe@example.com", "age": 30}'
user = User.parse_raw(json_data)
print(user)

# Serializing a Pydantic model to JSON
user_dict = user.dict()
print(user_dict)
