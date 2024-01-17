#連線,並檢查內線狀態資訊
#status=0,1,2正在連線
#tatus=3連線成功
#tatus<0沒有這個wifi機地台



import time
import network

ssid = 'FamilyC'
password = 'q6msz6qz'

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(ssid, password)


max_wait = 10
while max_wait > 0:
    status = wlan.status()
    if status < 0 or status >= 3:
        break
    max_wait -= 1
    print("等待連線")
    time.sleep(1)

#處理錯誤
if wlan.status() != 3:
    raise RuntimeError('連線失敗')
else:
    print('連線成功')
    status = wlan.ifconfig()
    print(f'ip={status[0]}')