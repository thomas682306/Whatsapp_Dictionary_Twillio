from twilio.rest import Client

account_sid = 'ACd744570cb9830f07dc55286d681cb003'
auth_token = '0202396c7eb499cb01e76a02890735e5'
client = Client(account_sid, auth_token)

message = client.messages.create(
    from_='whatsapp:+14155238886',
    body='Hello Thomacha',
    to='whatsapp:+918304831354'
)

print(message.sid)