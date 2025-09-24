from sqlmodel import Field, SQLModel


class Note(SQLModel, table=True):
    id: int | None = Field(primary_key=True)
    title: str
    content: str
    content: str
