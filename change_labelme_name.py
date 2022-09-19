import os 

darpath =  "D:/jo/Unet-Segmentation-Pytorch-Nest-of-Unets-master/fishdata/bbox/data_fish/"#object file
savelabeldir = "D:/jo/Unet-Segmentation-Pytorch-Nest-of-Unets-master/fishdata/bbox/label/"#save file


for x in os.listdir(darpath):
    print(x)
    #去掉標點符號後暫存
    characters = "%"
    string = ''.join( i for i in x if i not in characters)
    print(string)
    for o in os.listdir(darpath + x):
        #進入資料夾找label
        if o == "label.png":
            oldname = darpath + x + "/" + o
            newname = savelabeldir + string + ".png"
            print(oldname,newname)
            print("found it!!")
            #更改label名後存入label資料夾
            os.rename(oldname,newname)