# 8.7专辑
def make_album(singer, Album_name, Number_of_songs=''):
    album = {'singer': singer, 'ablum': Album_name}
    if Number_of_songs:
        album['Number_of_songs'] = Number_of_songs
    return album


album_1 = make_album('Jay', 'Fantasy')
print(album_1)
album_2 = make_album('Mayday', 'autobiography')
print(album_2)
album_3 = make_album('Mayday', '离开地球表面Jump!')
print(album_3)
album_4 = make_album('Mayday', '离开地球表面Jump!', '17')
print(album_4)