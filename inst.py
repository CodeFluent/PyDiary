import smtplib

fromaddr= 'python@gmail.com'
toaddrs= 'wasfimomenwim@gmail.com'
msg = 'PyDiary Here!'
subject='Your Daily Email Reminder'

username='wasfimomenwim'
password='gestalt1'

server= smtplib.SMTP("smtp.gmail.com:587")

server.starttls()

server.login(username,password)


server.sendmail(fromaddr, toaddrs, msg)

server.quit()


