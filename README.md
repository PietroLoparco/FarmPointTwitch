# FarmPointTwitch
Small "bot" in python, which redeems the chest points on twitch every time it appears

# How set up the bot
- clone the repo with: ```git clone <Repo URL>```
- Download Python
- install selenium via ```pip```
- Create your settings file by changing the variables:
```
CONTROL = "twitch page selector which can ensure that the page is open"
LINK = "Link of the twitch channel you want to redeem points to"
TIME = "Interruption time between one check and another"
BUTTON_CHEST = '#live-page-chat > div > div > div > div > div > section > div > div.Layout-sc-nxg1ff-0.fwjUjn.chat-input > div:nth-child(2) > div.Layout-sc-nxg1ff-0.ejhEzS.chat-input__buttons-container > div.Layout-sc-nxg1ff-0.cwwMDL > div > div > div > div.Layout-sc-nxg1ff-0.Aqzax > div > div > div > button' (This is a selector of button chest)
```
- Run the bot with: ```py index.py```

## For every bug/problem or new feautures open a new issue
