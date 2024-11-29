import requests
import validators

# TODO headers = {"Authorization": "token YOUR_PERSONAL_ACCESS_TOKEN"}


def print_data(data):
    if not data:
        print("No data available.")
        return
    
    for i, (key, value) in enumerate(data):
        print(f"{i}. {key}: {value}")

def convert_to_list(data):
    result = []
    if isinstance(data, list): 
        for item in data:
            if isinstance(item, dict): 
                for key, value in item.items():
                    if value is not None and value != "":
                        result.append([key, value])
    elif isinstance(data, dict):
        for key, value in data.items():
            if value is not None and value != "":
                result.append([key, value])

    return result

def get_data(url):
    try:
        response = requests.get(url)
        data = response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error making the request: {e}")
        return None
    except ValueError:
        print("Error decoding JSON from response.")
        return None
        
    return data
    
# TODO check if such user exists without using API
# def validate_user(login):
#     url = "https://github.com/" + login
#     return validators.url(url)

def validate_url(url):
    if validators.url(url):
        return url
    else:
        return None
    
def get_username_input():
    login = input("Input username on github: ")
    api_url = f"https://api.github.com/users/{login}"
    return api_url

def user_loop():
    url = get_username_input()

    while True:
        data = convert_to_list(get_data(url))
        
        if not data:
            print("Exiting due to no data.")
            break

        print_data(data)
        
        try:
<<<<<<< HEAD
            index = int(input("Input index out of possible, if api link: will be redirected there, else: exit program: "))
=======
            index = int(input("Input index out of possible, if apilink: will be redirected there, else: exit program: "))
>>>>>>> 7abc031b6e7572f8e02751e255d98c72924dc60e
            
            if 0 <= index < len(data):
                url = data[index][1]
            else:
                print("Invalid index")
                break

            if not validate_url(url): 
                break

        except ValueError:
            print("Invalid input. Exiting.")
            break

    print("Exit user loop!")
    

def print_events_data(data):
    if not data:
        print("No data available.")
        return
    
    for event in data:
        event_type = event["type"].replace("Event", "")
        if event_type.endswith("e"):
            event_type += "d"
        else:
            event_type += "ed"
        repo_name = event["repo"]["name"]
        login_name = event["actor"]["display_login"]
        
        print(f"User {login_name} {event_type} the repository {repo_name}")


def check_events():
    url = get_username_input()+"/events"

    data = get_data(url)
        
    if not data:
        print("Exiting due to no data.")
        return
    
    print_events_data(data)
    
if __name__ == "__main__":
    choice = input("Enter 'user' if you want to check info about user\nEnter 'events' if you wnt to check info about user's events.")
    
    match(choice):
        case "user":
            user_loop()
        case "events":
            check_events()

    print("Bye!")


