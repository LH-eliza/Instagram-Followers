import json 
with open('followers.json') as file:
    followers_json = json.load(file)

with open('following.json') as file:
    following_json = json.load(file)

with open('pending_follow_request.json') as file: 
    pending_follow_request.json = json.load(file)
