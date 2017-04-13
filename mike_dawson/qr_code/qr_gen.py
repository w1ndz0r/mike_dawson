from PIL import Image, ImageDraw, ImageFont
import qrcode


list = []
stage = 'p1'
link = 'http://inv.fibo.loc/'

for i in range(3):
    i += 1
    list.append(stage+str(i).zfill(2))

for i in list:
    url = link+i
    file_name = i+'.png'

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image()

    with open(file_name, "wb") as file:
        width, height = img.size

        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype('arialbd.ttf', 24)
        textwidth, textheight = draw.textsize(i, font)

        # calculate the x,y coordinates of the text
        margin = 5
        x = (width - textwidth) / 2
        y = height - textheight - margin

        # draw watermark
        draw.text((x, y), i, font=font)
        img.save(file)