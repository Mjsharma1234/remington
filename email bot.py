import smtplib
server=smtplib.SMTP('smtp.gmail.com',587)
server.startls()
server.login('sharmamrituyanjay@gmail.com','mrituyanjay@123')
server.sendmail('sharmamrituyanjay@gmail.com',
                'sharmalavi253@gmail.com',
                'hey this is an automated reply created by a mastermind')