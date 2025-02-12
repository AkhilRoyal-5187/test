from flask import Flask, request, jsonify, render_template
import subprocess

app = Flask(__name__)

# Serve the frontend
@app.route('/')
def index():
    return render_template('index.html')

# Start Attendance (Face Recognition)
@app.route('/start_attendance', methods=['POST'])
def start_attendance():
    data = request.get_json()
    print("Received Data:", data)  # Debugging log

    lecture_name = data.get("lecture")
    periods = data.get("periods")

    if not lecture_name or not periods:
        return jsonify({"error": "Missing lecture name or periods"}), 400

    try:
        subprocess.Popen(["python3", "face_recognition_code.py", lecture_name, str(periods)])
        return jsonify({"message": "Face recognition started successfully"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Capture Image
@app.route('/capture_image', methods=['POST'])
def capture_image():
    data = request.get_json()
    name = data.get("name")

    if not name:
        return jsonify({"error": "Missing name"}), 400

    try:
        subprocess.Popen(["python3", "capture_image_from_camera.py", name])
        return jsonify({"message": "Image capture started"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Get Attendance
@app.route('/get_attendance', methods=['GET'])
def get_attendance():
    result = subprocess.run(
        ["python3", "get_attendance.py"],
        capture_output=True, text=True
    )
    return jsonify({"message": "Attendance fetched", "output": result.stdout})

if __name__ == '__main__':
    app.run(debug=True)
