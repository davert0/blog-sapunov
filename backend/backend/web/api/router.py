from fastapi.routing import APIRouter

from backend.web.api import docs, dummy, echo, monitoring, article, user

api_router = APIRouter()
api_router.include_router(monitoring.router)
api_router.include_router(docs.router)
api_router.include_router(article.router, prefix="/articles", tags=["articles"])
api_router.include_router(user.router, prefix="/user", tags=["user"])
api_router.include_router(echo.router, prefix="/echo", tags=["echo"])
api_router.include_router(dummy.router, prefix="/dummy", tags=["dummy"])
