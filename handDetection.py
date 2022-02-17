import cv2
import mediapipe as mp
import time
import imutils


cap = cv2.VideoCapture(0)

mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
indicator = 0
tap = False
up_again = False
sigue_abajo = False
previous_time = time.time()

with mp_hands.Hands(
    model_complexity = 0,
    min_detection_confidence=0.5,
    min_tracking_confidence =0.5) as hands:

    while(cap.isOpened()):
        success, image = cap.read()
        
        image = imutils.resize(image, width = 640)

        if(not success):
            print('Ignoring frame')
            continue

        image.flags.writeable = False
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        results = hands.process(image)

        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        h, w, c = image.shape
        hand = False
        if(results.multi_hand_landmarks):
            
            for hand_landmark in results.multi_hand_landmarks:
                mp_drawing.draw_landmarks(
                    image,
                    hand_landmark,
                    mp_hands.HAND_CONNECTIONS,
                    mp_drawing_styles.get_default_hand_landmarks_style(),
                    mp_drawing_styles.get_default_hand_connections_style())
                for id, lm in enumerate(hand_landmark.landmark):
                    hand = True
                    if(id == 4):
                        point4_x = lm.x
                        point4_y = lm.y
                        point4_z = lm.z
                        point4_x_image = int(lm.x * w)
                        point4_y_image = int(lm.y * h)
                        point4_z_image = int(lm.z * h)
                        # print('---------------')
                        # print("4 x={} y={} z={}".format(lm.x, lm.y, lm.z))
                        # print('---------------')
                    if(id==8):
                        point8_x = lm.x
                        point8_y = lm.y
                        point8_z = lm.z
                        point8_x_image = int(lm.x * w)
                        point8_y_image = int(lm.y * h)
                        point8_z_image = int(lm.z * h)
                        # print('---------------')
                        # print("8 x={} y={} z={}".format(lm.x, lm.y, lm.z))
                        # print('---------------')
        if(hand):
            cv2.line(image, (point4_x_image, point4_y_image), (point8_x_image, point8_y_image), (0, 255, 0), thickness=3, lineType=8)
            distancia = ((point4_x-point8_x)**2 + (point4_y-point8_y)**2 + (point4_z-point8_z)**2)**(1/2)
            # print(distancia)
            if(distancia <= 0.06):
                # print('Hellooooo' + str(indicator) + ": " +str(distancia))
                print(distancia)
                tap_time = time.time()

                difference_bettween_taps = tap_time - previous_time
                
                is_double = difference_bettween_taps > 0.05 and difference_bettween_taps < 0.45
                # print("tap: {}\n is_double: {}\n up again: {}\n----------------".format(tap, is_double, up_again))
                # if(not tap and not is_double):
                #     print('Tap')
                #     tap = True
                #     previous_time = tap_time
                # elif(tap and not is_double):
                #     print("Still down")
                #     tap = True
                # if(up_again and is_double and not tap):
                #     print('DOUBLE TAP')
                #     tap = False
                #     previous_time = tap_time
                # elif(not tap):
                #     print("Still double down")
                #     tap = False

                # up_again = False
                # indicator += 1

                if(sigue_abajo == False):
                    if(not tap and up_again):
                        # print('Tap')
                        # print('is_double: {}'.format(is_double))
                        tap = True
                        if(is_double):
                            print('******Double Tap******\n')
                            # print("Time Difference: {}\nD".format(difference_bettween_taps))
                            # print("tap: {}\n is_double: {}\n up again: {}\n----------------\n\n".format(tap, is_double, up_again))
                        else:
                            print('******Tap******\n')
                            # print("Time Difference: {}\n".format(difference_bettween_taps))
                            # print("Time Difference: {}".format(difference_bettween_taps))
                        previous_time = tap_time
                    elif(tap and up_again):
                        print('Algo safas')
                    elif(not tap and not up_again):
                        print("Algo 2")
                        tap = True
                    elif(tap and not up_again):
                        print("Sigue abajo")
                        sigue_abajo = True
                        # print(distancia)
                
                up_again = False
                print('********')
            elif(distancia > 0.06):
                # if(tap):
                tap = False
                up_again = True
            
            if(distancia > 0.06):
                sigue_abajo = False
                # print(distancia)
                
            
            

        cv2.imshow('Hands', cv2.flip(image, 1))
        
        if(cv2.waitKey(1) and 0xFF == 27):
            break

cap.release()


    


