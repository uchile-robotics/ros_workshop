#!/usr/bin/env python
import rospy
import cv2
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
import numpy as np 

# define range of blue color in HSV
lower_blue = np.array([110,50,50])
upper_blue = np.array([130,255,255])
lower_red = np.array([0,0,0])
upper_red = np.array([0,0,0])
lower_yellow = np.array([45,50,50])
upper_yellow = np.array([100,255,255])

class DucksDetector():

    def __init__(self):

        self.image_subscriber = rospy.Subscriber('topico', MSG, callback )
        self.publisher = rospy.Publisher('topico', MSG , queue_size=10)

        #Clase necesaria para transformar el tipo de imagen
        self.bridge = CvBridge()
        self.cv_image = Image()
        self.img_out = Image()

        self.kernel = np.ones((5,5),np.uint8) #kernel a usar en transformaciones morfologicas

    def _process_image(self,img):
        #Se cambiar mensage tipo ros a imagen opencv
        try:
            self.cv_image = self.bridge.imgmsg_to_cv2(img, "bgr8")
        except CvBridgeError as e:
            print(e)

        #Cambiar tipo de color de BGR a HSV

        # Filtrar colores de la imagen en el rango utilizando 

        # Aplicar Máscara!

        #Operaciones morfologicas

        #Contornos
        
        #Publicar 
        
        #Rotar hacia Pato!
def main():

    rospy.init_node('DucksDetector')
    DucksDetector()
    rospy.spin()

if __name__ == '__main__':
    main()
