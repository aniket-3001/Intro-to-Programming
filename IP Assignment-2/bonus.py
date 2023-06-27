# made by:
# Aniket: 2022073
# Angad: 2022071
# Apaar: 2022089

import requests
import json


def quotes(ch):
    if ch == 1:
        url = base_url_1
        try:
            data = requests.get(url).json()
            print("anime:", data["anime"])
            print("character:", data["character"])
            print("quote:", data["quote"])
        except json.decoder.JSONDecodeError as e:
            print(f"Error: {e}")
            print("The API may be down or the endpoint is invalid.")

    elif ch == 2:
        title = input("Enter anime title: ")
        url = base_url_1 + "/anime?title=" + title
        try:
            data = requests.get(url).json()
            print("character:", data["character"])
            print("quote:", data["quote"])
        except json.decoder.JSONDecodeError as e:
            print(f"Error: {e}")
            print("The API may be down or the endpoint is invalid.")

    elif ch == 3:
        character = input("Enter anime character name: ")
        url = base_url_1 + "/character?name=" + character
        try:
            data = requests.get(url).json()
            print("anime:", data["anime"])
            print("quote:", data["quote"])
        except json.decoder.JSONDecodeError as e:
            print(f"Error: {e}")
            print("The API may be down or the endpoint is invalid.")

    elif ch == 4:
        url = base_url_2
        try:
            lst = requests.get(url).json()
            for data in lst:
                print("anime:", data["anime"])
                print("character:", data["character"])
                print("quote:", data["quote"])
                print()
        except json.decoder.JSONDecodeError as e:
            print(f"Error: {e}")
            print("The API may be down or the endpoint is invalid.")

    elif ch == 5:
        title = input("Enter anime title: ")
        url = base_url_2 + "/anime?title=" + title
        try:
            lst = requests.get(url).json()
            for data in lst:
                print("character:", data["character"])
                print("quote:", data["quote"])
                print()
        except json.decoder.JSONDecodeError as e:
            print(f"Error: {e}")
            print("The API may be down or the endpoint is invalid.")

    elif ch == 6:
        character = input("Enter anime character name: ")
        url = base_url_2 + "/character?name=" + character
        try:
            lst = requests.get(url).json()
            for data in lst:
                print("anime:", data["anime"])
                print("quote:", data["quote"])
                print()
        except json.decoder.JSONDecodeError as e:
            print(f"Error: {e}")
            print("The API may be down or the endpoint is invalid.")


print()

base_url_1 = "https://animechan.vercel.app/api/random"
base_url_2 = "https://animechan.vercel.app/api/quotes"

print("choices:\n")

print("1. Get any random anime quote")
print("2. Get any random quote by providing anime title")
print("3. Get any random quote by providing anime character")
print("4. Get any 10 random quotes")
print("5. Get 10 random quotes by providing anime title")
print("6. Get 10 random quotes by providing anime character")
print("Giving anything else as input will result in termination of the program\n")

while True:
    ch = int(input("enter choice no.: "))
    if ch in [1, 2, 3, 4, 5, 6]:
        print()
        quotes(ch)
        print()
    else:
        break
