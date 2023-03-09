# TODO здесь писать код
import requests
import json

def get_pilot_data(url):
    pilot_d = {}
    pilot = json.loads(requests.get(url).text)
    for pilot_k, pilot_val in pilot.items():
        if pilot_k == 'name' or pilot_k == 'height' or pilot_k == 'mass' or pilot_k == 'homeworld':
            pilot_d[pilot_k] = pilot_val
    return pilot_d

result = requests.get("https://swapi.dev/api/starships/10/")
dict = {}
pilots_d = []
count = 0
if result.status_code == 200:
    data = json.loads(result.text)
    for key, val in data.items():
        if key == 'name' or key == 'max_atmosphering_speed' or key == 'starship_class':
           dict[key] = val
        elif key == 'pilots':
            for _ in val:
                pilots_d.append(get_pilot_data(val[count]))
                dict[key] = pilots_d
                count += 1

    print(json.dumps(dict, indent=4))

    with open("swap.json", "w") as file:
        json_text = json.dump(dict, file, indent=4)







