import cv2
from threading import Thread
from time import sleep, time
from eye import Eye
from dynamixel import write_print
import numpy as np


class Track:
    def __init__(self, eye: Eye, face_net, gender_net, age_net, object_net):
        self.MODEL_MEAN_VALUES = (78.4263377603, 87.7689143744, 114.895847746)
        self.ageList = ['(0-2)', '(4-6)', '(8-12)', '(15-20)', '(25-32)', '(38-43)', '(48-53)', '(60-100)']
        self.genderList = ['Male', 'Female']
        self.objs = np.load('C:/xampp/htdocs/abusaif/prototype1/en/controlpanel/pythoncode/models/objs.npy')
        np.random.seed(2080)
        self.COLORS = np.random.uniform(0, 255, size=(len(self.objs), 3))

        self.gender_net = gender_net
        self.age_net = age_net
        self.obj_net = object_net
        self.change_angle = lambda x: write_print(6, 'GoalPosition', x)
        self.face_net = face_net
        self.face_here = False
        write_print(6, "MovingSpeed", 30)
        self.angle = 510
        self.change_angle(self.angle)
        self.eye = eye
        _, self.width, _ = eye.read().shape
        self.stopped = False

    def search_face(self):
        while True:
            # s = time()
            while not self.face_here:
                # if time() - s > 10:

                while self.angle < 510:
                    self.angle += 25
                    self.change_angle(self.angle)
                    sleep(.3)
                    if self.face_here:
                        break
                if self.face_here:
                    break
                sleep(3)

                while self.angle < 560:
                    self.angle += 25
                    self.change_angle(self.angle)
                    sleep(.3)
                    if self.face_here:
                        break
                if self.face_here:
                    break
                sleep(3)

                while self.angle > 510:
                    self.angle -= 25
                    self.change_angle(self.angle)
                    sleep(.3)
                    if self.face_here:
                        break
                if self.face_here:
                    break
                sleep(3)

                while self.angle > 460:
                    self.angle -= 25
                    self.change_angle(self.angle)
                    sleep(.3)
                    if self.face_here:
                        break
                if self.face_here:
                    break
                sleep(3)

    @staticmethod
    def rearrange(v, in_, out_):
        return (((v - in_[0]) * (out_[1] - out_[0])) / (in_[1] - in_[0])) + out_[0]  - 130

    def direction(self, val, range_vals):
        center_range = int((range_vals / 3) / 2)
        new_v = self.rearrange(val, [0, range_vals], [-int(range_vals / 2), int(range_vals / 2)])
        if abs(new_v) >= center_range:
            return -20 if new_v > 0 else 20
        else:
            return 0

    def start(self):
        Thread(target=self.update, args=()).start()
        Thread(target=self.search_face, args=()).start()
        return self

    def update(self):
        old_angle = 140
        while not self.stopped:
            frame = self.eye.read()
            (h, w) = frame.shape[:2]

            image_blob = cv2.dnn.blobFromImage(
                cv2.resize(frame, (300, 300)), 1.0, (300, 300),
                (104.0, 177.0, 123.0), swapRB=False, crop=False)
            object_blob = cv2.dnn.blobFromImage(cv2.resize(frame, (300, 300)), 0.007843, (300, 300), 127.5)

            self.face_net.setInput(image_blob)
            detections = self.face_net.forward()

            if len(detections) > 0:
                i = np.argmax(detections[0, 0, :, 2])
                confidence = detections[0, 0, i, 2]

                if confidence > 0.5:
                    box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
                    (startX, startY, endX, endY) = box.astype("int")

                    cent_x = ((endX - startX) / 2) + startX
                    cent_y = ((endY - startY) / 2) + startY
                    centroid = [cent_x, cent_y]
                    face = frame[startY:endY, startX:endX]
                    cv2.rectangle(frame, (startX, startY), (endX, endY), (0, 0, 255), 4)
                    self.angle += self.direction(centroid[0], self.width)
                    self.face_here = True
                    try:
                        blob = cv2.dnn.blobFromImage(face, 1.0, (227, 227), self.MODEL_MEAN_VALUES, swapRB=False)
                        # self.gender_net.setInput(blob)
                        # genderPreds = self.gender_net.forward()
                        # gender = self.genderList[genderPreds[1].argmax()]

                        self.age_net.setInput(blob)
                        agePreds = self.age_net.forward()
                        age = self.ageList[agePreds[0].argmax()]

                        # label = "{},{}".format(gender, age)
                        # cv2.putText(frame, label, (startX, startY - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255),
                        #             2, cv2.LINE_AA)

                        self.obj_net.setInput(object_blob)
                        detections = self.obj_net.forward()

                        for i in np.arange(0, detections.shape[2]):

                            confidence = detections[0, 0, i, 2]
                            if confidence > 0.5:
                                idx = int(detections[0, 0, i, 1])
                                box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
                                (startX, startY, endX, endY) = box.astype("int")
                                if not self.objs[idx] == 'background':
                                    label = "{}: {:.2f}%".format(self.objs[idx], confidence * 100)
                                    cv2.rectangle(frame, (startX, startY), (endX, endY), self.COLORS[idx], 4)
                                    y = startY - 15 if startY - 15 > 15 else startY + 15
                                    cv2.putText(frame, label, (startX, y), cv2.FONT_HERSHEY_SIMPLEX,
                                                0.5, self.COLORS[idx], 2)

                    except Exception as e:
                        del e
                        pass
                    cv2.imshow('frame', frame)
                    cv2.waitKey(1)
                else:
                    try:
                        self.face_here = False
                        self.obj_net.setInput(object_blob)
                        detections = self.obj_net.forward()

                        for i in np.arange(0, detections.shape[2]):

                            confidence = detections[0, 0, i, 2]
                            if confidence > 0.5:
                                idx = int(detections[0, 0, i, 1])
                                box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
                                (startX, startY, endX, endY) = box.astype("int")
                                if not self.objs[idx] == 'background':
                                    label = "{}: {:.2f}%".format(self.objs[idx], confidence * 100)
                                    cv2.rectangle(frame, (startX, startY), (endX, endY), self.COLORS[idx], 4)
                                    y = startY - 15 if startY - 15 > 15 else startY + 15
                                    cv2.putText(frame, label, (startX, y), cv2.FONT_HERSHEY_SIMPLEX,
                                                0.5, self.COLORS[idx], 2)

                    except Exception as e:
                        del e
                        pass
                    cv2.imshow('frame', frame)
                    cv2.waitKey(1)
                    continue
            else:
                try:
                    self.obj_net.setInput(object_blob)
                    detections = self.obj_net.forward()

                    for i in np.arange(0, detections.shape[2]):

                        confidence = detections[0, 0, i, 2]
                        if confidence > 0.5:
                            idx = int(detections[0, 0, i, 1])
                            box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
                            (startX, startY, endX, endY) = box.astype("int")
                            if not self.objs[idx] == 'background':
                                label = "{}: {:.2f}%".format(self.objs[idx], confidence * 100)
                                cv2.rectangle(frame, (startX, startY), (endX, endY), self.COLORS[idx], 4)
                                y = startY - 15 if startY - 15 > 15 else startY + 15
                                cv2.putText(frame, label, (startX, y), cv2.FONT_HERSHEY_SIMPLEX,
                                            0.5, self.COLORS[idx], 2)
                except Exception as e:
                    del e
                    pass
                cv2.imshow('frame', frame)
                cv2.waitKey(1)
                self.face_here = False
            if self.angle >= 560:
                self.angle = 560
            elif self.angle <= 0:
                self.angle = 0
            else:
                if not old_angle == self.angle:
                    self.change_angle(self.angle)
                    sleep(.1)
                    old_angle = self.angle
            cv2.imshow('frame', frame)
            cv2.waitKey(1)
        cv2.destroyAllWindows()
    
    def stop(self):
        self.stopped = True
        while self.angle != 510:
            if self.angle > 510:
                self.angle -= 5
                self.change_angle(self.angle)
                sleep(0.01)
            else:
                self.angle += 5
                self.change_angle(self.angle)
                sleep(0.01)
