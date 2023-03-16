import vonage

from otp.local_settings import VONAGE_API_KEY, VONAGE_API_SECRET, VONAGE_BRAND_NAME


def send_sms(phone_number, token):
    client = vonage.Client(key=VONAGE_API_KEY, secret=VONAGE_API_SECRET)
    responseData = client.sms.send_message(
        {
            "from": VONAGE_BRAND_NAME,
            "to": phone_number,
            "text": f"your code is: {token}",
        }
    )
    if responseData["messages"][0]["status"] == "0":
        print("Message sent successfully.")
    else:
        print(f"Message failed with error: {responseData['messages'][0]['error-text']}")
