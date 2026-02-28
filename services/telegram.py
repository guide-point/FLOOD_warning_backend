import requests
import time
#endpoint to get the chat-id https://api.telegram.org/bot8688967737:AAEM7yp0xt_Go7xo4wC9iowo7KFEenVDfRA/getUpdates

token = "8688967737:AAEM7yp0xt_Go7xo4wC9iowo7KFEenVDfRA"

chat_ids = [
    1902518342,
    556677889,
    998877665,
]

message = "Warning: Flood expected in your area within the next 24 hours. Please take necessary precautions and stay safe."

for chat_id in chat_ids:
    response = requests.post(
        f"https://api.telegram.org/bot{token}/sendMessage",
        data={
            "chat_id": chat_id,
            "text": message,
        },
    )
    print(response.json())
    time.sleep(0.05)


