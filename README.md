<p align="center">
  <a href="#">
    <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=32&pause=1000&color=4CAF50&center=true&vCenter=true&width=700&lines=Auto+Dog+Photographer+🐶📸" alt="Auto Dog Photographer animated title" />
  </a>
</p>

<h3 align="center">🐶📸 AI Powered Smart Pet Camera</h3>

<p align="center">
  A fun computer vision project that automatically captures your dog’s best moments using real-time AI detection.
</p>

---

## 🌟 About the Project

**Auto Dog Photographer** is built using **Python, OpenCV, and YOLOv8** to automatically capture photos of a dog when it is perfectly positioned.

The system:
- Detects your dog in real time 🐶  
- Checks if the dog is centered 🎯  
- Ensures the dog is stable 🧘  
- Captures the best frame automatically 📸  

---

## 🎯 Project Features

- 🧠 Real-time dog detection using YOLOv8  
- 🎯 Smart centering-based capture  
- 🧘 Stability detection  
- 📸 Automatic photo capture  
- 🖥️ Instant image display  

---

## 🛠️ Built With

- Python  
- OpenCV  
- YOLOv8 (Ultralytics)  
- NumPy  

---

## 🧠 How It Works

1. Webcam captures live frames  
2. YOLO detects dog  
3. Tracks position across frames  
4. Checks:
   - Centered 🎯  
   - Stable 🧘  
5. Captures image automatically  

---

## 📂 Project Structure

    auto_dog_photographer/
    │
    ├── main.py
    ├── config.py
    ├── requirements.txt
    │
    ├── models/
    │   └── yolo_model.py
    │
    ├── detection/
    │   └── dog_detector.py
    │
    ├── tracking/
    │   └── stability_tracker.py
    │
    ├── utils/
    │   ├── camera.py
    │   ├── image_utils.py
    │   └── trigger.py
    │
    ├── outputs/
    │   └── captured images
    │
    └── assets/
        └── yolov8n.pt

---

## 🚀 How to Run

### 1. Clone the repository

```bash
git clone https://github.com/M-Nivetha7/Auto_Dog_Photograher.git
cd Auto_Dog_Photograher
```

### 2. Create virtual environment
```
python -m venv venv
source venv/bin/activate
```

### 3. Install dependencies
```
pip install -r requirements.txt
```
### 4. Run the project
```
python main.py
```
---

## 📸 Usage

- Place your dog in front of the camera 🐶  
- Ensure:
  - centered 🎯  
  - still 🧘  
- System captures automatically 📸  

---

## 🐾 Inspiration

Built out of curiosity and boredom, turned into a fun AI project.  
Now my dog gets better photos than me 😄  

---

## 👩‍💻 Author

**M. Nivetha**  
AI & ML Undergraduate | Computer Vision Enthusiast 👁️  

---

⭐ Star the repo if you like it!
