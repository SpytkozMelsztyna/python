'''
Python Convert Mp4 to Mp3 File Using MoviePy Library Full Project For Beginners
Coding Shiksha
'''
from moviepy.editor import *
mp4_file = 'Spotkanie otwarte PJJ gość Jan Łopuszański - Warszawa  27022024 g 1730.mp4'
mp3_file = 'Spotkanie otwarte PJJ gość Jan Łopuszański - Warszawa  27022024 g 1730.mp3'
video_clip = VideoFileClip(mp4_file)
audio_clip = video_clip.audio
audio_clip.write_audiofile(mp3_file)
audio_clip.close()
video_clip.close()

