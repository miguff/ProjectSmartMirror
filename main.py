import subprocess
import cv2
import sys



def main():

    
    s = 1 #Number of camera
    source = cv2.VideoCapture(s)

    win_name = 'Camera Preview'
    cv2.namedWindow(win_name, cv2.WINDOW_NORMAL)

    while cv2.waitKey(1) != 27: # Escape
        has_frame, frame = source.read()
        if not has_frame:
            break
        cv2.imshow(win_name, frame)

    source.release()
    cv2.destroyWindow(win_name)


    pw = "1234"
    
    askedpw = input("What is the pw? ")
    if askedpw == pw:
        subprocess.call("./control.sh")





if __name__ == "__main__":
    main()