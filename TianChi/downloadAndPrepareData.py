import os

def unzipto(src, dst):
    mkdir(dst)
    os.system("unzip %s -d %s"%(src, dst))

def wget(url):
    os.system('wget %s'%(url))

def mkdir(path):
    if not os.path.exists(path):
        os.mkdir(path)

def download():
    urlbase = "http://tianchi-media.oss-cn-beijing.aliyuncs.com/231711_youku/round1/train/"

    for lr in ["youku_00000_00049_l.zip", "youku_00050_00099_l.zip", "youku_00100_00149_l.zip"]:
        if not os.path.exists(lr):
            print("download %s"%lr)
            wget(urlbase + "input/" + lr)
        else:
            print("%s is exists"%lr)

    for GT in ["youku_00000_00049_h_GT.zip", "youku_00050_00099_h_GT.zip", "youku_00100_00149_h_GT.zip"]:
        if not os.path.exists(GT):
            print("download %s"%GT)
            wget(urlbase + "label/" + GT)
        else:
            print("%s is exists"%GT)

def unzip():
    # for folder in ["l", "h_GT"]:
    for folder in ["l"]:
        for subData in ["00000_00049_", "00050_00099_", "00100_00149_"]:
            unzipto("youku_" + subData + folder + ".zip", folder)

def y4m2bmp():
    # for folder in ["l", "h_GT"]:
    for folder in ["l"]:
        for videoId in range(150):
            y4mfile = "Youku_%05d_%s"%(videoId, folder)
            mkdir(folder + "/" + y4mfile)
            print(y4mfile)
            os.system("ffmpeg -i " + folder + "/" + y4mfile + ".y4m  -vsync 0 " + folder + "/" + y4mfile + "/%3d.bmp -y")




download()
# unzip()
y4m2bmp()
