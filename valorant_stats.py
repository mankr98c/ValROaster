import requests

def roast_val_stats(riot_id):
    try:
        name, tag = riot_id.split('#')
        url = f"https://api.henrikdev.xyz/valorant/v1/account/{name}/{tag}"
        r = requests.get(url)
        data = r.json()
        acc = data['data']
        level = acc['account_level']
        region = acc['region']
        return f"{name}#{tag} is level {level} in {region}. Congratulations on surviving that long."
    except:
        return "Couldn't find you. Probably a skill issue."
