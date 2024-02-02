from fastapi import FastAPI
from fastapi.openapi.docs import get_swagger_ui_html
from fastapi.openapi.utils import get_openapi

from app.routers import history_router, forecast_router


app = FastAPI()

# Включите ваш роутер
#app.include_router(history_router)
app.include_router(forecast_router)
@app.get("/swagger/")
async def custom_swagger_ui():
    return get_swagger_ui_html(openapi_url="/openapi.json", title="Weather Forecast API")

# Добавление маршрута для OpenAPI Schema
@app.get("/openapi.json")
async def get_open_api_endpoint():
    return get_openapi(title="Weather Forecast API", version="1.0.0", routes=app.routes)


