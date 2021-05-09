import requests
string = 'https://api.dictionaryapi.dev/api/v2/entries/en/'
resp = requests.get('https://api.dictionaryapi.dev/api/v2/entries/en/')
respCode=resp.status_code
if respCode != 200:
    # This means something went wrong.
    print("Wrong Spelling")
else:
    try :
        meaning = (str(resp.json()[0]['meanings'][0]['definitions'][0]['definition']))
        print("Meaning: "+ meaning)
    except:
        meaning = "No definition found"
    try:
        pronounce = ("Prounciation: " +str(resp.json()[0]['phonetics'][0]['audio']))
        print(pronounce)
    except:
        print("Sorry unavailable")
    try:
        print("Example: "+(str(resp.json()[0]['meanings'][0]['definitions'][0]['example'])))
    except:
        print("no examples available")
    try:
        print("Synonyms: "+(str(resp.json()[0]['meanings'][0]['definitions'][0]['synonyms'])))
    except:
        print("synonyms unavailable")