import logging
import aiofiles
import aiohttp_jinja2
import jinja2
from aiohttp import web, ClientSession
import subprocess
from aiohttp.web_exceptions import HTTPInternalServerError

from src.middlewares.middleware import setup_middlewares

logger = logging.getLogger(__name__)

HOST = "http://0.0.0.0:8080/"
MEDIA_FILES_URL = 'src/media/images/image_to_process'
COMMAND_FUNCTION = 'image-processing/main.py'

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
    await save_image_locally(request)
    logger.info('starting image processing')
    try:
        results = subprocess.check_output(['python3.6', COMMAND_FUNCTION, MEDIA_FILES_URL]).decode()
    except subprocess.CalledProcessError as e:
        logger.error('error image processing: %s ' % e)
        raise HTTPInternalServerError()
    logger.info('success image processing')
    return web.Response(text=results, status=200)


async def save_image_locally(request):
    async with ClientSession() as session:
        async with session.get(HOST) as resp:
            if resp.status == 200:
                logger.info('save uploaded image')
                f = await aiofiles.open(MEDIA_FILES_URL, mode='wb')
                data = await request.post()
                image = data['my_image']
                await f.write(image.file.read())
                await f.close()
                logger.info('success image uploaded locally')


def set_logging_env():
    logging.basicConfig(format='', level=logging.INFO)


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
