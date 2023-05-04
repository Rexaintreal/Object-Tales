<h1 align="center">Object Tales</h1>

<p align="center">
  <img src="https://img.shields.io/badge/license-MIT-blue.svg" alt="License: MIT">
  <img src="https://img.shields.io/badge/python-3.8-blue.svg" alt="Python: 3.8">
  <img src="https://img.shields.io/badge/yolov3--320-v4.0-green" alt="yolov3-320: v4.0">
  <img src="https://img.shields.io/badge/gpt--2-v2.2-blue" alt="gpt-2: v2.2">
</p>

<p align="center">
  <img src="https://github.com/Rexaintreal/Object-Tales/blob/main/Images/Object%20Tales.png" alt="Object Tales Logo">
</p>

<p align="center">
  Object Tales generates stories based on the objects in the images. It uses YOLOv3-320 to detect objects and GPT-2 to generate stories. This is a Python 3.8 application.
</p>

--- 

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [How it Works](#how-it-works)
- [Author](#author)

---

## Installation
### Clone the repository:

```bash
git clone https://github.com/Rexaintreal/object-tales.git

cd object-tales/
```
### Install dependencies:
```bash
pip install -r requirements.txt
```
### Download YOLOv3-320 weights:
Download the pre-trained YOLOv3-320 weights from the official repository using the following command:
```bash
wget https://pjreddie.com/media/files/yolov3.weights -O models/yolov3-320.weights
```
### Download GPT-2 model:
Download the GPT-2 model from OpenAI using the following command:
```bash
python download_model.py 117M
```
## Usage

To use the Object Tales GUI application, follow these steps:

1. Launch the application by running the `main.py` file.
2. Click the "Open Image" button to select an image to generate a story for.
3. Click the "Generate Story" button to generate a story based on the objects detected in the selected image.
4. The generated story will be displayed in the "Story" section of the application.

Note: Make sure that the required dependencies are installed before launching the application. See the "Installation" section for details.
![Screenshot 1](https://github.com/Rexaintreal/Object-Tales/blob/main/Images/Screenshot%20(60).png)
![Screenshot 2](https://github.com/Rexaintreal/Object-Tales/blob/main/Images/Screenshot%20(61).png)
### How it Works

Object Tales is a Python-based application that generates stories based on the objects in the images. It uses a combination of YOLOv3-320 object detection and GPT-2 text generation to analyze the images and create unique and engaging narratives.

When you run the program, you can select an image from your local file system or use the program's built-in camera to capture an image. Object Tales then uses YOLOv3-320 to identify the objects in the image and extract their features. These features are then passed to GPT-2, which generates a story based on the objects and their attributes.

The program outputs the generated story to the screen, and you can save it to a file if desired. Object Tales also allows you to adjust the length and complexity of the generated stories, as well as the confidence threshold for object detection.

Overall, Object Tales provides a fun and creative way to explore the stories hidden in everyday objects and images.

![Working](https://github.com/Rexaintreal/Object-Tales/blob/main/Images/Working.png)
### Author

MyProgram was created by [Saurabh Tiwari](https://github.com/Rexaintreal). 

- [Email](mailto:saurabhtiwari7986@gmail.com)

### You may also like...

- [Libro Voice](https://github.com/Rexaintreal/Libro-Voice) - A PDF to Audio Converter
- [Snippet Vision](https://github.com/Rexaintreal/Snippet-Vision)- A Youtube Video Summarizer
- [Weather App](https://github.com/Rexaintreal/WeatherApp) - A Python Weather Forcast App
- [Python Screenrecorder](https://github.com/Rexaintreal/PythonScreenrecorder) - A Python Screen Recorder
- [Typing Speed Tester](https://github.com/Rexaintreal/TypingSpeedTester) - A Python Typing Speed Tester
- [Movie Recommender](https://github.com/Rexaintreal/Movie-Recommender) - A Python Movie Recommender
- [Password Generator(https://github.com/Rexaintreal/Password-Generator) - A Python Password Generator
