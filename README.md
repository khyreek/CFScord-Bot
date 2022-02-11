# Codeforces-Discord-Bot
Discord bot that crops and posts any specified, or unspecified codeforce problem with crisped corners to discord on command. Created to solve codeforce problems with friends on a commonly used social media platform, without the need to coordinate steps before starting discussions or problem-solving.

## Setup
This was written while using Chrome, so driver installations are Chrome-based
1. Run in command prompt: `pip install selenium beautifulsoup4, discord.py, python-opencv, numpy, webdriver-manager`
2. Add your discord bot token in `src/discordbot.py` in place of `YOUR TOKEN HERE` ['here'](https://github.com/khyreek/CFScord-Bot/blob/master/src/discordbot.py#L79)  
3. Open project in text editor and run `DiscordBot.py` in `CodeforcesDiscordBot`
And now the bot will be working in all servers!

## Features/Commands
`cf p [codeforce_problem_code]`
Sends the codeforce problem requested given the problem code, the code includes contest number prefix, and alphabetical postfix, ex. `cf p 1540A`, `cf p 1431E`

`cf random`
Sends a rand codeforce problem beginning from the first problem in codeforces history, demonstration; `cf rand`

`cf filt [minimum_rating] [maximum_rating] (optional)[filters]`  
Filters through the given requests and finds a random codeforces problem fitting those requirements, ex. `cf filt 800 1200 data-structures`, `cf filt 1500 2000 bitmasks hashing`
 
`$subm [codeforce_problem_code]`
Sends a link to the codeforce page with submission space scrolled-to and highlighted, ex. `cf subm 1546E`; outputs: `https://codeforces.com/problemset/problem/1546/E#:~:text=%E2%86%92%20Submit%3F,Submit`

## Demonstration
https://user-images.githubusercontent.com/69024184/134733513-fddafb1f-e088-4868-9ce6-6dad3a90cd30.mp4

