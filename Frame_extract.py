import cv2

cap = cv2.VideoCapture("Data_vid/back.mp4")
i=0
while(cap.isOpened()):
    
    ret,img=cap.read()
    
    filename='back'
    foldername="image/"+filename+'/'
    img_filename=foldername+filename+'_'+str(i)+'.jpg'
    # print(img.shape)
    cv2.imwrite(img_filename,img)
    i=i+1
    print(i)