from PIL import Image 

# 画像のファイルパスを指定して画像を開く 

image_path = "./resource/resize_rotate.jpg" 

image = Image.open(image_path) 

# 画像の幅と高さを取得 

width, height = image.size 

# 画像のピクセルデータを出力 

print("Image Width:", width) 

print("Image Height:", height) 

# 画像の基本情報を取得 

image_info = { 

    "ファイル名": image.filename, 

    "形式": image.format, 

    "画像のサイズ(width)": width, 

    "画像のサイズ(height)": height, 

    "カラーモード": image.mode, 

    "画像のモード": image.getbands(),  # カラーモードの各バンド（R, G, Bなど）をリストとして返す 

    "透明度の有無": image.info.get("transparency"),  # 画像に透明度がある場合は透明度の値が返される 

} 

# 画像の基本情報を出力 

for key, value in image_info.items(): 

    print(f"{key}: {value}")
 
left = int(2100)
upper = int(1500)
right = int(2500)
lower = int(1900)
image_crop = image.crop((left, upper, right, lower))
image_resized = image_crop.resize((4032, 3024))
image_resized.save(f'./resource/image_croped_{left}_{upper}.jpg', quality=95)

