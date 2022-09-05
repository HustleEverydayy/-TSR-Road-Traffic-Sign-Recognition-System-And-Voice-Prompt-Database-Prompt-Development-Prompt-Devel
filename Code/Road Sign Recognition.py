import cv2
from keras.models import load_model
import numpy as np

traffic_sign = cv2.CascadeClassifier('circular_lbp_new.xml')
threshold=0.90
font=cv2.FONT_HERSHEY_COMPLEX
model = load_model('traffic_classifier1(2).h5')

def preprocessing(img):
    img=img.astype("uint8")
    img=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img=cv2.equalizeHist(img)
    img = img/255
    return img

def get_className(classNo):
   if classNo==0:
   		return "Speed limit (20km/h)"
   elif classNo==1:
   		return "Speed limit (30km/h)"
   elif classNo==2:
        return "Speed limit (50km/h)"
   elif classNo==3:
        return "Speed limit (60km/h)"
   elif classNo==4:
        return "Speed limit (70km/h)"
   elif classNo==5:
        return "Speed limit (80km/h)"
   elif classNo==6:
        return "Speed limit (100km/h)"
   elif classNo==7:
        return "Speed limit (120km/h)"

cv2.namedWindow('frame',1)
address = ('http://admin:admin@172.20.10.2:8081/')
cap = cv2.VideoCapture(address)
cap.set(3,800)
cap.set(4,800)
while True: 
    if cv2.waitKey(1):
        ret, frame = cap.read()
        signs = traffic_sign.detectMultiScale(frame,1.3,5)
        for x,y,w,h in signs:
            crop_img=frame[y:y+h,x:x+h]
            img = cv2.resize(crop_img, (30,30)) 
            img = np.expand_dims(img, axis=0) 
            img = np.array(img)
            prediction=model.predict(img)
            classIndex=model.predict_classes(img)
            probabilityValue=np.amax(prediction)
            if probabilityValue>threshold:
                if classIndex==0:
                    cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
                    cv2.rectangle(frame, (x,y-40),(x+w, y), (0,255,0),-2)
                    cv2.putText(frame, str(get_className(classIndex)),(x,y-10), font, 0.75, (255,255,255),1, cv2.LINE_AA)
                if classIndex==1:
                    cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
                    cv2.rectangle(frame, (x,y-40),(x+w, y), (0,255,0),-2)
                    cv2.putText(frame, str(get_className(classIndex)),(x,y-10), font, 0.75, (255,255,255),1, cv2.LINE_AA)
                if classIndex==2:
                    cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
                    cv2.rectangle(frame, (x,y-40),(x+w, y), (0,255,0),-2)
                    cv2.putText(frame, str(get_className(classIndex)),(x,y-10), font, 0.75, (255,255,255),1, cv2.LINE_AA)
                if classIndex==3:
                    cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
                    cv2.rectangle(frame, (x,y-40),(x+w, y), (0,255,0),-2)
                    cv2.putText(frame, str(get_className(classIndex)),(x,y-10), font, 0.75, (255,255,255),1, cv2.LINE_AA)
                if classIndex==4:
                    cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
                    cv2.rectangle(frame, (x,y-40),(x+w, y), (0,255,0),-2)
                    cv2.putText(frame, str(get_className(classIndex)),(x,y-10), font, 0.75, (255,255,255),1, cv2.LINE_AA)
                if classIndex==5:
                    cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
                    cv2.rectangle(frame, (x,y-40),(x+w, y), (0,255,0),-2)
                    cv2.putText(frame, str(get_className(classIndex)),(x,y-10), font, 0.75, (255,255,255),1, cv2.LINE_AA)
                if classIndex==6:
                    cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
                    cv2.rectangle(frame, (x,y-40),(x+w, y), (0,255,0),-2)
                    cv2.putText(frame, str(get_className(classIndex)),(x,y-10), font, 0.75, (255,255,255),1, cv2.LINE_AA)
                if classIndex==7:
                    cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
                    cv2.rectangle(frame, (x,y-40),(x+w, y), (0,255,0),-2)
                    cv2.putText(frame, str(get_className(classIndex)),(x,y-10), font, 0.75, (255,255,255),1, cv2.LINE_AA)
            
        cv2.imshow ( 'frame', frame)
    if cv2.waitKey(1) & 0xFF == 27:
        break 
cap.release ()
cv2.destroyAllWindows()
