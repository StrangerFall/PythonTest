import datetime
import decimal

from pydantic import BaseModel


class WorkerSchema(BaseModel):
    username: str
    department: str
    salary: decimal.Decimal
    hire_date: datetime.date