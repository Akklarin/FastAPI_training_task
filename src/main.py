from fastapi import FastAPI
from src.api import main_router
from src.urlshort.config import settings
from src.init_db import init_db
import uvicorn

app = FastAPI()
app.include_router(main_router)


@app.on_event("startup")
async def on_startup():
    await init_db()


if __name__ == '__main__':
    uvicorn.run(
        'src.main:app',
        host=settings.PROJECT_HOST,
        port=settings.PROJECT_PORT,
    )
