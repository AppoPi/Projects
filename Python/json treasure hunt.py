text = '''{
    "name": "William Shakespeare",
    "birthYear" : 1564,
    "dead" : true,
    "deathYear" : 1616,
    "selectedWorks" : [
        {
            "name" : "The Tragedy of Macbeth",
            "written" : 1606,
            "isItAwesome" : true
        },
        {
            "name" : "Coriolanus",
            "written" : 1608,
            "isItAwesome" : "It's alright, but kinda fascist-y"
        }
    ],
    "wife" : {
        "name" : "Anne Hathaway",
        "birthYear" : 1555,
        "dead" : false,
        "deathYear" : "Fun fact, she's a vampire"
    },
    "favoriteWebsites" : [
        "dailysonneter",
        "dailyprogrammer",
        "vine (he's way into 6-second cat videos)"
    ],
    "facebookProfile" : null
}'''

from pprint import pprint
import json

def find_value(input, value):
    for i,x in enumerate(input):
        print i,x
        print type(input)
        if type(input) == dict:
            print 'Value found to be a dictionary'
            print 'Seeing value of dictionary\'s first element is ' + str(input[x])
        elif type(input) == list:
            print 'Value found to be a list'
        elif type(input) in [int, str]:
            print input


find_value({'test':1606}, 1606)
find_value([5,1250,1606], 1606)
