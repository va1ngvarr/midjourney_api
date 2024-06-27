# midjourney_api

Midjourney unofficial API written in python

## Install
```
pip install midjourney-unofficial-api
```

## How to connect
You should go to discord server created by yourself where you have brought the Midjourney bot on. You'll need to generate any image with /imagine command in discord web-version and press F12. 

Go to Network tab. After image is generated you may see a line named "interactions". Click on it and choose Payload tab that should appear. Now, copy "channel_id", "application_id", "guild_id", "session_id", "version", "id" fields and save them somewhere.

Then move from Payload tab to Headers tab. Find the "authorization" key and, hence, save its value. When you have got all values you open "midjourney_config.json" file and insert values on the related keys.

## Documentation
How to use the library you may learn at "test.py" file. Config file that you have should be placed at the same directory with file that loads config

There is no complete documentation and surely won't be
