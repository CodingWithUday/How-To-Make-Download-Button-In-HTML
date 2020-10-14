import qrcode

#user input
a = input("Enter Your Data To Be Stored In Qrcode: ")
#data
dat = (a)

#File Name
file_name = "qrcode.png"

#generate qrcode
img = qrcode.make(data=dat)

#save Generated Qrcode
img.save(file_name)