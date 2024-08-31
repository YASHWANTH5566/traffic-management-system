from flask import Flask, Response, render_template, jsonify
import cv2
from ultralytics import YOLO

app = Flask(__name__)
model = YOLO('yolov8s.pt')

def process_video_feed():
    # Use raw string literal or forward slashes in the path
    video_path = r'C:\Users\myasw\OneDrive\Desktop\traffic-management-system\5927708-hd_1080_1920_30fps.mp4'
    cap = cv2.VideoCapture(video_path)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        results = model(frame)
        vehicle_count = 0

        for result in results:
            boxes = result.boxes
            for box in boxes:
                label = result.names[box.cls[0].item()]
                if label in ['car', 'bus', 'truck', 'motorbike', 'bicycle']:
                    vehicle_count += 1

        signal_decision = "Green" if vehicle_count > 20 else "Red"

        yield jsonify({"vehicle_count": vehicle_count, "signal": signal_decision})

    cap.release()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    return Response(process_video_feed(), mimetype='application/json')

if __name__ == '__main__':
    app.run(debug=True)
