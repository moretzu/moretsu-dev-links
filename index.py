from flask import Flask, redirect, abort, render_template_string

LINKS = {
    "twitch": "https://www.twitch.tv/moretsuu",
    "github": "https://github.com/moretzu",
    "telegram": "https://t.me/moretsu",
    "twitter": "https://twitter.com/david_moretsu",
}


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/")
def index():
    links_as_buttons = ""

    for platform, url in LINKS.items():
        links_as_buttons += f'<a role="button" href="{url}">{platform}</a><br/>'

    template_string = "<h1>hi, this is my sort of URL shortener pls go away :(</h1><a href=https://moretsu.dev>my main website</a>"
    template_string += (
        f"<h3>links to my socials and other things</h3>{links_as_buttons}"
    )

    return render_template_string(template_string)


@app.route("/<platform>")
def url_to_platform(platform: str):
    url = LINKS.get(platform.lower())

    if url:
        return redirect(url, 307)

    return abort(404)
