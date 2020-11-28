# -*- coding: utf-8 -*-
"""line_bot2

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1eCMvPvN1UroR0YTWOdVwq6cUueXOGVg8
"""

from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage
import pya3rt

app = Flask(__name__)

linebot_api = LineBotApi("oIWHAgdvl+ugiXkx1nelw4YWABYBJKTh4UL5RwR7Oy7F0ZmkYIb0f\
niZ1kRCTHNoTQK/3H39AuGNC9fKLSiJS3DP1KeqHSrP/jS0B0bNZFfdBuBIDiZIDskXDtXv/7I3Mkih\
tyI5bxnZaN4ibXbXsQdB04t89/1O/w1cDnyilFU=")

handler = WebhookHandler("da1e70e9faaf2cd9bcda664e4580b9bb")

@app.route("/callback",methods=['POST'])

def callback():
  signature = request.headers["X-Line-Signature"]
  body = request.get_data(as_text=True)

  try:
    handler.handle(body, signature)
  except InvalidSignatureError:
    abort(400)

  return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
  ai_message = talk_ai(event.message.text)
  linebot_api.reply_message(event.reply_token, TextSendMessage(text=ai_message))

def talk_ai(word):
  apikey = "DZZqaZrOeILbmDft7pJSj0lOf4ruYnJ9"
  client = pya3rt.TalkClient(apikey)
  reply_message = client.talk(word)
  return reply_message['results'][0]['reply']

if __name__ == '__main__':
  app.run()
