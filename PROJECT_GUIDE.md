# 🎯 Project Implementation Guide

This guide provides detailed specifications for all 7 major projects in the 100-day curriculum.

---

## Project 1: End-to-End ML Pipeline (Day 15)

### Credit Card Fraud Detection System

**Difficulty:** ⭐⭐☆☆☆

**Tech Stack:**
- Python, Pandas, NumPy, Scikit-learn
- Matplotlib, Seaborn
- Imbalanced-learn (SMOTE)
- XGBoost

**Dataset:**
- Kaggle: Credit Card Fraud Detection
- Alternative: IEEE-CIS Fraud Detection

**Architecture:**
```
Data → EDA → Preprocessing → Feature Engineering →
Model Training → Evaluation → Model Selection → Deployment Prep
```

**Step-by-Step Implementation:**

1. **Setup (30 min)**
```bash
mkdir project1_fraud_detection
cd project1_fraud_detection
python -m venv venv
source venv/bin/activate
pip install pandas numpy scikit-learn xgboost imbalanced-learn matplotlib seaborn jupyter
```

2. **Data Exploration (2 hours)**
```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
df = pd.read_csv('creditcard.csv')

# Basic exploration
print(df.info())
print(df.describe())
print(f"Fraud percentage: {df['Class'].mean() * 100:.2f}%")

# Visualizations
# - Distribution of transaction amounts
# - Time analysis
# - Class imbalance visualization
# - Correlation heatmap
```

3. **Feature Engineering (2 hours)**
```python
from sklearn.preprocessing import StandardScaler

# Create new features
df['Hour'] = df['Time'] // 3600 % 24
df['Day'] = df['Time'] // (3600 * 24)

# Amount bins
df['Amount_bin'] = pd.cut(df['Amount'], bins=[0, 10, 100, 1000, 10000], labels=[0,1,2,3])

# Log transform
df['Amount_log'] = np.log1p(df['Amount'])

# Scale features
scaler = StandardScaler()
df['Amount_scaled'] = scaler.fit_transform(df[['Amount']])
```

4. **Handle Imbalanced Data (1 hour)**
```python
from imblearn.over_sampling import SMOTE
from imblearn.under_sampling import RandomUnderSampler
from imblearn.pipeline import Pipeline as ImbPipeline

# Strategy 1: SMOTE
smote = SMOTE(sampling_strategy=0.5, random_state=42)
X_resampled, y_resampled = smote.fit_resample(X_train, y_train)

# Strategy 2: Combined
over = SMOTE(sampling_strategy=0.3)
under = RandomUnderSampler(sampling_strategy=0.7)
steps = [('o', over), ('u', under)]
pipeline = ImbPipeline(steps=steps)
```

5. **Model Training (3 hours)**
```python
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier
from sklearn.model_selection import cross_val_score, StratifiedKFold

models = {
    'Logistic Regression': LogisticRegression(max_iter=1000, class_weight='balanced'),
    'Random Forest': RandomForestClassifier(n_estimators=100, class_weight='balanced'),
    'XGBoost': XGBClassifier(scale_pos_weight=ratio, use_label_encoder=False)
}

results = {}
for name, model in models.items():
    cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
    scores = cross_val_score(model, X_train, y_train, cv=cv, scoring='roc_auc')
    results[name] = scores
    print(f"{name} - Mean AUC: {scores.mean():.4f} (+/- {scores.std():.4f})")
```

6. **Hyperparameter Tuning (2 hours)**
```python
from sklearn.model_selection import RandomizedSearchCV

param_dist = {
    'n_estimators': [100, 200, 300],
    'max_depth': [10, 20, 30, None],
    'min_samples_split': [2, 5, 10],
    'min_samples_leaf': [1, 2, 4],
    'class_weight': ['balanced', 'balanced_subsample']
}

rf = RandomForestClassifier(random_state=42)
random_search = RandomizedSearchCV(
    rf, param_dist, n_iter=20, cv=3, scoring='roc_auc',
    random_state=42, n_jobs=-1
)
random_search.fit(X_train, y_train)
best_model = random_search.best_estimator_
```

7. **Evaluation (1 hour)**
```python
from sklearn.metrics import classification_report, confusion_matrix, roc_auc_score, roc_curve
import matplotlib.pyplot as plt

# Predictions
y_pred = best_model.predict(X_test)
y_pred_proba = best_model.predict_proba(X_test)[:, 1]

# Metrics
print(classification_report(y_test, y_pred))
print(f"ROC-AUC: {roc_auc_score(y_test, y_pred_proba):.4f}")

# Confusion Matrix
cm = confusion_matrix(y_test, y_pred)
sns.heatmap(cm, annot=True, fmt='d')

# ROC Curve
fpr, tpr, thresholds = roc_curve(y_test, y_pred_proba)
plt.plot(fpr, tpr)
plt.plot([0, 1], [0, 1], 'k--')
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('ROC Curve')
```

8. **Model Saving (15 min)**
```python
import joblib

# Save model
joblib.dump(best_model, 'fraud_detection_model.pkl')
joblib.dump(scaler, 'scaler.pkl')

# Load and test
loaded_model = joblib.load('fraud_detection_model.pkl')
```

**Deliverables:**
- ✅ `01_eda.ipynb` - Exploratory data analysis
- ✅ `02_training.ipynb` - Model training and evaluation
- ✅ `train.py` - Training script
- ✅ `predict.py` - Prediction script
- ✅ `fraud_detection_model.pkl` - Saved model
- ✅ `README.md` - Documentation
- ✅ `requirements.txt` - Dependencies

**Success Criteria:**
- ROC-AUC > 0.95
- Precision > 0.85 for fraud class
- Recall > 0.75 for fraud class

---

## Project 2: Image Classification System (Day 30)

### Plant Disease Classifier with Web Interface

**Difficulty:** ⭐⭐⭐☆☆

**Tech Stack:**
- PyTorch, torchvision
- timm (PyTorch Image Models)
- Streamlit/Gradio
- Pillow, OpenCV

**Dataset:**
- PlantVillage Dataset
- Kaggle: Plant Disease Recognition

**Architecture:**
```
Image Input → Preprocessing → CNN/Transfer Learning Model →
Classification → Confidence Scores → Web Interface
```

**Implementation:**

1. **Setup (30 min)**
```bash
mkdir project2_plant_disease
cd project2_plant_disease
pip install torch torchvision timm streamlit pillow opencv-python matplotlib albumentations
```

2. **Data Preparation (2 hours)**
```python
from torchvision import datasets, transforms
from torch.utils.data import DataLoader, random_split
import albumentations as A
from albumentations.pytorch import ToTensorV2

# Data augmentation
train_transform = A.Compose([
    A.Resize(224, 224),
    A.HorizontalFlip(p=0.5),
    A.VerticalFlip(p=0.2),
    A.Rotate(limit=30, p=0.5),
    A.RandomBrightnessContrast(p=0.5),
    A.GaussNoise(p=0.3),
    A.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
    ToTensorV2()
])

test_transform = A.Compose([
    A.Resize(224, 224),
    A.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
    ToTensorV2()
])

# Custom Dataset class
class PlantDiseaseDataset(Dataset):
    def __init__(self, root_dir, transform=None):
        self.root_dir = root_dir
        self.transform = transform
        self.images = []
        self.labels = []
        # Load images and labels

    def __len__(self):
        return len(self.images)

    def __getitem__(self, idx):
        image = cv2.imread(self.images[idx])
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        if self.transform:
            augmented = self.transform(image=image)
            image = augmented['image']

        return image, self.labels[idx]
```

3. **Model Definition (1 hour)**
```python
import torch.nn as nn
import timm

# Custom CNN
class PlantCNN(nn.Module):
    def __init__(self, num_classes):
        super().__init__()
        self.conv1 = nn.Conv2d(3, 32, 3, padding=1)
        self.conv2 = nn.Conv2d(32, 64, 3, padding=1)
        self.conv3 = nn.Conv2d(64, 128, 3, padding=1)
        self.pool = nn.MaxPool2d(2, 2)
        self.fc1 = nn.Linear(128 * 28 * 28, 512)
        self.fc2 = nn.Linear(512, num_classes)
        self.dropout = nn.Dropout(0.3)

    def forward(self, x):
        x = self.pool(F.relu(self.conv1(x)))
        x = self.pool(F.relu(self.conv2(x)))
        x = self.pool(F.relu(self.conv3(x)))
        x = x.view(-1, 128 * 28 * 28)
        x = self.dropout(F.relu(self.fc1(x)))
        x = self.fc2(x)
        return x

# Transfer Learning Model
def create_transfer_model(model_name='resnet50', num_classes=38, pretrained=True):
    model = timm.create_model(model_name, pretrained=pretrained, num_classes=num_classes)
    return model
```

4. **Training Loop (2 hours)**
```python
def train_one_epoch(model, train_loader, optimizer, criterion, device):
    model.train()
    running_loss = 0.0
    correct = 0
    total = 0

    for images, labels in tqdm(train_loader):
        images, labels = images.to(device), labels.to(device)

        optimizer.zero_grad()
        outputs = model(images)
        loss = criterion(outputs, labels)
        loss.backward()
        optimizer.step()

        running_loss += loss.item()
        _, predicted = outputs.max(1)
        total += labels.size(0)
        correct += predicted.eq(labels).sum().item()

    epoch_loss = running_loss / len(train_loader)
    epoch_acc = 100. * correct / total
    return epoch_loss, epoch_acc

def validate(model, val_loader, criterion, device):
    model.eval()
    running_loss = 0.0
    correct = 0
    total = 0

    with torch.no_grad():
        for images, labels in val_loader:
            images, labels = images.to(device), labels.to(device)
            outputs = model(images)
            loss = criterion(outputs, labels)

            running_loss += loss.item()
            _, predicted = outputs.max(1)
            total += labels.size(0)
            correct += predicted.eq(labels).sum().item()

    val_loss = running_loss / len(val_loader)
    val_acc = 100. * correct / total
    return val_loss, val_acc

# Training
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
model = create_transfer_model('efficientnet_b0', num_classes=38).to(device)
criterion = nn.CrossEntropyLoss()
optimizer = optim.AdamW(model.parameters(), lr=0.001)
scheduler = optim.lr_scheduler.ReduceLROnPlateau(optimizer, mode='min', patience=3)

best_acc = 0
for epoch in range(50):
    train_loss, train_acc = train_one_epoch(model, train_loader, optimizer, criterion, device)
    val_loss, val_acc = validate(model, val_loader, criterion, device)

    scheduler.step(val_loss)

    print(f'Epoch {epoch+1}: Train Loss: {train_loss:.4f}, Train Acc: {train_acc:.2f}%')
    print(f'Val Loss: {val_loss:.4f}, Val Acc: {val_acc:.2f}%')

    if val_acc > best_acc:
        best_acc = val_acc
        torch.save(model.state_dict(), 'best_model.pth')
```

5. **Web Interface with Streamlit (1.5 hours)**
```python
import streamlit as st
import torch
from PIL import Image
import numpy as np

st.set_page_config(page_title="Plant Disease Classifier", layout="wide")
st.title("🌿 Plant Disease Detection System")

# Load model
@st.cache_resource
def load_model():
    model = create_transfer_model('efficientnet_b0', num_classes=38)
    model.load_state_dict(torch.load('best_model.pth', map_location='cpu'))
    model.eval()
    return model

model = load_model()

# Class names
class_names = ['Apple___Apple_scab', 'Apple___Black_rot', ...]  # All 38 classes

# File uploader
uploaded_file = st.file_uploader("Choose a plant image...", type=['jpg', 'png', 'jpeg'])

if uploaded_file is not None:
    col1, col2 = st.columns(2)

    with col1:
        image = Image.open(uploaded_file)
        st.image(image, caption='Uploaded Image', use_column_width=True)

    with col2:
        # Preprocess
        transform = A.Compose([
            A.Resize(224, 224),
            A.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
            ToTensorV2()
        ])

        img_array = np.array(image)
        augmented = transform(image=img_array)
        img_tensor = augmented['image'].unsqueeze(0)

        # Predict
        with torch.no_grad():
            outputs = model(img_tensor)
            probabilities = torch.softmax(outputs, dim=1)[0]
            top5_prob, top5_idx = torch.topk(probabilities, 5)

        st.subheader("Top 5 Predictions:")
        for prob, idx in zip(top5_prob, top5_idx):
            disease = class_names[idx]
            confidence = prob.item() * 100
            st.write(f"**{disease}**: {confidence:.2f}%")
            st.progress(confidence / 100)

        # Treatment recommendation
        if top5_prob[0] > 0.7:
            st.success(f"Diagnosis: {class_names[top5_idx[0]]}")
            st.info("Recommended Treatment: [Add treatment info based on disease]")
```

**Deliverables:**
- ✅ `train.py` - Training script
- ✅ `app.py` - Streamlit application
- ✅ `best_model.pth` - Trained model
- ✅ `requirements.txt`
- ✅ `README.md` with usage instructions
- ✅ `notebooks/` - EDA and experiments

**Success Criteria:**
- Validation accuracy > 95%
- Working web interface
- Inference time < 1 second

---

## Project 3: Smart Surveillance System (Day 45)

### Real-Time Object Detection and Tracking

**Difficulty:** ⭐⭐⭐⭐☆

**Tech Stack:**
- YOLOv8 (Ultralytics)
- OpenCV
- SORT/DeepSORT for tracking
- FastAPI for API
- WebSockets for real-time streaming

**Features:**
- Real-time object detection
- Multi-object tracking
- People counting
- Intrusion detection
- Alert system

**Implementation:**

1. **Setup**
```bash
pip install ultralytics opencv-python deep-sort-realtime fastapi uvicorn websockets
```

2. **Core Detection System**
```python
from ultralytics import YOLO
import cv2
from deep_sort_realtime.deepsort_tracker import DeepSort

class SurveillanceSystem:
    def __init__(self, model_path='yolov8n.pt'):
        self.model = YOLO(model_path)
        self.tracker = DeepSort(max_age=30)
        self.people_count = 0
        self.alert_zones = []

    def detect_and_track(self, frame):
        # YOLO detection
        results = self.model(frame)[0]
        detections = []

        for box in results.boxes:
            x1, y1, x2, y2 = box.xyxy[0].cpu().numpy()
            conf = box.conf[0].cpu().item()
            cls = int(box.cls[0].cpu().item())

            if cls == 0 and conf > 0.5:  # Person class
                detections.append([[x1, y1, x2-x1, y2-y1], conf, cls])

        # Tracking
        tracks = self.tracker.update_tracks(detections, frame=frame)

        # Draw boxes and IDs
        for track in tracks:
            if not track.is_confirmed():
                continue
            track_id = track.track_id
            ltrb = track.to_ltrb()

            cv2.rectangle(frame, (int(ltrb[0]), int(ltrb[1])),
                         (int(ltrb[2]), int(ltrb[3])), (0, 255, 0), 2)
            cv2.putText(frame, f'ID: {track_id}', (int(ltrb[0]), int(ltrb[1])-10),
                       cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

        return frame, len(tracks)

    def check_intrusion(self, tracks, zone):
        # Check if any track is in restricted zone
        for track in tracks:
            bbox = track.to_ltrb()
            center_x = (bbox[0] + bbox[2]) / 2
            center_y = (bbox[1] + bbox[3]) / 2

            if self.point_in_polygon((center_x, center_y), zone):
                return True, track.track_id
        return False, None
```

3. **Real-time Processing**
```python
def process_video_stream(source=0):
    system = SurveillanceSystem()
    cap = cv2.VideoCapture(source)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        processed_frame, count = system.detect_and_track(frame)

        # Display info
        cv2.putText(processed_frame, f'People Count: {count}',
                   (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        cv2.imshow('Surveillance', processed_frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
```

4. **Web API**
```python
from fastapi import FastAPI, WebSocket
from fastapi.responses import StreamingResponse
import asyncio

app = FastAPI()

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    system = SurveillanceSystem()
    cap = cv2.VideoCapture(0)

    try:
        while True:
            ret, frame = cap.read()
            if not ret:
                break

            processed_frame, count = system.detect_and_track(frame)

            # Encode frame
            _, buffer = cv2.imencode('.jpg', processed_frame)
            frame_bytes = buffer.tobytes()

            # Send to client
            await websocket.send_bytes(frame_bytes)
            await asyncio.sleep(0.03)  # ~30 FPS

    finally:
        cap.release()
```

**Deliverables:**
- ✅ Real-time detection system
- ✅ Web interface for monitoring
- ✅ Alert system
- ✅ Performance metrics dashboard

---

## Project 4: NLP Multi-Task Application (Day 60)

**Coming in full guide...**

## Project 5: Production RAG Application (Day 75)

**Coming in full guide...**

## Project 6: Production ML System (Day 85)

**Coming in full guide...**

## Project 7: Capstone Project (Days 94-100)

**Coming in full guide...**

---

## 📊 Project Evaluation Criteria

Each project will be evaluated on:

1. **Functionality** (40%)
   - Does it work as intended?
   - Are all features implemented?

2. **Code Quality** (20%)
   - Clean, readable code
   - Proper documentation
   - Following best practices

3. **Performance** (20%)
   - Meets accuracy/speed requirements
   - Optimized for production

4. **Presentation** (20%)
   - Good README
   - Demo video/screenshots
   - User interface (if applicable)

---

**Keep building, keep learning!** 🚀
