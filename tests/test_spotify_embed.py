from datasette.app import Datasette
import pytest
import sqlite_utils


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "value,expect_embed",
    (
        (1, False),
        (1.2, False),
        (None, False),
        ("dog", False),
        ("track:uri:108", False),
        ("spotify:track:13508703-", True),
        ("spotify:track:jkavusdbvafbasdu", True),
        ("spotify:track:10814801038ndvaodn", True),
    ),
)
async def test_spotify_embed(value, expect_embed):
    datasette = Datasette(memory=True)
    db = datasette.add_memory_database("test")

    def setup(conn):
        sqlite_utils.Database(conn)["demo"].insert({"value": value})

    await db.execute_write_fn(setup, block=True)

    response = await datasette.client.get("/test/demo")
    assert response.status_code == 200
    html = response.text
    if expect_embed:
        assert (
            f'<iframe style="border-radius:12px" src="https://open.spotify.com/embed/track/{value.split(":")[-1]}?theme=0" width="100%" height="80" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture"></iframe>'
            in html
        )
    else:
        assert "<iframe " not in html
