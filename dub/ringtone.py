# arpit tiwari
# making ringtone from some song
# install pydub -> pip install pydub
# install pyaudio -> pip install pyaudio
# make sure system has FFmpeg
from pydub import AudioSegment

# make a folder and copy one song in it 
# loading song.mp3 from same folder where our python code is
song = AudioSegment.from_mp3("song.mp3")

# print the durtion of song.mp3
print( int(song.duration_seconds))

# time is taken in mili second to convert in into second multiply by 1000
t=1000
# initilize starting time of ringtone
start=29*t
# initilize finish time of ringtone
end=63*t
#editedSong will be from start to end
editedSong=song[start:end]
#exporting ringtone it will be saved as ringtone.mp3
editedSong.export("ringtone.mp3",format="mp3", tags={'artist': 'Arijit', 'album': 'Best of 2019', 'comments': 'This album is awesome!','title':'arpit is very good'})


## addition part

editedSong2=song[start:end]
# increse volume by 1db
begin = editedSong2 + 1
begin.export("editVolHigh.mp3",format="mp3",bitrate='400k')
# decrease volume by 5 db
end=editedSong2 - 5
end.export("editedVolLow.mp3",format="mp3")
#merging two clips
mixed=begin + end
mixed.export("mixed.mp3",format="mp3")

# fading song
with_style = begin.append(end, crossfade=1500)
with_style.export("faded.mp3",format='mp3')

#editedSong.fade_in(5000).fade_out(1000)
