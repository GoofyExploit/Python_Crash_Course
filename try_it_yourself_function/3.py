# # City Names:

def city_country(city,country):
    full_name = f"{city.title()}, {country.title()}"
    return full_name
while True:
    print("\nTell us about your Vacation plans:")
    print("Enter 'q' at any time to quit.")

    city = input("Name of a city: ")
    if city == 'q':
        break
    country = input("It's Country: ")
    if country == 'q':
        break
    country_city = city_country(city,country)
    print(f"{country_city}")

# # Album:

def make_album(artist,album,songs=None):
    album = {'artist':artist,'album_title':album}
    if songs:
        album['songs'] = songs
    return album

albums = []

while True:
    print("\nTell us about your recommendations:")
    print("Enter 'q' to quit any time.")

    artist = input("Enter artist's name: ").title()
    if artist.lower() == 'q':
        break
    album_title = input("Enter its album: ").title()
    if album_title.lower() == 'q':
        break
    songs_number = input("Enter the no. of songs in this album (press enter to skip): ")
    if songs_number:
        songs_num = int(songs_number)
    else:
        songs_num = None

    full_album = make_album(artist,album_title,songs_number)
    albums.append(full_album)

for album in albums:
    print(album)