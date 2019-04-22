import numpy as np
import cv2

### マーカーの設定

marker_dpi = 800 # 画面解像度(マーカーサイズ)
scan_dpi = 720 # スキャン画像の解像度

# グレースケール (mode = 0)でファイルを読み込む
marker=cv2.imread('anal1.jpeg',0)

# マーカーのサイズを取得
w, h = marker.shape[::-1]

# マーカーのサイズを変更
marker = cv2.resize(marker, (int(h*scan_dpi/marker_dpi), int(w*scan_dpi/marker_dpi)))

### スキャン画像を読み込む
img = cv2.imread('asss-1.jpeg',0)

res = cv2.matchTemplate(img, marker, cv2.TM_CCOEFF_NORMED)

threshold = 0.4
loc = np.where( res >= threshold)

mark_area = {}
mark_area['top_x']= min(loc[1])
mark_area['top_y']= min(loc[0])
mark_area['bottom_x']= max(loc[1])
mark_area['bottom_y']= max(loc[0])

img = img[mark_area['top_y']:mark_area['bottom_y'],mark_area['top_x']:mark_area['bottom_x']]

n_col = 2 # 1行あたりのマークの数

n_row = 20 # マークの行数
margin_top = 1 # 上余白行数
margin_bottom = 1 # 下余白行数

n_row = n_row + margin_top + margin_bottom # 行数 (マーク行 7行 + 上余白 3行 + 下余白 1行)

img = cv2.resize(img, (n_col*100, n_row*100))

### ブラーをかける
img = cv2.GaussianBlur(img,(5,5),0)

### 50を閾値として2値化
res, img = cv2.threshold(img, 50, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)

### 白黒反転
img = 255 - img

cv2.imwrite('tunaki.png',img)

### 結果を入れる配列を用意
result = []

### 行ごとの処理(余白行を除いて処理を行う)
for row in range(margin_top, n_row - margin_bottom):

    ### 処理する行だけ切り出す
    tmp_img = img [row*100:(row+1)*100,]
    area_sum = [] # 合計値を入れる配列

    ### 各マークの処理
    for col in range(n_col):

        ### NumPyで各マーク領域の画像の合計値を求める
        area_sum.append(np.sum(tmp_img[:,col*100:(col+1)*100]))

    ### 画像領域の合計値が，中央値かどうかで判断
    result.append(area_sum > np.median(area_sum) * 1)

for x in range(len(result)):
    res = np.where(result[x]==True)[0]+1
    if len(res)>1:
        print('Q%d: ' % (x+1) +str(res)+ ' ## 複数回答 ##')
    elif len(res)==1:
        print('Q%d: ' % (x+1) +str(res))
    else:
        print('Q%d: ** 未回答 **' % (x+1))
