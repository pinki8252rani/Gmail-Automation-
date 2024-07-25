import smtplib as s

ob=s.SMTP("smtp.gmail.com",587)
ob.ehlo()
ob.starttls()
ob.login("pinkirani841215@gmail.com","pinki1234567")
subject="test python "
body="I Love Python"
massage="subject:{}\n\n{}".formate(subject,body)
listadd=["ranipinki8252@gmail.com","ritik7282kumar@gmail.com"]
ob.sendmail("pinkirani841215@gmail.com",listadd,massage)
print("send mail")
ob.quit()