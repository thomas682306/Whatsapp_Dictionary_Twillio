from flask import Flask, request, redirect
import requests
from twilio.twiml.messaging_response import MessagingResponse

import DictionaryApi

app = Flask(__name__)

@app.route("/sms", methods=['GET', 'POST'])
def incoming_sms():
    """Send a dynamic reply to an incoming text message"""
    # Get the message the user sent our Twilio number
    body = request.values.get('Body', None)

    # Start our TwiML response
    resp = MessagingResponse()

    # Determine the right reply for this message
    wordRequest = DictionaryApi.string + str(body)
    myResp = requests.get(wordRequest)
    respCode = myResp.status_code

    if respCode != 200:
        resp.message("Something went wrong")

    else :
        try:
            meaning = (str(myResp.json()[0]['meanings'][0]['definitions'][0]['definition']))
            resp.message("Meaning: " + meaning)
        except:
            meaning = "No definition found"
            resp.message("Meaning: " + meaning)
        try:
            pronounce = ("Prounciation: " + str(myResp.json()[0]['phonetics'][0]['audio']))
            resp.message(pronounce)
        except:
            resp.message("Sorry unavailable")
        try:
            resp.message("Example: " + (str(myResp.json()[0]['meanings'][0]['definitions'][0]['example'])))
        except:
            resp.message("no examples available")
        try:
            resp.message("Synonyms: " + (str(myResp.json()[0]['meanings'][0]['definitions'][0]['synonyms'])))
        except:
            resp.message("synonyms unavailable")
    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)