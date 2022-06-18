import cv2

class WindowManager(object):
    def __init__(self,windowName,keypressedCallback=None):
        self.keypresscallback = keypressedCallback
        self._windowName = windowName
        self._isWindowCreated = False
    
    @property
    def isWindowCreated(self):
        return self._isWindowCreated

    def createWindow(self):
        cv2.namedWindow(self._windowName)
        self._isWindowCreated = True
    
    def show(self,image):
        cv2.imshow(self._windowName,image)
    
    def destroyWindow(self):
        cv2.destroyWindow(self._windowName)
        self._isWindowCreated = False
        
    def processEvents(self):
        keycode = cv2.waitKey(1)
        if self.keypresscallback is not None and keycode != -1:
            self.keypresscallback(keycode)