import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import uvicorn
from fastapi import FastAPI



from src.domain.routers import workers_route


def create_app() -> FastAPI:
    app = FastAPI(
        title="WorkersAPI"
    )

    app.include_router(workers_route.router)

    return app

app = create_app()

if __name__ == "__main__":
    uvicorn.run("src.main:app",reload=True)