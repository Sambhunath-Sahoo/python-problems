user = {}
name, age = str(input('enter your name and age:')).split(',')
fav_movie = input('enter youe fav movie :').split(',')
fav_song = input('enter youe fav song :').split(',')

user['name']=name
user['age']=age
user['fav_movie']=fav_movie
user['fav_song']=fav_song



print(user)