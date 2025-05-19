This is a quick & dirty demo of implementing the webex_bot pip package to create a simple WebEx chatbot 
that can respond to messages in a WebEx Teams space.

## Prerequisites
You'll need to supply a .env file in the root dir of this project with a couple of environment variables the bot will use:

BOT_TOKEN: The bot's access token. You can create one of these or just get this from me (marchaye)  
APPROVED_USER_IDS: A list of user IDs that the bot can interact with. See [WebEx API for getting own user ID](https://developer.webex.com/messaging/docs/api/v1/people/get-my-own-details) to get your own ID  
APPROVED_ROOM_IDS: A list of room IDs that the bot can interact with. See [WebEx API for getting room IDs](https://developer.webex.com/messaging/docs/api/v1/rooms/list-rooms) to get the room IDs   

## Running
To run the bot, simply run the following command in your terminal:

```bash
pip install -r requirements.txt
python main.py
```