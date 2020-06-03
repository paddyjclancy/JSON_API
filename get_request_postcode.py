import requests


def geo_locate(postcode):
    response = requests.get(path + postcode)
    if response.status_code == 400:
        print("Oops, something went wrong")
    elif response.status_code == 200:
        response_dict = response.json()
        result_dict = response_dict['result']
        print(
            f"Your longitude is {result_dict['longitude']}, your latitude is {result_dict['latitude']}, your parliamentary_constituency is {result_dict['parliamentary_constituency']},  and your NUTS value is {result_dict['nuts']}")
    else:
        print("Please try again - Better luck next time")

while True:
    postcode = (input("Please enter a postcode, or enter 'exit':   ")).replace(" ", "").lower()
    path = 'http://api.postcodes.io/postcodes/'

    if postcode == "exit":
        print("Goodbye")
        break
    else:
        geo_locate(postcode)
