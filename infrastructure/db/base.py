from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    def __repr__(self):
        cols = []
        for col in self.__tablename__.columns:
            cols.append(f"{col} = {getattr(self, col)}")
        return f"<{self.__class__.__name__}. {cols}>"