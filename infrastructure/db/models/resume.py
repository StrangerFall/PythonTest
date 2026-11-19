import datetime
import decimal
from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.infrastructure.db.base import Base
if TYPE_CHECKING:
    from src.infrastructure.db.models.worker import WorkerOrm


class ResumesOrm(Base):
    __tablename__ = 'resumes'

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str]
    workload: Mapped[str]
    worker_id: Mapped[int] = mapped_column(ForeignKey('workers.id',ondelete='CASCADE'))
    compensation: Mapped[decimal.Decimal]
    hire_date: Mapped[datetime.datetime]

    worker: Mapped["WorkerOrm"] = relationship(
        back_populates="resumes"
    )