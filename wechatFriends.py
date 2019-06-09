import itchat
import sys
from  collections import Counter
import numpy as np
import tkinter
#from tkinter import mainloop
import matplotlib.pyplot as plt

#log in wechat
itchat.auto_login(hotReload = True)
friends = itchat.get_friends(update = True)

def analyseSex(firends):
    sexs = list(map(lambda x:x['Sex'], friends[1:]))
    counts = list(map(lambda x:x[1], Counter(sexs).items()))
    labels = ['Unknow','Male','Female']
    colors = ['red','yellowgreen','lightskyblue']
    explode = [0, 0, 0.1]

    plt.figure(figsize=(8,5), dpi=80)
    plt.axes(aspect=1)              # set this, Figure is round, otherwise it is an ellipse
    plt.pie(x=counts,                 #性别统计结果
            labels = labels,          #性别展示标签
            explode = explode,       # 0.1 突出这部分
            colors = colors,          #饼图区域配色
            labeldistance = 1.1,    #标签距离圆点距离，1.1倍半径
            autopct = '%3.1f%%',    #饼图区域文本格式
            shadow = True,         #饼图是否显示阴影
            startangle = 90,        #饼图起始角度
            pctdistance = 0.6       #饼图区域文本距离圆心距离
    )
    plt.legend(loc='upper right',)  #图例位置    
    plt.title(u'%s的微信好友性别组成' % friends[0]['NickName'])
    plt.show()

analyseSex(friends)

def analyseHeadImage(frineds):
    # Init Path
    basePath = os.path.abspath('.')
    baseFolder = basePath + '\\HeadImages\\'
    if(os.path.exists(baseFolder) == False):
        os.makedirs(baseFolder)

    # Analyse Images
    faceApi = FaceAPI()
    use_face = 0
    not_use_face = 0
    image_tags = ''
    for index in range(1, len(friends)):
        friend = friends[index]
        # Save HeadImages
        imgFile = baseFolder + '\\Image%s.jpg' % str(index)
        imgData = itchat.get_head_img(userName = friend['UserName'])
        if(os.path.exists(imgFile) == False):
            with open(imgFile,'wb') as file:
                file.write(imgData)

        # Detect Faces
        time.sleep(1)
        result = faceApi.detectFace(imgFile)
        if result == True:
            use_face += 1
        else:
            not_use_face += 1 

        # Extract Tags
        result = faceApi.extractTags(imgFile)
        image_tags += ','.join(list(map(lambda x:x['tag_name'], result)))

    labels = [u'使用人脸头像', u'不使用人脸头像']
    counts = [use_face, not_use_face]
    colors = ['red', 'yellowgreen', 'lightskyblue']
    plt.figure(figsize=(8,5), dpi=80)
    plt.axes(aspect=1) 
    plt.pie(counts,                 #性别统计结果
            labels=labels,          #性别展示标签
            colors=colors,          #饼图区域配色
            labeldistance = 1.1,    #标签距离圆点距离
            autopct = '%3.1f%%',    #饼图区域文本格式
            shadow = False,         #饼图是否显示阴影
            startangle = 90,        #饼图起始角度
            pctdistance = 0.6       #饼图区域文本距离圆点距离
    )
    plt.legend(loc='upper right',)
    plt.title(u'%s的微信好友使用人脸头像情况' % friends[0]['NickName'])
    plt.show() 

    image_tags = image_tags.encode('iso8859-1').decode('utf-8')
    back_coloring = np.array(Image.open('face.jpg'))
    wordcloud = WordCloud(
        font_path='simfang.ttf',
        background_color="white",
        max_words=1200,
        mask=back_coloring, 
        max_font_size=75,
        random_state=45,
        width=800, 
        height=480, 
        margin=15
    )

    wordcloud.generate(image_tags)
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.show()