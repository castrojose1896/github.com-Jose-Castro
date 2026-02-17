print("Environmental enginering + Python")
site_elevation=2600
print(f"Project altitude is {site_elevation} meters")
weatherForecast='HOT'
type(weatherForecast)
station_name = "South Melbourne"
station_id = 132310
temp=17.34545
info_text=(f"the temperature at {station_name} (ID:{station_id})is {temp:.2f} Celcius.")
text="Stations:South Melbourne, North Melbourne, East Melbourne"
splitted=text.split(":")
splitted
['Stations','South Melbourne, North Melbourne, East Melbourne']
type(splitted)
list
stations_text=splitted[1]
stations_text
print(info_text)
