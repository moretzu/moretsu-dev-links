from flask import Flask, redirect, abort

LINKS = {
    "twitch": "https://www.twitch.tv/moretsuu",
    "github": "https://github.com/moretzu",
    "telegram": "https://t.me/moretsu",
    "twitter": "https://twitter.com/david_moretsu",
}


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/<platform>")
def url_to_platform(platform: str):
    url = LINKS.get(platform.lower())

    if url:
        return redirect(url, 307)

    return abort(404)
