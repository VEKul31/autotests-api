from pydantic import BaseModel, Field, EmailStr
# Импортируем заранее созданный экземпляр класса Fake
from tools.fakers import fake

class UserSchema(BaseModel):
    """
    Описание структуры пользователя.
    """
    id: str
    email: EmailStr
    last_name: str = Field(alias="lastName")
    first_name: str = Field(alias="firstName")
    middle_name: str = Field(alias="middleName")


class CreateUserRequestSchema(BaseModel):
    """
    Описание структуры запроса на создание пользователя.
    """
    # Добавили генерацию случайного email
    email: EmailStr = Field(default_factory=fake.email)
    # Добавили генерацию случайного пароля
    password: str = Field(default_factory=fake.password)
    # Добавили генерацию случайной фамилии
    last_name: str = Field(alias="lastName", default_factory=fake.last_name)
    # Добавили генерацию случайного имени
    first_name: str = Field(alias="firstName", default_factory=fake.first_name)
    # Добавили генерацию случайного отчества
    middle_name: str = Field(alias="middleName", default_factory=fake.middle_name)


class CreateUserResponseSchema(BaseModel):
    """
    Описание структуры ответа создания пользователя.
    """
    user: UserSchema
