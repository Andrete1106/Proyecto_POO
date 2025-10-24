from pc_test import Computer
from music import Album
c1 = Computer("HP", "Intelcore i5 7th Gen", "8" , "1TB", "Windows 11","NVIDIA GTX 1650","500W","HP","Air cooled","ATX")
c2 = Computer("Lenovo", "Intelcore i5 8th Gen", "4" , "1TB", "Windows 11","----","500W","Lenovo","Air cooled","Lenovo")
c1.specs()
print()
c2.specs()
print()
number_of_tracks = ["Obstaculo","Pasasiempre","Todavia","Fantasma | AVC","Mojabi Ghost","11 y Once","Desde las 10 (Kany's interlude)","Manana","Buenos Aires","Colmillo","La Baby","Me jodi...","Volver","En visto","Lo siento BB:/","Si preguntas por mi","SCI-FI","Corleone interlude","Paranormal","Sacrificio"]
a1 = Album("DATA","Tainy",number_of_tracks)
a1.specs()
for track in number_of_tracks:
    print(track)