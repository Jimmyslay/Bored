import requests
import json


class MakeApiCall:

    def get_data(self, api):
        response = requests.get(f"{api}")
        if response.status_code == 200:
            print("sucessfully fetched the data")
            self.formatted_print(response.json())

    def formatted_print(self, obj):
        text = json.dumps(obj, sort_keys=True, indent=4)
        print(text)

    def __init__(self, api):
        self.get_data(api)


if __name__ == "__main__":
  while True:
      chosen_category = input("which catagory do you want to filter? accessibility, activity, key, link, participants, price, or type? ")
      activity_type = input("Give the value to your chosen category (" + chosen_category + "): ")
      api_call = MakeApiCall("https://www.boredapi.com/api/activity?" + chosen_category + "=" + activity_type)
      done = input("Are you done (y or n)? ")
      if done == "y":
        break
        
