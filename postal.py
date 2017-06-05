import requests
import json
import os

class Client:
    def __init__(self):
        self.host = "https://postal.cooperstanbury.com"
        try:
            self.serverKey = os.environ['POSTAL_KEY']
        except:
            self.serverKey = ''
            print "Failed to get postal key from environ"

    def make_request(self, action, parameters):
        url = '%s/api/v1/send/%s' % (self.host, action)

        headers = {
            'x-server-api-key': self.serverKey,
            'content-type': 'application/json',
        }

        response = requests.post(url, headers=headers, data=json.dumps(parameters))
        return response.json()

    def send_message(self, subject="", to_address=[], from_address="", headers=[], html="", text="", reply_to="", sender="", tag=""):
        attributes = {}        

        if to_address:
            attributes['to'] = []
            for email in to_address:
                attributes['to'].append(email)

        if from_address:
            attributes['from'] = from_address
        
        if sender:
            attributes['sender'] = sender

        if subject:
            attributes['subject'] = subject

        if tag:
            attributes['tag'] = tag

        if reply_to:
            attributes['reply_to'] = reply_to

        if text:
            attributes['plain_body'] = text
        
        if html:
            html_content = ""
            with open(html, 'rU') as content_file:
                html_content = content_file.read()

            attributes['html_body'] = html_content

        if headers:
            attributes['headers'] = {}
            for i in headers:
                attributes['headers'][i] = headers[i]

        return self.make_request('message', attributes)
