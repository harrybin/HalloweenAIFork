from Tracking.gfx.DetectionHelper import DetectionHelper
import dlib 

class TrackingHelper:
    def __init__(self) -> None:
        pass
            
    def createTrackers(self, detections, frameRGB):
        trackers=[]        
        for i,faceRect in enumerate(detections):
            (startX, startY, endX, endY) = faceRect.astype("int")
            detections[i] =[int(coord) for coord in faceRect]
            dlibCorrelationTracker = dlib.correlation_tracker()
            correlationRect = dlib.rectangle(startX, startY, endX, endY)
            dlibCorrelationTracker.start_track(frameRGB,correlationRect)
            trackers.append(dlibCorrelationTracker)
        return trackers

    def updateTrackers(self, trackers, frameRGB):
        detections = []
        for tracker in trackers:
            psr = tracker.update(frameRGB)
            pos = tracker.get_position()
            # unpack the position object
            startX = int(pos.left())
            startY = int(pos.top())
            endX = int(pos.right())
            endY = int(pos.bottom())

            detections.append((startX, startY, endX, endY))
        return detections
                