# Discord Bot for Uploading & Using GIF Emotes
The idea is to make use of a bot to bypass discord limitations of animated emotes on a Nitro-less account.
The method has some downsides listed at the end but it is an okay solution to using them gifs.

Makes use of two separate Python containers:
1. For the Discord bot, which interacts through Discord's interactions API
2. For an API with FastAPI, that the bot can make calls against

Also, makes use of an Nginx container for reverse proxy.

## Initial Setup:
1. Add your discord bot token to ./Volumes/DiscordBot/token.txt
2. Run: docker compose up
3. Test the discord bot on your private server

Note:
It is necessary to build the docker images in between changes when testing the app as a whole with: 
docker compose up --build

## Demo 
API: https://prabeshgiri.com.np/api/v1/huehuebot/docs
Discord Bot: https://discord.com/oauth2/authorize?client_id=1226780853351481376&permissions=414464727104&integration_type=0&scope=bot

Bot Commands:
'huetake [gif file]' : Records the gif file through the API
'huehue [gif filename]' : Displays a recorded gif file in chat. Extension should be ignored in provided filename.

## Ending Thoughts:
The disadvantage of using such an approach vs just using emojis with Nitro or tenor/other gif keyboard is that it leaves user messages intact.
It is not possible to edit the user's message even with admin permissions are user messages are read only for the bot.
The other issue is latency, but it is less pronounced for smaller gifs.
Adding MongoDB to record user info and having a more private chat contexts to complement that is something that should be explored.
