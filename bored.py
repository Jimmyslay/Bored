import requests
import json

#The code we made consists of two main parts: the MakeApiCall class and the code block under if __name__ == "__main__":.
class MakeApiCall:
    
    #The get_data method takes an API URL as a parameter and sends a GET request to that API using the
    #requests.get function from the requests module. If the response status code is 200 (indicating a successful
    #request), it prints "successfully fetched the data" and calls the formatted_print method, passing the response data as JSON.
    def get_data(self, api):
        response = requests.get(f"{api}")
        if response.status_code == 200:
            print("sucessfully fetched the data")
            self.formatted_print(response.json())

    #The formatted_print method takes an object (in this case, the response data) and uses the json.dumps function from the json module to convert it to a formatted string.
    #The sort_keys=True argument sorts the keys in the JSON object, and indent=4 adds indentation for readability.
    #Finally, it prints the formatted JSON string. The __init__ method is the constructor of the class. It takes an API URL as a parameter and immediately calls the get_data method, passing the API URL.
    def formatted_print(self, obj):
        text = json.dumps(obj, sort_keys=True, indent=4)
        print(text)

    def __init__(self, api):
        self.get_data(api)

#This block is the entry point of the program, which means it will be executed when the script is run directly.
#It starts an infinite loop using while True, which can be exited by entering 'y' when prompted.
#It prompts the user to choose a category (accessibility, key, participants, price, or type) to filter the activity. 
#Depending on the chosen category, it provides further instructions on how to input the value for that category.
#The user's chosen category and value are used to construct the API URL by appending them as query parameters.
#An instance of the MakeApiCall class is created, passing the constructed API URL as a parameter. This triggers the API call and printing of the fetched data.
#After each API call, the user is prompted if they are done. If the user enters 'y', the loop breaks and the program terminates.
if __name__ == "__main__":
  while True:
      chosen_category = input("which catagory do you want to filter? accessibility, activity, key, link, participants, price, or type? ")
      if chosen_category == "type":
        print("please choose education, recreational, social, diy, charity, cooking, relaxation, music, or busywork")
      if chosen_category == "price":
        print("choose a number between 0 and 0.5")
      if chosen_category == "participants":
        print("choose a number between 0 and 9")
      activity_type = input("Give the value to your chosen category (" + chosen_category + "): ")
      api_call = MakeApiCall("https://www.boredapi.com/api/activity?" + chosen_category + "=" + activity_type)
      done = input("Are you done (y or n)? ")
      if done == "y":
        break
        
