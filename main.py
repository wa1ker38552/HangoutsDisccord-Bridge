from alive import keepAlive
from replit import db
import requests
import hangups
import os

user_data = {'id': 'name'}

def get_chat_contents(id):
  with open('LOG', 'r') as file:
    data = file.read().split('\n')
  
    text_raw = []
    for i, line in enumerate(data):
      if 'event_notification' in line:
        raw_string = [item.strip() for item in data[i:i+43]]

        '''
        # object debug
        for i, item in enumerate(raw_string):
          print(i, item)
        '''
          
        if raw_string[3].replace('id: "', '').replace('"', '') == id:
          if 'text: ' in raw_string[22]:
            message = raw_string[22].replace('text: "', '').replace('"', '')
          else:
            message = raw_string[21].replace('text: "', '').replace('"', '')
          text_raw.append({
            'user': raw_string[7].replace('chat_id: "', '').replace('"', ''),
            'time': raw_string[9].replace('timestamp: ', ''),
            'message': message
          })
  return text_raw

# only for debug
'''
# print pre-loaded messages
for item in get_chat_contents('chat_id'):
  print(f'{item["time"]}: {item["message"]}')
'''

keepAlive()
print('Reading messages!')

while True:
  content = get_chat_contents('chat_id')

  # checks for new message
  if content[len(content)-1]['message'] != db['last_message']:
    db['last_message'] = content[len(content)-1]['message']
    requests.post(os.environ['WEBHOOK'], json={
      "content" : content[len(content)-1]["message"],
      "username" : user_data[content[len(content)-1]["user"]]
    })
        
