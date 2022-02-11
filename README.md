# Codeforces-Discord-Bot
Discord bot that crops and posts any specified, or unspecified codeforce problem with crisped corners to discord on command. Created to solve codeforce problems with friends on a commonly used social media platform, without the need to coordinate steps before starting discussions or problem-solving.

# Setup
This was written while using Chrome, so driver installations are Chrome-based
1. Run in command prompt: `pip install selenium beautifulsoup4, discord.py, python-opencv, numpy, webdriver-manager`
2. Add your discord bot token in `src/discordbot.py` in place of `YOUR TOKEN HERE` ['here'](https://github.com/khyreek/CFScord-Bot/blob/master/src/discordbot.py#L79)
   
4. Create a discord bot in your discord developer panel, and paste your discord bot token in your already-created `.env` file
5. Open project in text editor and run `DiscordBot.py` in `CodeforcesDiscordBot`

Use `https://discord.com/api/oauth2/authorize?client_id=885209720590303232&permissions=8&scope=bot` to invite the bot to your server  
After that, you're good to go


# Features/Commands
<ins>cf p [codeforce_problem_code]</ins>
Sends the codeforce problem requested given the problem code, the code includes contest number prefix, and alphabetical postfix, ex. `cf p 1540A`, `cf p 1431E`

<ins>cf random</ins>
Sends a rand codeforce problem beginning from the first problem in codeforces history, demonstration; `cf rand`

<ins>cf filt [minimum_rating] [maximum_rating] (optional)[filters]</ins>  
Filters through the given requests and finds a random codeforces problem fitting those requirements, ex. `cf filt 800 1200 data-structures`, `cf filt 1500 2000 bitmasks hashing`
 
<ins>$subm [codeforce_problem_code]</ins> 
Sends a link to the codeforce page with submission space scrolled-to and highlighted, ex. `cf subm 1546E`; outputs: `https://codeforces.com/problemset/problem/1546/E#:~:text=%E2%86%92%20Submit%3F,Submit`

 
# Demonstration
https://user-images.githubusercontent.com/69024184/134733513-fddafb1f-e088-4868-9ce6-6dad3a90cd30.mp4

