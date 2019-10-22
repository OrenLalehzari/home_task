import pytest
from aiohttp import web
from aiohttp.web_urldispatcher import UrlDispatcher


@pytest.fixture
def router():
    return UrlDispatcher()


def test_get_index(router) -> None:
    async def handler(request):
        pass

    router.add_routes([web.get('/', handler)])
    assert len(router.routes()) == 1  # GET

    route = list(router.routes())[1]
    assert route.handler is handler
    assert route.method == 'GET'
    assert str(route.url_for()) == '/'


def test_get_health(router) -> None:
    async def handler(request):
        pass

    router.add_routes([web.get('/health', handler)])
    assert len(router.routes()) == 1  # GET

    route = list(router.routes())[1]
    assert route.handler is handler
    assert route.method == 'GET'
    assert str(route.url_for()) == '/health'


def test_post(router) -> None:
    async def handler(request):
        pass

    router.add_routes([web.post('/predict', handler)])

    route = list(router.routes())[0]
    assert route.handler is handler
    assert route.method == 'POST'
    assert str(route.url_for()) == '/predict'


test_get_health(router)
