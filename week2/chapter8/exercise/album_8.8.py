# 8.7专辑
def make_album(singer, Album_name, Number_of_songs=''):
    album = {'singer': singer, 'ablum': Album_name}
    if Number_of_songs:
        album['Number_of_songs'] = Number_of_songs
    return album


while True:
    print("\nPlease enter the artist and name of an album: ")
    print("(enter 'q' at any time to quit)")
    s_name = input("Singer`s name: ")
    if s_name == 'q':
        break
    a_name = input("Album`s name: ")
    if a_name == 'q':
        break
    album_0 = make_album(s_name, a_name)
    print(album_0)
