#!/usr/bin/env python3

# ライブラリのインポート
import cv2

# 画像を読み込む
image = cv2.imread("banana.jpg")

# 円の中心をどこにするか決める（x座標のピクセル, y座標のピクセル）
center = (300, 300)

# 円の大きさ（半径）を決める（数字を大きくすると円が大きくなる）
radius = 100

# 線の太さを決める（数字を大きくすると太くなる）
thickness = 10

# 線の色を決める（青, 緑, 赤）
color = (0, 0, 0)

# cv2.circleという関数を使って、画像の中に円を描画する
cv2.circle(image, center, radius, color, thickness, cv2.LINE_AA)

# 円が追加された画像を保存する
cv2.imwrite("circle_banana.jpg", image)
print("画像を加工して保存しました。")

# 画像を表示
cv2.imshow("Banana", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
