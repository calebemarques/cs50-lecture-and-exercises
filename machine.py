emoticon = "v.v"

def main():
    global emoticon
    say("Is Anyone There? ")
    emoticon = ":D"
    say("Oh, Hi! ")


def say(phrase):    
    print(phrase + "Hello " + emoticon)


main()