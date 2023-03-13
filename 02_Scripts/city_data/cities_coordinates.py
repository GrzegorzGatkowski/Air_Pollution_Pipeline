import pandas as pd
import requests

cities = ['Warszawa', 'Kraków', 'Łódź', 'Wrocław', 'Poznań', 'Gdańsk', 'Szczecin', 'Bydgoszcz', 'Lublin', 'Katowice',
               'Białystok', 'Gdynia', 'Częstochowa', 'Radom', 'Sosnowiec', 'Toruń', 'Kielce', 'Rzeszów', 'Gliwice', 'Zabrze',
               'Olsztyn', 'Bielsko-Biała', 'Bytom', 'Ruda Śląska', 'Rybnik', 'Tychy', 'Dąbrowa Górnicza', 'Opole', 'Elbląg', 'Płock',
               'Wałbrzych', 'Gorzów Wielkopolski', 'Włocławek', 'Tarnów', 'Chorzów', 'Kalisz', 'Koszalin', 'Legnica', 'Grudziądz',
               'Słupsk', 'Jaworzno', 'Jastrzębie-Zdrój', 'Pruszków', 'Nowy Sącz', 'Mielec', 'Ostrowiec Świętokrzyski', 'Siemianowice Śląskie',
               'Stargard Szczeciński', 'Pabianice', 'Świdnica', 'Skierniewice', 'Kędzierzyn-Koźle', 'Zgierz', 'Łomża', 'Ełk', 'Przemyśl',
               'Starachowice', 'Krotoszyn', 'Gniezno', 'Kołobrzeg', 'Świnoujście', 'Jarosław', 'Zduńska Wola', 'Żyrardów', 'Namysłów', 'Łask',
               'Augustów', 'Kraśnik', 'Pszczyna', 'Ostrołęka', 'Głogów', 'Sandomierz', 'Suwałki', 'Goleniów', 'Złotów', 'Rawicz',
               'Sanok', 'Lębork', 'Nakło nad Notecią', 'Nysa', 'Chojnice', 'Świebodzice', 'Wągrowiec', 'Brzeg', 'Luboń', 'Wieluń',
               'Łaziska Górne', 'Węgrów', 'Ostrzeszów', 'Łęczyca', 'Dzierżoniów', 'Bartoszyce', 'Olecko', 'Bieruń', 'Skarszewy', 'Zwoleń',
               'Chodzież', 'Rydułtowy', 'Bogatynia', 'Lidzbark Warmiński', 'Lubniewice', 'Jasło', 'Pszczyna']

# empty lists for storing coordinates
latitudes = []
longitudes = []

# loop over cities to get their coordinates
for city in cities:
    url = f"https://nominatim.openstreetmap.org/search?q={city},+Poland&format=json"
    response = requests.get(url).json()
    latitude = response[0]["lat"]
    longitude = response[0]["lon"]
    latitudes.append(latitude)
    longitudes.append(longitude)

# create DataFrame from the cities and their coordinates
df = pd.DataFrame({"City": cities, "Latitude": latitudes, "Longitude": longitudes})
df.to_csv('cities.csv', index=False)
print(df.tail())
