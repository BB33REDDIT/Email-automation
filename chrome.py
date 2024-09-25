import yagmail
import os
from dotenv import load_dotenv

load_dotenv()




sender = "BOSSBABY33REDDIT@gmail.com"
receiver = "pranavdinakar24@gmail.com"
subject = 'Test mail using python'
contents = '''
No context frr
'''
yag = yagmail.SMTP(user=sender,password=os.getenv('PASSWORD'))
yag.send(to=receiver, subject=subject, contents=contents)
print("Email send!")