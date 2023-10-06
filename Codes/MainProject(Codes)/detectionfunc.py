

def most_freq(List):
	return max(set(List),key = List.count)
	

def detection():
	from cvzone.ClassificationModule import Classifier
	import cv2
	import time
	cap = cv2.VideoCapture(0)
	maskClassifier = Classifier("/home/user/Desktop/keras_model.h5","/home/user/Desktop/labels.txt")    
	prediction_list = [];
	classDic = {0: 0,           #0 Organic
            1: 2,           #1 Recyclable
            2: 1,           #2 Non-Recyclable
            3: 1,			# 3 is Nothing(Yet to be added)
            4: 1,
            5: 1,
            6: 3}


	bins = ("Organic", "Recyclable", "Non-Recyclable", "Nothing")      #The bins
	t_end = time.time()+20							#(takes the average value of 20 seconds)
	while time.time() < t_end:
		_, img = cap.read()
		predection = maskClassifier.getPrediction(img)      #Getting prediction from the model
		#print(predection)
		ID = predection[1]
		#print(bin)
		prediction_list.append(ID)
		#cv2.imshow("Image", img)
		#if cv2.waitKey(1) == ord('q'):
			#break
			
	ID = most_freq(prediction_list)
	can = bins[classDic[ID]]
	cap.release()
	cv2.destroyAllWindows()
	print("The bin to go is: "+can)
	return ID



