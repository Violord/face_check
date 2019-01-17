import face_recognition as fr
import cv2
import numpy as np
import requests


def face_match(known_img_addr, target_img_addr, threshold):
    '''
    Compare two images and find out if there are matched faces.
    known_img_addr, target_img_addr : Images url address
    threshold : A float between 0~1 for thresholding the comparison result
    '''
    file = requests.get(known_img_addr)
    known_img = cv2.imdecode(np.fromstring(file.content, np.uint8), 1)
    print('Got image 1 - ', type(known_img), '\n')
    file = requests.get(target_img_addr)
    target_img = cv2.imdecode(np.fromstring(file.content, np.uint8), 1)
    print('Got image 2 - ', type(target_img), '\n')

    try:
        known_encod = fr.face_encodings(known_img)
        target_encod = fr.face_encodings(target_img)[0]
    except:
        print('Failed finding faces!')
        return

    if True in fr.compare_faces(known_encod, target_encod, threshold):
        '''
        Liveness detection
        '''
        return True

    return False


if __name__ == '__main__':
    addr1 = input('Address of the first image: ')
    addr2 = input('Address of the second image: ')
    threshold = input('Threshold (leave blank to use the default threshold 0.45) : ')
    while threshold and (float(threshold) > 1 or float(threshold) < 0):
        threshold = input('Threshold must be between 0~1 ! Reinput threshold: ')
    if not threshold:
        threshold = 0.45
    print(face_match(addr1, addr2, float(threshold)))