'''
load YOLOv8 model
read image
predict image(use supervision)


---test---
view the predicted image
save the image to a folder 
'''
import cv2
import supervision as sv
from ultralytics import YOLO

MODEL_PATH = "best.pt"
# SOURCE_IMAGE_PATH = 'image_folder/image_45_jpg.rf.37a18abc18459eff451a82f54c34dfc8.jpg'

# Initialize the YOLOv8 model
model = YOLO(MODEL_PATH)

def process_image(image, model):
    # Predict image
    results = model(image)[0]
    detections = sv.Detections.from_ultralytics(results)

    bounding_box_annotator = sv.BoundingBoxAnnotator()
    label_annotator = sv.LabelAnnotator()

    annotated_image = bounding_box_annotator.annotate(
        scene=image, detections=detections)
    annotated_image = label_annotator.annotate(
        scene=annotated_image, detections=detections)
    
    return annotated_image

#     sv.plot_image(image=annotated_image, size=(5, 5))

# if __name__ == "__main__":
#     annotated_image = process_image(SOURCE_IMAGE_PATH, model)
#     sv.plot_image(image=annotated_image, size=(5, 5))