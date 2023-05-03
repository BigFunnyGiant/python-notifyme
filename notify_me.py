#!/usr/bin/env python3

import argparse
import json
import requests

parser = argparse.ArgumentParser(description='Send a notification using Notify Me API')
parser.add_argument('message', metavar='MESSAGE', type=str,
                    help='the message to send')
parser.add_argument('--api-key-file', metavar='API_KEY_FILE', type=str, default='api_key.txt',
                    help='the path to the file containing the Notify Me API key')
args = parser.parse_args()

with open(args.api_key_file, 'r') as f:
    api_key = f.read().strip()

body = json.dumps({
    "notification": args.message,
    "accessCode": api_key
})

response = requests.post(url="https://api.notifymyecho.com/v1/NotifyMe", data=body)
print(response.text)
