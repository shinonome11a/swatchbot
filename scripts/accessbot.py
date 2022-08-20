#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
import urllib.request
import os
import socket
import sys


# ここにslack webhookのURLを記入する
url_OK = ''
url_NG = ''




##############################################################################################
# DNS逆引き
def reverse_lookup(ip):
   try:
      return socket.gethostbyaddr(ip)[0]
   except:
      return False




if __name__ == "__main__":

   args = sys.argv
   if 2 > len(args):
      print('Invalid arguments')
      sys.exit(1)

   logtext = args[2]
   logtexts = logtext.split()
   url = ""
   color = ""
   reason = ""
   if args[1] == 'Y':
      url = url_OK
      color = "#2EB886"
      hostname = logtexts[3]
      username = logtexts[8]
      ipaddr = logtexts[10]
      port = logtexts[12]
   elif args[1] == 'N0':
      url = url_NG
      color = "#A30100"
      hostname = logtexts[3]
      username = logtexts[7]
      ipaddr = logtexts[9]
      port = logtexts[11]
      reason = " reason: Invalid user"
   elif args[1] == 'N1':
      url = url_NG
      color = "#A30100"
      hostname = logtexts[3]
      username = logtexts[10]
      ipaddr = logtexts[12]
      port = logtexts[14]
      reason = " reason: Failed publickey or password for invalid user"
   else:
      url = url_NG
      color = "#A30100"
      hostname = logtexts[3]
      username = logtexts[8]
      ipaddr = logtexts[10]
      port = logtexts[12]
      reason = " reason: Failed publickey or password"





   data = {
	"attachments": [
		{
        "fallback": hostname + " is received an SSH connection from " + ipaddr + "(" + str(reverse_lookup(ipaddr)) + ")",
        "color": color,
			"blocks": [
				{
					"type": "section",
					"text": {
						"type": "mrkdwn",
						"text": "System is received an SSH connection at " + hostname + reason + "."
					}
				},
				{
					"type": "divider"
				},
				{
					"type": "section",
					"fields": [
						{
							"type": "mrkdwn",
							"text": "*Remote IP Address*\n`" + ipaddr + "`"
						},
    						{
    							"type": "mrkdwn",
    							"text": "*Remote hostname*\n`" + str(reverse_lookup(ipaddr)) + "`"
    						},
						{
							"type": "mrkdwn",
							"text": "*Remote Port*\n`" + port + "`"
						},
						{
							"type": "mrkdwn",
							"text": "*Username*\n`" + username + "`"
						}
					]
				}
			]
		}
	]
   }

   headers = {
   'Content-Type': 'application/json',
   }
   req = urllib.request.Request(url, json.dumps(data).encode(), headers)
   with urllib.request.urlopen(req) as res:
      body = res.read()
      print(body)
