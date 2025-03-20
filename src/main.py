"""Main module for the FastAPI application."""

from enum import StrEnum

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from src.config import settings

app = FastAPI(
    title=settings.app_name,
    description=settings.app_description,
    version=settings.app_version,
)

app.mount(
    path=settings.url_static_root,
    app=StaticFiles(directory=settings.dir_static),
    name="static",
)

renderer = Jinja2Templates(directory=settings.dir_templates)
default_context = {
    "common": {
        "title": settings.app_name,
        "description": settings.app_description,
        "language": settings.language,
        "theme": settings.theme,
    },
}


class Templates(StrEnum):
    """Templates for the main route."""

    HOME = "home.j2"
    HOME_HX_PAYLOAD = "home_hx_payload.j2"


class URLs(StrEnum):
    """URLs for the main route."""

    HOME = "/"
    HOME_HX_PAYLOAD = "/home-payload"


@app.get(URLs.HOME, response_class=HTMLResponse)
async def read_root(request: Request) -> HTMLResponse:
    """Renders the main page."""
    return renderer.TemplateResponse(
        name=Templates.HOME.value,
        request=request,
        context=default_context
        | {
            "hx_get_url": URLs.HOME_HX_PAYLOAD.value,
        },
    )


@app.get(URLs.HOME_HX_PAYLOAD, response_class=HTMLResponse)
async def read_content(request: Request) -> HTMLResponse:
    """Renders the content page."""
    return renderer.TemplateResponse(
        name=Templates.HOME_HX_PAYLOAD.value,
        request=request,
        context=default_context | {"payload": "This is a payload from the server."},
    )
