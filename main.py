from flask import Flask, render_template
import datetime
import spotipy
import spotipy.util
from spotipy import oauth2
from spotipy.oauth2 import SpotifyClientCredentials

app = Flask(__name__)

app.config["SECRET_KEY"]         = "execute order 66"
app.config["SPOTIFY_CLIENT"]     = "e29426dfb22c41cdbc92122fbb9c398c"
app.config["SPOTIFY_SECRET"]     = "e29426dfb22c41cdbc92122fbb9c398c"
app.config["SPOTIFY_SCOPE"]      = "playlist-modify-public playlist-modify-private playlist-read-private playlist-read-collaborative user-read-recently-played user-top-read"
app.config["SPOTIFY_CACHE"]      = ".spotifyoauthcache"
app.config["CLIENT_CREDENTIALS"] = SpotifyClientCredentials(client_id = app.config["SPOTIFY_CLIENT"], client_secret = app.config["SPOTIFY_SECRET"])

@app.route("/")
def index():
    return render_template("index.html", year=datetime.datetime.now().year)

if __name__ == "__main__":
    app.run(debug=True)