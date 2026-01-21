import requests
import json
import sys 

def main():
    print("Search the Art Institute of Chicago!")
    artist = input("Tell me an artist")
    
    try:
        response = requests.get(
            "https://api.artic.edu/api/v1/artworks/search", 
            {"q": artist}
        )
        response.raise_for_status()
    except  requests.HTTPError:
        print("Couldn't complete request")
        return sys.exit

    content =  response.json()
    for artwork in content ["data"]:
        print(f"*{artwork['title']}")


main()
