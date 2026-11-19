from sqlalchemy import select

from src.domain.interfaces.IWorkersRepository import IWorkersRepository
from src.infrastructure.db.database import SessionDep
from src.infrastructure.db.models.worker import WorkerOrm


class WorkerRepository(IWorkersRepository):
    def __init__(self, session: SessionDep):
        self.session = session
    async def get_worker_by_id_async(self, worker_id: int):
        query = (
            select(WorkerOrm)
            .where(WorkerOrm.id == worker_id)
        )
        result = await self.session.execute(query)
        return result.scalars().first()

    async def get_all_workers(self):
        query = (
            select(WorkerOrm)
        )
        result = await self.session.execute(query)
        return result.scalars().all()

    async def add_workers(self,workers: dict):
        workers = WorkerOrm(**workers)
        self.session.add(workers)
        await self.session.commit()

