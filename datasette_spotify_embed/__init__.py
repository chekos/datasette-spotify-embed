from datasette import hookimpl
from markupsafe import Markup


@hookimpl
def render_cell(value):
    if not isinstance(value, str):
        return
    if value.startswith("spotify:track:"):
        uri = value.split(":")[-1]
        iframe_options = 'width="100%" height="80" frameBorder="0" allowfullscreen="" allow="autoplay; '
        iframe_options += 'clipboard-write; encrypted-media; fullscreen; picture-in-picture">'
        source = f'src="https://open.spotify.com/embed/track/{uri}?theme=0"'
        iframe = f'<iframe style="border-radius:12px" {source} {iframe_options} </iframe>'
        return Markup(iframe)