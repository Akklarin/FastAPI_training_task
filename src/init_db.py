from src.database import Base, engine
from src.urlshort.models import Urls


async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
