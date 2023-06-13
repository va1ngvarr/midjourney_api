# midjourney_api

You should go to discord created by yourself where you have brought the Midjourney bot on. Then you generate any image with /imagine command in discord web-version and press F12. 

## How to connect
Go to Network tab. After generation you may see line named "interactions". Press on it and choose Payload tab that should appear. Now copy "channel_id", "application_id", "guild_id", "session_id", "version", "id" values and save them somewhere.

Then move from Payload tab to Headers tab. Seek the "authorization" key and, hence, save its value. When you have got all values open "midjourney_config.json" file and insert values on the related keys.

## Documentation
How to use the library you may learn at "test.py" file. Config file that you have should be placed at the same directory with file that loads config

There is no complete documentation yet
