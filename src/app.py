import requests, os, json

# Retrieve your API credentials from the .env file
if os.getenv("API_KEY") is None or os.getenv("API_KEY") == "":
    print("ERROR! Make sure you have created your .env file with your API credentials (look for the .evn.example as an example and replace it with your own API credentials that you got from RapidAPI)")
    exit(1)

# Get credentials from the .env file
API_HOST = os.getenv("API_HOST") 
API_KEY = os.getenv("API_KEY")

# continue with your application here

def sync_word(user_response,_permission):
    text_file = open("src/"+user_response+"_definition.txt",_permission)
    if _permission =="w+": 
        text_file.write(body["list"][0]["definition"])
    else:
        return text_file.read()
    text_file.close()

user_response = input("What term do you want to look for?")

if os.path.isfile("src/"+user_response+"_definition.txt"):
    print("Fetching From Cache")
    print(sync_word(user_response,"r"))
else:
    url = "https://mashape-community-urban-dictionary.p.rapidapi.com/define?term="+user_response

    headers = {
        'x-rapidapi-host': API_HOST,
        'x-rapidapi-key': API_KEY
        }

    response = requests.request("GET", url, headers=headers)

    body = response.json()

    definitions_array = body["list"]

    single_definition_from_dict = definitions_array[0]

    print(single_definition_from_dict)
    #print(response.text)

    text_file = open("src/"+user_response+"_definition.txt", "w")
    text_file.write(single_definition_from_dict)
    text_file.close()