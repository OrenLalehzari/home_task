import logging
from aiohttp import web
import aiohttp_jinja2
import jinja2
from PIL import Image

from src.neuralnetwork.main import main
from src.middlewares.middleware import setup_middlewares

logger = logging.getLogger(__name__)

HOST = "http://0.0.0.0:8080/"
routes = web.RouteTableDef()


@routes.get('/')
async def index(request):
    response = aiohttp_jinja2.render_template('home.html', request, {})
    return response


@routes.get('/health')
async def health(request):
    return web.json_response({"health": "Ok"}, status=200)


@routes.post('/predict')
async def predict(request):
    data = await request.post()
    image = data['image_file']
    img = Image.open(image.file)
    image_processing_data = main(img)
    res = ['%s, %s, %s' % o for o in image_processing_data[0]]
    return web.json_response(res, status=200)


def set_logging_env():
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)


async def init_app() -> web.Application:
    app = web.Application()
    set_logging_env()
    logger.info('Running on %s' % HOST)
    aiohttp_jinja2.setup(app, loader=jinja2.FileSystemLoader('src/templates'))
    app.add_routes(routes)
    setup_middlewares(app)
    return app


if __name__ == '__main__':
    web.run_app(init_app())
