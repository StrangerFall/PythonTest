from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException

from src.infrastructure.db.models import WorkerOrm
from src.infrastructure.db.repositories.WorkersRepository import WorkerRepository
from src.infrastructure.db.schemas.WorkerShema import WorkerSchema

router = APIRouter(prefix="/workers", tags=["Workers"])

WorkerRepoDep = Annotated[WorkerRepository, Depends()]

@router.get("/{worker_id}", summary="Получение работника по индентификатору")
async def get_worker_by_id(worker_id: int,repo: WorkerRepoDep):
    worker = await repo.get_worker_by_id_async(worker_id)
    if not worker:
        raise HTTPException(status_code=404, detail="Worker not found")
    return worker


@router.get("", summary="Получение работников")
async def get_workers(repo: WorkerRepoDep):
    worker = await repo.get_all_workers()
    if not worker:
        raise HTTPException(status_code=404, detail="Worker not found")
    return worker

@router.post("")
async def add_worker(worker: WorkerSchema, repo: WorkerRepoDep):
    await repo.add_workers(worker.model_dump())
    return {"status": "ok", "message":"workers added"}
