from sqlmodel import Field, SQLModel


class UserBase(SQLModel):
    name: str
    email: str


class User(UserBase, table=True):
    id: int | None = Field(primary_key=True)
    hashed_password: str
    test_field: str | None
