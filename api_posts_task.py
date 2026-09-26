import requests

try:
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url, timeout=5)
    response.raise_for_status()  # Raises HTTPError for bad responses

    data = response.json()
    print("Status Code:", response.status_code)
    print("=================Raw Response Text==========")
    print(response.text[:200], "...")  # Print only first 200 chars for readability

    print("\n=================Five ITEMS==========")
    for item in data[0:5]:
        print(item)

    print("\n=================POSTS==========")
    for item in data[0:5]:
        print("POST ID: ", item["id"])
        print("USER ID: ", item["userId"])
        print("TITLE: ", item["title"])
        print("BODY: ", item["body"])
        print("----------------------------------------")

except requests.exceptions.RequestException as e:

 print("Error occurred:", e)
