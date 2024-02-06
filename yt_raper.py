'''
YouTube Video Downloader
Author: Ayushi Rawat
'''

#import the package
from pytube import YouTube

# niżej to filmik Ayushi Rawat o ripowaniu YT na mp4
#url = 'https://www.youtube.com/watch?v=7BXJIjfJCsA'

# url = 'https://www.youtube.com/watch?v=3iS4cuW6JQ0&list=RDEMDPf0CxyiNqsC7N3jXqAwkA&index=3' #wśród nocnej ciszy
# url = 'https://www.youtube.com/watch?v=U1Rax-YH0t0&list=RDEMDPf0CxyiNqsC7N3jXqAwkA&index=5' #Przybieżeli do Betlejem
# url = 'https://www.youtube.com/watch?v=CafewgrHIKA&list=RDEMDPf0CxyiNqsC7N3jXqAwkA&index=6' #A wczora z wieczora
# url = 'https://www.youtube.com/watch?v=qbzN93kyUPM&list=RDEMDPf0CxyiNqsC7N3jXqAwkA&index=9' #Jezusa narodzonego
# url = 'https://www.youtube.com/watch?v=PXN5UNbSiIw&list=RDEMDPf0CxyiNqsC7N3jXqAwkA&index=13' #W sercach nasyk my Cie wyswiniyncili
# url = 'https://www.youtube.com/watch?v=jqXedrwCwpA&list=RDEMDPf0CxyiNqsC7N3jXqAwkA&index=14' #Leć muzyczko
# url = 'https://www.youtube.com/watch?v=WlepbV0Z0h0&list=RDEMDPf0CxyiNqsC7N3jXqAwkA&index=19' #Czarna Madonno
# url = 'https://www.youtube.com/watch?v=RXCN1vRQIc8&list=RDEMDPf0CxyiNqsC7N3jXqAwkA&index=21' #Czarna Madonno - Jasna Góra
# url = 'https://www.youtube.com/watch?v=FO7xi2R4KS0&list=RDEMDPf0CxyiNqsC7N3jXqAwkA&index=22' #Gore gwiozda
# url = 'https://www.youtube.com/watch?v=JBpIpPfDqEM&list=RDEMDPf0CxyiNqsC7N3jXqAwkA&index=25' #Hej kolenda
# url = 'https://www.youtube.com/watch?v=bXZaWKUuhg8&list=RDEMDPf0CxyiNqsC7N3jXqAwkA&index=27' #Gore gwiozda - Krzeptówki
# url = 'https://www.youtube.com/watch?v=-VJr5B5PDdY&list=RDEMDPf0CxyiNqsC7N3jXqAwkA&index=27' #Dnia jednego o północy
# url = 'https://www.youtube.com/watch?v=ZM51TRlafVQ&list=RDEMDPf0CxyiNqsC7N3jXqAwkA&index=27' #Walczymy do końca
# url = 'https://www.youtube.com/watch?v=EDwkz4ScbZc&list=RDEMDPf0CxyiNqsC7N3jXqAwkA&index=27' #Hej tam spod Tater

url = 'https://www.youtube.com/watch?v=2RHGgvMEWlw' #marsz SS
url = 'https://www.youtube.com/watch?v=Hlh6bAm9gIw' #sieg heil

url = 'https://www.youtube.com/watch?v=SM3Zw4APPQI' #mazur halka

url = 'https://www.youtube.com/watch?v=JjTHr-J74js' #rule britania
url = 'https://www.youtube.com/watch?v=U_rp2R4emcI' #taniec rabina Louis de Fines
url = 'https://www.youtube.com/watch?v=sf9CtbLGzgw' #can can
#url = 'https://www.youtube.com/watch?v=qPnpSJ59dCU' #MESSIAH
#url = 'https://www.youtube.com/watch?v=RPkm8op1oEs' #rondo alla turca


my_video = YouTube(url)
print("*********************Video Title************************")
#get Video Title
print(my_video.title)

print("********************Tumbnail Image***********************")
#get Thumbnail Image
print(my_video.thumbnail_url)

print("********************Download video*************************")
#get all the stream resolution for the 
for stream in my_video.streams:
    print(stream)

#set stream resolution
my_video = my_video.streams.get_highest_resolution()

#or
#my_video = my_video.streams.first()

#Download video
my_video.download()

