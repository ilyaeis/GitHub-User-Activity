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

    list = convert_to_list(data)
        
    return list
    
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
    api_url = "https://api.github.com/users/"
    login = input("Input username on github: ")

    return api_url + login

if __name__ == "__main__":
    url = get_username_input()

    while True:
        data = get_data(url)
        
        if not data:
            print("Exiting due to no data.")
            break

        print_data(data)
        
        try:
            index = int(input("Input index out of possible, if apilink: will be redirected there, else: exit program: "))
            
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

    print("Bye!")



