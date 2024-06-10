"""Settings for the web application."""

from rich import traceback

traceback.install(
    width=120,
    word_wrap=True,
    show_locals=True,
)


class _Settings:
    """Settings for the web application."""

    _app_root: str = "src"
    _static_root: str = "/static"
    app_description: str = "A demonstration of HTMX with FastAPI."
    app_name: str = "HTMX Demo"
    app_version: str = "0.1"
    host: str = "localhost"
    language: str = "en-US"
    port: int = 8000
    protocol: str = "http"
    theme: str = "dark"

    def __init__(self, **kwargs) -> None:
        self.__dict__.update(kwargs)

    @property
    def url_base(self) -> str:
        """The base URL for the web application."""
        return f"{self.protocol}://{self.host}:{self.port}"

    @property
    def url_static_root(self) -> str:
        """The root directory for static files."""
        return self._static_root

    @property
    def dir_static(self) -> str:
        """The location of the static files."""
        return f"{self._app_root}/static"

    @property
    def dir_templates(self) -> str:
        """The location of the templates."""
        return f"{self._app_root}/templates"


settings = _Settings()

__all__ = ["settings"]
