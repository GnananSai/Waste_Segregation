from cvzone.ClassificationModule import Classifier
import cv2



    
cap = cv2.VideoCapture(0)
    maskClassifier = Classifier("/home/user/Desktop/keras_model.h5","/home/user/Desktop/labels.txt")    #path of model, labels respectively

classDic = {0: 0,           #0 Organic
            1: 2,           #1 Recyclable
            2: 1,           #2 Non-Recyclable
            3: 1,
            4: 1,
            5: 1}


bins = ("Organic", "Recyclable", "Non-Recyclable")      #The bins
while True:
    _, img = cap.read()
    predection = maskClassifier.getPrediction(img)      #Getting prediction from the model
    #print(predection)
    ID = predection[1]
    bin = bins[classDic[ID]]
    print(bin)
    cv2.imshow("Image", img)
    if cv2.waitKey(1) == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()


