# BITCOIN-TRACKER
This script makes use of two APIs: the CoinCapMarket API and the Twilio API.
The CoinCapMarket API produces data on fluctuating bitcoin prices and the Twilio API, a cloud messaging API, to send 
the prices as texts every five minutes.


**HOW TO MODIFY MY SCRIPT**
1. Get a free Twilio trial account in other to get your account sid and the auth token.
2. Run script from terminal to see code in action.

**LIBRARIES TO IMPORT**
1. requests
2. time
3. twilio.rest #you'd have to install this. 
4. datetime

**FUNCTIONS**
1. get_bitcoin_price()
This function sends AND receives requests to the CoinCapMarket API 
2. sms() #takes an input
This function makes use of the Twilio API to send the message
3. main()
This is the most important, which executes the function.
