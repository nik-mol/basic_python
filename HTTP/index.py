import requests
import os

# -------------------Task1-------------------------

def get_superheroes(url):  
  headers = {"Autorization": "2619421814940190"}
  response = requests.get(url, headers=headers)
  
  for value in response.json().values():
    result = value
  result_name = result[0]['name']
  result_intelligence = int(result[0]['powerstats']['intelligence'])  
  return {result_name: result_intelligence}

def most_intelligence():   
    Hulk = get_superheroes("https://superheroapi.com/api.php/2619421814940190/search/Hulk")
    Captain_America = get_superheroes("https://superheroapi.com/api.php/2619421814940190/search/Captain America")
    Thanos = get_superheroes("https://superheroapi.com/api.php/2619421814940190/search/Thanos")  
    dict_superheroes = {**Hulk, **Captain_America, **Thanos}   
    most_intelligence_superhero = max(dict_superheroes, key=dict_superheroes.get)
    print(f"Супер герой с максимальным интеллектом:  {most_intelligence_superhero}")
    
if __name__ == '__main__':
  most_intelligence()
  
# -------------------Task2-------------------------

TOKEN = "AQAAAAAMXeVcAADLW64nqInsAE_GnjUaGTbQFFY"

class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': self.token
        }

    def get_upload_disk(self, file_path):
      upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
      headers = self.get_headers()
      params = {"path": file_path, "overwrite": True}
      response = requests.get(upload_url, headers = headers, params = params)
      return response.json() 
  
    def upload(self, file_path, path_to_file):
      href = self.get_upload_disk(file_path).get("href")
      response = requests.put(href, open(path_to_file, 'rb'))
      response.raise_for_status()
      if response.status_code == 201:
          print("Success")
       
if __name__ == '__main__':
  
    token = TOKEN
   
    BASE_PATH = os.getcwd()
    LOGS_NAME = 'files'
    FILE_NAME = 'test_file.txt'
    path_to_file = os.path.join(BASE_PATH, LOGS_NAME, FILE_NAME)
  
    uploader = YaUploader(token)
    result = uploader.upload('Документы/' + FILE_NAME, path_to_file)