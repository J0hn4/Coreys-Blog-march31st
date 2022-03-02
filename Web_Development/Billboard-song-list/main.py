from bs4 import BeautifulSoup
import lxml
import requests
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# pick_date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
# date_split = pick_date.split("-")



SPOT_CLIENT_SECRET = "ffb813aa75674bbfbb757ff9b06f0893"
SPOT_CLIENT_ID = "fe8b07f572cd46ada81d01d6b62f074a"
FIRST_SONG_CLASS = "c-title__link lrv-a-unstyle-link"
CLASS_SONG="c-title a-no-trucate a-font-primary-bold-s u-letter-spacing-0021 lrv-u-font-size-18@tablet lrv-u-font-size-16 u-line-height-125 u-line-height-normal@mobile-max a-truncate-ellipsis u-max-width-330 u-max-width-230@tablet-only"
FIRST_ARTIST_CLASS = "c-tagline  a-font-primary-l a-font-primary-m@mobile-max lrv-u-color-black u-color-white@mobile-max lrv-u-margin-tb-00 lrv-u-padding-t-025 lrv-u-margin-r-150"
CLASS_ARTIST = "c-label a-no-trucate a-font-primary-s lrv-u-font-size-14@mobile-max u-line-height-normal@mobile-max u-letter-spacing-0021 lrv-u-display-block a-truncate-ellipsis-2line u-max-width-330 u-max-width-230@tablet-only"
URL = f"https://www.billboard.com/charts/hot-100/1983-10-12/"
USER_AGENT = "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:97.0) Gecko/20100101 Firefox/97.0"

headers = {
    "User-Agent": USER_AGENT,
}




response = requests.get(URL, headers=headers)
billboard_web_page = response.text
soup = BeautifulSoup(billboard_web_page, "lxml")


song_info = soup.find_all(name="h3", id="title-of-a-story", class_=CLASS_SONG)
# print(song_info)

first_song_info = soup.find(name="a", class_=FIRST_SONG_CLASS)
first_song = first_song_info.string.strip()

song_band = soup.find_all(name="span", class_=CLASS_ARTIST)
# band_name = song_band.string
# print(song_band)

# first_band = soup.find(name="p", class_=FIRST_ARTIST_CLASS)
# print(first_band)


song_band_list = []
song_list = []
song_list.append(first_song)

for song in song_band:
    band = song.getText()
    song_band_list.append(band.strip())

for song in song_info:
    name = song.getText()
    song_list.append(name.strip())

# print(song_band_list)
# print(song_list)

# sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=SPOT_CLIENT_ID,
#                                                            client_secret=SPOT_CLIENT_SECRET))
#
# results = sp.search(q=song_list, limit=20)
# for idx, track in enumerate(results['tracks']['items']):
#     print(idx, track['name'])

    # Creating the Spotipy Object
    sp = spotipy.Spotify(
        auth_manager=SpotifyOAuth(
            scope="playlist-modify-private",
            redirect_uri="https://example.com",  # Your URI
            client_id=SPOT_CLIENT_ID,  # YOUR CLIENT ID
            client_secret=SPOT_CLIENT_SECRET,  # Your Client Secret
            show_dialog=True,
            cache_path="token.txt"
        )
    )

    user_id = sp.current_user()["id"]