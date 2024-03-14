import skimage
import cv2
import os

print('étape :')
if not os.path.exists('resized_dataset') :
		os.makedirs('resized_dataset')
for folder in os.listdir('data') :
	if not os.path.exists('resized_dataset/' + folder) :
		os.makedirs('resized_dataset/'+ folder)
	n = 0
	for file in os.listdir('data/' + folder) :
		file_path = 'data/' + folder + '/' + file
		image = cv2.imread(file_path, 0)
		resized_image = cv2.resize(inverted_img, dsize=(28,28), interpolation=cv2.INTER_CUBIC)
		inverted_img = skimage.util.invert(resized_image)
		future_file_path = 'resized_dataset/' + folder + '/' + folder + '-' + str(n) + '.png'
		n += 1
		cv2.imwrite(future_file_path, inverted_img)
		if n%300 == 0 :
			print(f'{folder} redimensionnés : {n}')
