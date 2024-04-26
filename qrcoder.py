import qrcode

img = qrcode.make('https://masterbarbermag.com/')
img.save('pythonsbarber.jpg')

img = qrcode.make('Learn Python it is the Best language')
img.save('learnPy')