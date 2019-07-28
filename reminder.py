

# import os
# import sched
# import time


#
from twilio.rest import Client

account_sid = 'AC3d7a4655023c4eef9f7147fdc4310b1a'
auth_token = '917aabd65c59dd238a49ce37b7876254'
client = Client(account_sid, auth_token)

message = client.messages.create(
                              from_='+12055256928',
                              body="Reminder to Move! Get up, go stretch, drink water",
                              to='+14797771344'
                          )

print(message.sid)
    # pass
    # time.sleep(60) #4hours
#
# while True:
#     sendSMS()
#
# from twilio.rest import Client
#
# ACCOUNT_SID = 'AC3d7a4655023c4eef9f7147fdc4310b1a'
# AUTH_TOKEN = '917aabd65c59dd238a49ce37b7876254'
#
# client = Client(ACCOUNT_SID, AUTH_TOKEN)
# notification = client.notify.services('ISXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX') \
#     .notifications.create(
#         to_binding='{"binding_type":"sms", "address":"+12538885523"}',
#         body='Knok-Knok! This is your first Notify SMS')
# print(notification.sid)

# credentials



# DELAY = 5
# DELAY_WEEK = 42
#
#
# def get_numbers():
#     number_array = []
#     message_object_array = client.messages.list()
#     for message in message_object_array:
#         if message.direction == 'inbound' and message.from_ not in number_array:
#             number_array.append(message.from_)
#     return number_array
#
#
#
#
# def welcome():
#     pass
#
#
#
# # def brag_log(scheduler):
# def brag_log():
#     msg_by_num = {}
#     for message in client.messages.list(): # array of all messages
#         # for each number, send most recent 7 messages (0-7 index)
#
#         if message.direction == 'inbound':
#             if message.from_ not in msg_by_num.keys():
#                 msg_by_num[message.from_] = []
#
#             # stores message in the number's array of messages
#             msg_by_num[message.from_].append(message.body)
#     print msg_by_num
#
#     for number, messages in msg_by_num.items():
#         messages = messages[0:7]
#         newline = "\n"
#         messages = newline.join(messages)
#         # emojis = u'\U0001f483 \U0001f451 \u2728 \U0001f3c6'.encode('unicode_escape')
#
#         client.api.account.messages.create(
#             to=number,
#             from_=os.environ["12055256928"],
#             body= "Reminder to Move! \n" + messages
#         )
#     # scheduler.enter(DELAY_WEEK, 1, brag_log(scheduler), (scheduler,))
#
#
# # s = sched.scheduler(time.time, time.sleep)
#
#
# def brag_reminder(numbers):
#     # send at certain time.
#     # send to all numbers stored.
#     for number in numbers:
#         client.api.account.messages.create(
#             to=number,
#             from_=os.environ["12055256928"],
#             body="Take a break! Get up, stretch, drink water!"
#         )
#     # scheduler.enter(DELAY, 1, brag_reminder(get_numbers(), scheduler), (scheduler,))
#
#
# brag_timer()
#
# # live credentials
# # account_sid = os.environ["TWILIO_SID"]
# # auth_token = os.environ["TWILIO_TOKEN"]
# # client = Client(account_sid, auth_token)
# #
# # message = client.api.account.messages.create(
# #     to=os.environ["BEC_NUMBER"],
# #     from_=os.environ["TWILIO_NUMBER"],
# #     body="Testing brag log heeeey"
# # )
