import requests
def taom_qaytar():
    res=requests.get("https://www.themealdb.com/api/json/v1/1/random.php")
    info=res.json()
    return info['meals'][0]
