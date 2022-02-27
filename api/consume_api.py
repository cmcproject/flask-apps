import requests


response = requests.get("http://api.stackexchange.com/2.3/questions?order=desc&sort=activity&site=stackoverflow")
print(response)
print(response.json())

for data in response.json()["items"]:
    if data['answer_count'] == 0:
        print(data['title'])
        print(data['link'])
    else:
        print("Skipped")
    print()
