SHOWS = [       

"Ben 10",
 "Avatar: The Last Airbender",
   "Phineas and Ferb", 
   "The Simpsons",
     "The Amazing World of Gumball",
   "Gravity Falls",
   "Adventure Time",
   "Steven Universe",
   "Regular Show",
   "Futurama",
   "Rick and Morty",
   "SpongeBob SquarePants",
   "The Loud House",
   "Teen Titans Go!",
   "DuckTales",
   "Big Hero 6: The Series",
   "Star Wars: The Clone Wars",
    "Star Wars Rebels", 
    "The Owl House",    
    "Amphibia",
    "Kipo and the Age of Wonderbeasts",
    "Infinity Train",
    "Hilda",
    "Tales of Arcadia",
    "The Dragon Prince",
    "Voltron: Legendary Defender",
    "She-Ra and the Princesses of Power",
    "Carmen Sandiego",
    "The Legend of Korra",
    "Young Justice",
    "Justice League",
    "Justice League Unlimited",
    "Batman: The Animated Series",
    "Superman: The Animated Series"
    ]
def main():
    cleaned_shows = []
    for show in SHOWS:
        cleaned_shows.append(show.strip().title())

    
    print(','.join(cleaned_shows))

main()