from firebase import Firebase

instance = Firebase()

# response = Firebase.create_user("918780495805", "Parth Panchal")
response = Firebase.update_user("918866224546", "resume", {"id": "407257911455315", "name": "Pratik-TL.pdf"})
# response = Firebase.get_user_data("917227856454")
# response = instance.delete_data("918780495804")
print(response)
#

import json
# import requests
#
# import constants
#
# response = requests.get(
#     url="https://graph.facebook.com/v13.0/407257911455315",
#     headers=constants.header,
# )
# url = response.json()['url']
#
# file = requests.get(url, headers=constants.header)
# # with open('resume.pdf', 'w') as f:
# open('resume.pdf', 'wb').write(file.content)

