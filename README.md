**IoT-based system for Waste Classification and Segregation**

---

### Overview

This project aims to create a waste classification system using machine learning and IoT technologies. By integrating a camera-equipped device, such as an ESP32 CAM, with a Flask web application and a pre-trained machine learning model, users can classify waste into biodegradable and non-biodegradable categories.

---

### Features

- Real-time waste classification using a camera feed
- Classification results displayed on a web interface
- Dumping of waste based on its classification using servo motor.
- Simple and intuitive user interface

---

### How It Works

1. The ESP32 CAM captures images of waste placed on its lid.
2. The Flask web application receives the camera feed and sends it to a pre-trained machine learning model for classification.
3. The model determines whether the waste is biodegradable or non-biodegradable.
4. The classification result is displayed on the web interface, along with a "Dump" button.
5. When the "Dump" button is clicked, the Flask application sends a command to the servo motor to dump the waste into the appropriate bin.
6. The lid of the waste bin rotates accordingly based on the waste classification.

---

![Screenshot 2024-02-29 165434](https://github.com/Mohd-Daniyal/WasteWise-An-Iot-based-Waste-Segregation/assets/96229438/0886ef9e-de57-4f04-8552-8d2e54d1b3eb)   ![Screenshot 2024-02-29 165536](https://github.com/Mohd-Daniyal/WasteWise-An-Iot-based-Waste-Segregation/assets/96229438/7ab6a219-2d87-4bc6-a130-216d8c3475cf)


### Getting Started

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/your-username/your-repository.git
   ```

2. Install the required Python packages:

   ```bash
   pip install -r requirements.txt
   ```

3. Connect your ESP32 and NodeMCU devices to your computer.

4. Open the Arduino IDE, select the appropriate board and port, then upload the respective codes.

5. Run the Flask application:

   ```bash
   python app.py
   ```

6. Open your web browser and navigate to `http://localhost:5000` to access the web interface.

7. Place waste on the lid of the camera-equipped device and click the "Classify" button to start the classification process.

---

### Dependencies

- Flask
- TensorFlow
- OpenCV
- NumPy

---

Feel free to contribute, report issues, or suggest improvements. Let's make waste classification more efficient and sustainable together! 🌱🌍
