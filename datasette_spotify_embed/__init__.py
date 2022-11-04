from datasette import hookimpl
from markupsafe import Markup, escape


@hookimpl
def extra_css_urls(columns, datasette):
    if not columns:
        return None
    return [
        datasette.urls.static_plugins(
            "datasette-spotify-embed", "datasette-spotify-embed.css"
        )
    ]


@hookimpl
def render_cell(value):
    if not isinstance(value, str):
        return
    if value.startswith("spotify:track:"):
        uri = escape(value.split(":")[-1])
        iframe = (
            f'<iframe style="border-radius:12px" '
            f'src="https://open.spotify.com/embed/track/{uri}?theme=0" '
            'width="100%" height="80" frameBorder="0" allowfullscreen="" allow="autoplay; '
            'clipboard-write; encrypted-media; fullscreen; picture-in-picture">'
            "</iframe>"
        )
        return Markup(iframe)
