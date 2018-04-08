import urllib.request
import time
for i in range (100):
    a = input("請輸入此素材的名稱，全部小寫，不能多打任何一個字元，包括空格，且請切換到半形：\n")
        print("現在時間是{}，現在我正在下載{}的素材，請稍等".format(time.strftime("%H:%M:%S"),a))
        urllib.request.urlretrieve("https://templated.co/{}/download".format(a),"{}.mp4".format(a))
hhh = input("quit?")
if (hhh == y):
    quit()
else:
    quit()
    
