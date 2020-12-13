[![Build Status](https://travis-ci.com/Rubber-Duck-LTD/RubberDucksDiscordBot.svg?branch=main)](https://travis-ci.com/Rubber-Duck-LTD/RubberDucksDiscordBot)
![workflow_name](https://github.com/Rubber-Duck-LTD/RubberDucksDiscordBot/workflows/Python%20application%20-%20DiscordBot,%20Rubber%20Ducks%20Ltd,%20testing/badge.svg)
![GitHub top language](https://img.shields.io/github/languages/top/Rubber-Duck-LTD/RubberDucksDiscordBot)

## NOTE:
Tests will pass and work properly when the API-keys are inputted to the code (.env-files) - more information below at the Develop-section.


<details open="open">
  <summary>Content</summary>
  <ol>
     <li><a href="#discordbot">Project</a></li>
      <li><a href="#technologies">Technologies</a></li>
      <li><a href="#libraries">Libraries</a></li>
      <li><a href="#commands">Commands</a></li>
        <li><a href="#functions">Functions</a></li>
    <li><a href="#develop">Develop</a></li>
    
    
  </ol>
</details>




# DiscordBot
This is a Discord Bot project that we built for our Programmingproject course II at Haaga-Helia. Our goal was to build a bot that is compatible with the discord environment and its purpose would be to help students of Haaga-helia. 

The bot excecutes a set of useful commands for students. The main idea is that the bots would ease or fasten students studying experience in discord environment/server. 


## Technologies
* [Python3](https://www.python.org/downloads/)
* [Discord development portal](https://discord.com/developers/docs/intro) 
* [Discord](https://discord.com/) 
* [Azure](https://azure.microsoft.com/en-us/features/azure-portal/)
* [Travis CI](https://travis-ci.com/)
* [Docker](https://www.docker.com/)
* [Visual Studio Code](https://code.visualstudio.com/download)
* [Oracle VM](https://www.virtualbox.org/)

## Libraries 

* discord.py
```sh
Linux/macOS
python3 -m pip install -U discord.py

Windows
py -3 -m pip install -U discord.py
```
 
* googlemaps
```sh
pip install -U googlemaps 
```

* python-dotenv 
```sh
pip install -U python-dotenv
```

* requests 
```sh
python -m pip install requests
```

* urrlib3 
```sh
python -m pip install urllib3
```

Notice! In our project we used [Google Platform's](https://console.developers.google.com/apis/dashboard?project=vivid-cache-290908&hl=fi) encrypted Api-Keys and [Mapquest API's](https://www.mapquest.com/) Keys. So if you want to clone/download our code you need to inhabit the .env file with your own api keys.

In the .env file should also be added DISCORD_TOKEN=*insert discord token* and DISCORD_GUILD=*insert discord guild*  so that the bot can connect to your desired server. 


## Commands

Notice! The commands need to be written exactly right and the command can't contain any other unnesecary content whatsoever or the bot doesn't function right. And the command needs to start with a Prefix. For example in our project we used "-" as our prefix and the correct way to exploit a command would be "-help".

User gets notices from incorrect inputs. 


## Functions:


### Covid-19

Command call: -covid, -c, -cov (and alternatively country, For example: "-c Finland") 

Shows information about the covid-19 virus globaly or by country.


### Google Map Picture

Command call: -map

Sends a picture from google maps to the user of a desired location.

### Google Places

Command call: -places

Shows five (5) closest restaurants from users spesified location.

### Google Traveltime

Command call: -distance, -dist

Tells the estimated travel time and distace of users spesified locations. 

### Haaga-Helia (info)

-Moodle	- link

-Kide	- link

-MyNet	- link

-Lukkari	- link

## Bistro

Command call: -bistro (one day), -bistro week (week)

Shows the menu of Pasila campus bistro. Can be narrowed down to current day or to a week.


### Helsinki Events

Command call: -events

Tells the user the five (5) closest events in Helsinki at users spesified location. Command also shows information about the event like description and event photo.



### HSL

Command call: -hsl

=======
### Route Planning
>commands: **-route** OR **-rt**
>
>User is able to recieve information about a trip from point A to point B.
>
>### Usage
>Use spaces **ONLY** to **separate** the **prefix** (-route or -rt), the **origin** and the **destination** from each other.  
>**e.g. -route [origin] [destination]**
>
>Use "-" instead of a space when writing address numbers  
>**e.g. -route valtimotie-3,vantaa jätkäsaari**
>
>Use "," to add address details to origin or destination  
>**e.g. -route valtimotie-3,vantaa jätkäsaari**
>
>The module also accepts Points of Interest as an origin or a destination  
>**e.g. Shopping Centers**
>
>### Examples
>-route valtimotie-3,vantaa jätkäsaari  
>-rt gigantti,tammisto itäkeskus  
>-route helsinki vantaa  

### How to add the bot to your discord server

Click the following link:
https://discord.com/api/oauth2/authorize?client_id=750282686656151642&permissions=0&scope=bot

* Sign in to discord.
* Select a server in which you want to add the bot
(Note that you have to have the rights to add bots into servers)
* Click Authorize.

Now the bot is added to the server and you can start by typing the -help command.

### Help
Command call: -help

Sends the user a private message of the functins and commands and instructions how to use them.






Example of the “-help” command.

Sent message:

![Image of msg](https://i.imgur.com/I69abYy.png)

Bots reply as a private message:

![Image of response](https://i.imgur.com/qv5ckHg.png)


## Develop:

If you want to develop this project further or add some functionalities (modules) to this bot, here is an easy way:
<ol>
<li>Clone this repo to your local machine. "git clone [ADDRESS]". </li>
  <li>Change the remote repository to your own remote repository ("git remote -v" can help you to determine the current repository; also, forking can be done if needed). </li>
  <li>Add more modules to the path: /src/components/cogs/ and follow the structure provided in the other modules (e.g. self, parameters, etc). An example: /src/components/cogs/NewFooBarModule.  </li>
  <li>Add initializing settings for the new module in the connection.py-file located at /src/components/connection.py. Follow the cogs-initialized structure. </li>
  <li>Change the two .env-files located at the test_modules-folder and at the root of this project to contain your own API-keys. </li>
  <li>Finally, one can run the bot LOCALLY from the terminal by inputting python3 connection.py at the correct folder that is /src/components/. </li>
  <li>Happy coding! </li>
  </ol>
