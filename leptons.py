import requests
import time
from twilio.rest import Client
from datetime import datetime

url = 'https://api.coinmarketcap.com/v1/ticker/bitcoin/'
def get_bitcoin_price():

    response = requests.get(url)
    my_json = response.json()
    return  float(my_json[0]['price_usd'])

def sms(talk):
    """
    In order to see how this function is used, it would be better
    to signup with get the twilio API by signing up for
    a trial account on the twilio website.
    visit https://www.twilio.com
    There are other APIs like WhatsApp's Sandbox you could use as well
    in addition to lots of tools.


    This function sends an SMS or MMS to a number(a verified twilio number)


    """
    # Your Account Sid and Auth Token from twilio.com/console
    # DANGER! This is insecure. See http://twil.io/secure
    account_sid = 'AC5d5e141a40cd1ad612f1bbab6524374c'
    auth_token = '60d557e226be1fd70447ed6ec8697fa8'
    client = Client(account_sid, auth_token)

    message = client.messages.create(
                                  from_= '+12672142542',
                                  body = talk,
                                  to = '+14849047054'
                              )

    print(message.sid)


data = get_bitcoin_price()

def main():


    while True:
        date = datetime.now()
        message = str('Today is: '+ str(date) +'\n'+'Bitcoin is valued at $'+str(data))
        sms(message)
        time.sleep(5*60)


if __name__ == '__main__':
    main()
