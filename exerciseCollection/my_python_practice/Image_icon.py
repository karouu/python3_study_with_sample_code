'''
将你的 QQ 头像（或者微博头像）右上角加上红色的数字，类似于微信未读信息数量那种提示效果。
'''


from PIL import Image,ImageFont,ImageDraw

num = '666'
font = ImageFont.truetype("/home/matter/Pictures/msyh.ttf",10)

img = Image.open('/home/matter/Pictures/linux_org.jpg')
width,height = img.size

draw = ImageDraw.Draw(img)

draw.text( (width-height,0),num,fill="green",font=font)
img.save("/home/matter/Pictures/p2_out.jpg")
