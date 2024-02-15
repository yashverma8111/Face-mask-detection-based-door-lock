import cv2
import os
import warnings
from controller import doorAutomate
from controller import led
import mediapipe as mp
import time
import controller as cnt


def detect_media(results, img, nose):
    if len(x_coordinates) > 0:
        cv2.putText(img, "(Remove hand)", remove_hand_org, font, font_scale, door_close_color,
                    thickness,
                    cv2.LINE_AA)
        cv2.putText(img, "Door is Closed", open_close_org, font, font_scale, door_close_color, thickness,
                    cv2.LINE_AA)
        doorAutomate(0)
        led("red")
    else:
        if results.detections:
            for detection in results.detections:
                mp_draw.draw_detection(img, detection)
                bboxC = detection.location_data.relative_bounding_box
                ih, iw, _ = image.shape
                bbox = [(int(bboxC.xmin * iw), int(bboxC.ymin * ih), int(bboxC.width * iw), int(bboxC.height * ih))]

                # Print coordinates, height, and width
                print("Bounding Box Coordinates (xmin, ymin, width, height):", bbox)
                for (x, y, w, h) in bbox:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
                    if len(nose) == 0:
                        cv2.putText(img, weared_mask, org, font, font_scale, weared_mask_font_color, thickness,
                                    cv2.LINE_AA)
                        cv2.putText(img, "Door is Open", open_close_org, font, font_scale, door_open_color, thickness,
                                    cv2.LINE_AA)
                        doorAutomate(1)
                        led("green")

                    else:
                        for (x2, y2, w2, h2) in nose:
                            cv2.rectangle(img, (x2, y2), (x2 + w2, y2 + h2), (0, 255, 123), 2)
                            if x < x2 and y < y2 and (x + w) > x2 + w2 and (y + h) > y2 + h2:
                                cv2.putText(img, not_weared_mask, org, font, font_scale, not_weared_mask_font_color,
                                            thickness,
                                            cv2.LINE_AA)
                                doorAutomate(0)
                                cv2.putText(img, "Door is Closed", open_close_org, font, font_scale, door_close_color,
                                            thickness,
                                            cv2.LINE_AA)
                                doorAutomate(0)
                                led("red")
                                time.sleep(duration)
                            elif len(nose) <= 1:
                                cv2.putText(img, "Door is Open", open_close_org, font, font_scale, door_open_color,
                                            thickness,
                                            cv2.LINE_AA)
                                doorAutomate(1)
                                led("green")
        else:
            cv2.putText(img, "No face found...", org, font, font_scale, no_face_found_color, thickness, cv2.LINE_AA)
            cv2.putText(img, "Door is Open", open_close_org, font, font_scale, door_open_color, thickness, cv2.LINE_AA)
            doorAutomate(1)
            led("green")




mp_draw = mp.solutions.drawing_utils
mp_hand = mp.solutions.hands
# Initialize MediaPipe Face Detection
mp_face_detection = mp.solutions.face_detection
mp_drawing = mp.solutions.drawing_utils

# Create a Face Detection object
face_detection = mp_face_detection.FaceDetection(min_detection_confidence=0.3)

tipIds = [4, 8, 12, 16, 20]

warnings.filterwarnings('ignore')

cv2_base_dir = os.path.dirname(os.path.abspath(cv2.__file__))
nose_cascade = cv2.CascadeClassifier('haarcascade_mcs_nose.xml')
div_factor = 1.1
bw_threshold = 70
font = cv2.FONT_HERSHEY_SIMPLEX
org = (30, 30)
open_close_org = (30, 80)
remove_hand_org = (350, 30)
weared_mask_font_color = (0, 255, 0)
no_face_found_color = (255, 255, 255)
door_open_color = (0, 255, 0)
door_close_color = (0, 0, 255)
not_weared_mask_font_color = (0, 0, 255)
thickness = 2
font_scale = 1
duration = 0.5
weared_mask = "Thank You for wearing MASK"
not_weared_mask = "Please wear MASK"
cap = cv2.VideoCapture(0)

with mp_hand.Hands(min_detection_confidence=0.5,
                   min_tracking_confidence=0.5) as hands:
    while 1:
        ret, img = cap.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        image = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        # Process the frame with MediaPipe Face Detection
        results_face = face_detection.process(image)

        image.flags.writeable = False
        results = hands.process(image)
        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        lmList = []
        x_coordinates = []
        y_coordinates = []
        x_max = x_min = y_max = y_min = 0
        if results.multi_hand_landmarks:
            for hand_landmark in results.multi_hand_landmarks:
                myHands = results.multi_hand_landmarks[0]
                for id, lm in enumerate(myHands.landmark):
                    h, w, c = image.shape
                    cx, cy = int(lm.x * w), int(lm.y * h)
                    lmList.append([id, cx, cy])
                mp_draw.draw_landmarks(img, hand_landmark, mp_hand.HAND_CONNECTIONS)
                for landmark in lmList:
                    landmark_id = landmark[0]
                    x_coord = landmark[1]
                    y_coord = landmark[2]
                    x_coordinates.append(x_coord)
                    y_coordinates.append(y_coord)

        nose = nose_cascade.detectMultiScale(gray, 1.1, 4)

        detect_media(results_face, img, nose)
        cv2.imshow('Mask Detection', img)
        k = cv2.waitKey(30) & 0xff
        if k == 27:
            break

cap.release()
cv2.destroyAllWindows()
