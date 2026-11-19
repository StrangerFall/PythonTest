import datetime
import decimal
from typing import TYPE_CHECKING

from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.infrastructure.db.base import Base
if TYPE_CHECKING:
    from src.infrastructure.db.models.resume import ResumesOrm


class WorkerOrm(Base):
    __tablename__ = 'workers'

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str]
    department: Mapped[str]
    salary: Mapped[decimal.Decimal]
    hire_date: Mapped[datetime.date]

    resumes: Mapped[list["ResumesOrm"]] = relationship(
        back_populates="worker"
    )