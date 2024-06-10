"""Main module for the FastAPI application."""

from enum import StrEnum

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from rich import traceback

from src.config import settings

traceback.install(
    width=120,
    word_wrap=True,
    show_locals=True,
)

app = FastAPI(
    title="HTMX Demo",
    description="A demonstration of HTMX with FastAPI.",
    version="0.1",
)

app.mount(
    path=settings.url_static_root,
    app=StaticFiles(directory=settings.dir_static),
    name="static",
)

renderer = Jinja2Templates(directory=settings.dir_templates)
default_context = {
    "common": {
        "title": "HTMX Demo",
        "description": "A demonstration of HTMX with FastAPI.",
        "language": "en-US",
        "theme": "dark",
    },
}


class templates(StrEnum):
    """Templates for the main route."""

    HOME = "home.j2"
    HOME_HX_PAYLOAD = "home_hx_payload.j2"


class urls(StrEnum):
    """URLs for the main route."""

    HOME = "/"
    HOME_HX_PAYLOAD = "/home-payload"


@app.get(urls.HOME, response_class=HTMLResponse)
async def read_root(request: Request) -> HTMLResponse:
    """Renders the main page."""
    return renderer.TemplateResponse(
        name=templates.HOME.value,
        request=request,
        context=default_context
        | {
            "hx_get_url": urls.HOME_HX_PAYLOAD.value,
        },
    )


@app.get(urls.HOME_HX_PAYLOAD, response_class=HTMLResponse)
async def read_content(request: Request) -> HTMLResponse:
    """Renders the content page."""
    return renderer.TemplateResponse(
        name=templates.HOME_HX_PAYLOAD.value,
        request=request,
        context=default_context | {"payload": "This is a payload."},
    )
