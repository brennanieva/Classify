
from twilio.rest import Client
#
# ACCOUNT_SID = 'AC3d7a4655023c4eef9f7147fdc4310b1a'
# AUTH_TOKEN = '917aabd65c59dd238a49ce37b7876254'



# client = Client(ACCOUNT_SID, AUTH_TOKEN)
# binding = client.notify.services('IS4d786f5156213da41357e85e63d69594') \
#     .bindings.create(
#         # We recommend using a GUID or other anonymized identifier for Identity
#         identity='00000001',
#         binding_type='sms',
#         address='+12538885523')
# print(binding.sid)

account_sid = 'AC3d7a4655023c4eef9f7147fdc4310b1a'
auth_token = '917aabd65c59dd238a49ce37b7876254'
client = Client(account_sid, auth_token)

message = client.messages.create(
                              from_='+12055256928',
                              body='Reminder to Move! Get up, Stretch, Drink Water',
                              to='+12538885523'
                          )

print(message.sid)
