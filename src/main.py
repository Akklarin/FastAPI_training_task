from fastapi import FastAPI
from api import main_router
from urlshort.config import settings
import uvicorn

app = FastAPI()
app.include_router(main_router)

url_store = {}

# if __name__ == '__main__':
#     uvicorn.run('main:app', port=8080, reload=True)


if __name__ == '__main__':
    uvicorn.run(
        'src.main:app',
        host=settings.PROJECT_HOST,
        port=settings.PROJECT_PORT,
    )
