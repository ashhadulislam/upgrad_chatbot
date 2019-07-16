# UpGrad Chatbot for restaurant search

[![N|Solid](https://cldup.com/dTxpPi9lDf.thumb.png)](https://nodesource.com/products/nsolid)
### Introduction

This bot searches for restaurants and gives them to us as a list

Some examples are as follows:
```
User: Hi
Bot: Hi there! How may I help you?
User: Can you suggest some good restaurants in kolkata 
Bot: What kind of cuisine would you like to have?
1. Chinese 2. Mexican 3. Italian
4. American 5. Thai
6. North Indian
User: american
Bot: What's the average budget for two people?
1. Lesser than Rs. 300 2. Rs. 300 to 700
3. More than 700
User: <300
Bot: Showing you top rated restaurants:
1. Restaurant 1 in Area 1. And the average price for two people here is: XXX Rs
2. Restaurant 1 in Area 1. And the average price for two people here is: XXX Rs
3. .
4. .
5. .
Bot: Should I send you details of all the restaurants on email? User: yes. Please
Bot: To what email id should I send it to?
User: jddk.2jmd@kdl.co.in
Bot: Sent. Bon Appetit!
```


### Installation

Download this repo and cd into the folder

Install the dependencies
```sh
$ pip install -r requirements.txt
```
Install the spacy en library
```sh
$ python -m spacy download en
```

### Training the RASA 

In order to train the interpreter, run the following command

```sh
$ python -m rasa_nlu.train -c nlu_config.yml --data data/data.json -o models --fixed_model_name nlu --project current --verbose
```

In order to train RASA CORE, run the following command

```sh
$ python -m rasa_core.train -d domain.yml -s data/stories.md -o models/current/dialogue -c policies.yml
```

### Running the RASA on commandline

In order to run rasa action server, execute
```sh
$ python -m rasa_core_sdk.endpoint --actions actions
```


In order to run rasa at commandline, execute
```sh
$ python -m rasa_core.run -d models/current/dialogue -u models/current/nlu --endpoints endpoints.yml
```

### Running the RASA on GUI
First, run a small flask server to get the GUI
```sh
$ cd chat_interface
$ python deploy.py
```
This will run flask server with a chat window that can be accessed by visiting
http://localhost:5090

Next get the rasa action server up and running
```sh
$ python -m rasa_core_sdk.endpoint --actions actions
```

Next run rasa as a simple server
```sh
$ python -m rasa_core.run --enable_api -d models/current/dialogue -u models/current/nlu -o out.log --endpoints endpoints.yml
```

Now if you go to your browser and open http://localhost:5090, a chat window will pop up and you can converse with the bot.


### Running the RASA on Slack

Set up slack as mentioned here

https://www.youtube.com/watch?v=xu6D_vLP5vY

Also check out this blog for more clarity 

https://towardsdatascience.com/building-a-conversational-chatbot-for-slack-using-rasa-and-python-part-2-ce7233f2e9e7

First get the rasa action server up and running
```sh
$ python -m rasa_core_sdk.endpoint --actions actions
```

Next run the app which will handle slack messages
```sh
$ python run_app.py
```

Create the ngrok tunneling as mentioned in the video/blog post mentioned above.
Open slack and you're good to go.
