import capture
import bounding_boxes
import predict
import tts
import pytesseract
import cv2
import sys

print("Enter 1 for book reading \n Enter 2 for scene images")
a = int(input())

#orig_img, gray_img = cv2.imread(sys.argv[1]), cv2.imread(sys.argv[1], 0) 
orig_img, gray_img = capture.Capture()
custom_config = r'--oem 3 --psm 6'

if a == 1 :
    text = pytesseract.image_to_string(orig_img, config = custom_config)

elif a == 2 :
    letters, words = bounding_boxes.get_bboxes(orig_img, gray_img)
    #print(len(words))
    #text = ' '.join([pytesseract.image_to_string(word, config = custom_config) for word in words if word.shape[1] > 0 and word.shape[1] > 0])
    text = ' '.join([''.join([predict.Predict(letter) for letter in _]) for _ in letters])


print(text)
tts.texttospeech(text)
