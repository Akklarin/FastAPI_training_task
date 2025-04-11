from fastapi import APIRouter
import asyncio
import httpx
import requests

router = APIRouter()


@router.get("/async-request")
async def async_request():
    print("Начинаю асинхронный запрос")
    await asyncio.sleep(5)
    async with httpx.AsyncClient() as client:
        response = await client.get("https://jsonplaceholder.typicode.com/todos/1")
    print("Асинхронный запрос выполнен")
    return response.json()


@router.get("/sync-request-for-test", description='запрос для проверки асинхронности')
def sync_request():
    print("Начинаю синхронный запрос")
    response = requests.get("https://jsonplaceholder.typicode.com/todos/2")
    print("Синхронный запрос выполнен")
    return response.json()