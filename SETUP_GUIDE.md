# 🛠️ Setup Guide for 100 Days of AI Engineer

Complete setup instructions for your development environment.

---

## 📋 Table of Contents

1. [System Requirements](#system-requirements)
2. [Python Installation](#python-installation)
3. [Environment Setup](#environment-setup)
4. [Essential Libraries](#essential-libraries)
5. [GPU Setup (Optional)](#gpu-setup-optional)
6. [IDE Configuration](#ide-configuration)
7. [Cloud Setup (Optional)](#cloud-setup-optional)
8. [Verification](#verification)
9. [Troubleshooting](#troubleshooting)

---

## 💻 System Requirements

### Minimum Requirements
- **OS:** Windows 10/11, macOS 10.15+, or Linux (Ubuntu 20.04+)
- **RAM:** 8 GB (16 GB recommended)
- **Storage:** 20 GB free space (50 GB recommended for datasets)
- **CPU:** Multi-core processor (Intel i5/AMD Ryzen 5 or better)

### Recommended for Deep Learning
- **RAM:** 16-32 GB
- **GPU:** NVIDIA GPU with 6+ GB VRAM (RTX 3060 or better)
- **Storage:** 100+ GB SSD (for datasets and models)

---

## 🐍 Python Installation

### Option 1: Anaconda (Recommended for Beginners)

**Why Anaconda?**
- Pre-installed scientific packages
- Easy environment management
- Cross-platform compatibility

**Installation:**

1. Download Anaconda from [anaconda.com](https://www.anaconda.com/download)

2. Install Anaconda:
   - **Windows:** Run the `.exe` installer
   - **macOS:** Run the `.pkg` installer
   - **Linux:**
   ```bash
   bash Anaconda3-2024.02-Linux-x86_64.sh
   ```

3. Verify installation:
   ```bash
   conda --version
   python --version  # Should be 3.10+
   ```

### Option 2: Python.org + pip

1. Download Python 3.10+ from [python.org](https://www.python.org/downloads/)

2. Install with "Add to PATH" checked

3. Verify:
   ```bash
   python --version
   pip --version
   ```

4. Install virtualenv:
   ```bash
   pip install virtualenv
   ```

---

## 🌍 Environment Setup

### Using Conda (Recommended)

```bash
# Create environment
conda create -n ai-engineer python=3.10 -y

# Activate environment
conda activate ai-engineer

# Verify
which python  # Should point to conda environment
```

### Using venv (Alternative)

```bash
# Create environment
python -m venv ai-engineer-env

# Activate environment
# Windows:
ai-engineer-env\Scripts\activate
# macOS/Linux:
source ai-engineer-env/bin/activate

# Verify
which python  # Should point to venv
```

---

## 📦 Essential Libraries

### Phase 1: Foundations & Classical ML

```bash
# Data manipulation and visualization
pip install numpy pandas matplotlib seaborn plotly

# Machine learning
pip install scikit-learn xgboost lightgbm

# Jupyter notebook
pip install jupyter jupyterlab ipykernel

# Utilities
pip install tqdm requests pillow
```

### Phase 2-3: Deep Learning & Computer Vision

```bash
# PyTorch (CPU version - see GPU section for CUDA version)
pip install torch torchvision torchaudio

# Computer vision
pip install opencv-python opencv-contrib-python
pip install albumentations
pip install timm  # PyTorch Image Models

# Object detection
pip install ultralytics  # YOLOv8
```

### Phase 4-5: NLP & LLMs

```bash
# NLP basics
pip install nltk spacy

# Download spaCy model
python -m spacy download en_core_web_sm

# Transformers and LLMs
pip install transformers datasets accelerate
pip install sentence-transformers

# LLM frameworks
pip install langchain openai anthropic
pip install chromadb faiss-cpu
pip install tiktoken
```

### Phase 6: MLOps & Deployment

```bash
# Web frameworks
pip install fastapi uvicorn[standard]
pip install streamlit gradio

# Experiment tracking
pip install mlflow wandb

# Model serving
pip install bentoml

# Utilities
pip install python-multipart aiofiles
```

### Complete Installation (All at Once)

Save this as `requirements.txt`:

```txt
# Data Science
numpy==1.24.3
pandas==2.0.3
matplotlib==3.7.2
seaborn==0.12.2
plotly==5.15.0

# Classical ML
scikit-learn==1.3.0
xgboost==1.7.6
lightgbm==4.0.0
imbalanced-learn==0.11.0

# Deep Learning
torch==2.0.1
torchvision==0.15.2
torchaudio==2.0.2

# Computer Vision
opencv-python==4.8.0.74
albumentations==1.3.1
timm==0.9.5
ultralytics==8.0.147

# NLP
nltk==3.8.1
spacy==3.6.0
transformers==4.31.0
datasets==2.14.3
sentence-transformers==2.2.2

# LLMs
langchain==0.0.267
openai==0.27.8
chromadb==0.4.6
faiss-cpu==1.7.4
tiktoken==0.4.0

# MLOps
mlflow==2.5.0
wandb==0.15.8
fastapi==0.101.0
uvicorn==0.23.2
streamlit==1.25.0
gradio==3.39.0

# Utilities
jupyter==1.0.0
jupyterlab==4.0.3
tqdm==4.65.0
requests==2.31.0
pillow==10.0.0
python-dotenv==1.0.0
```

Install all:
```bash
pip install -r requirements.txt
```

---

## 🚀 GPU Setup (Optional but Recommended)

### Check GPU Availability

```bash
# For NVIDIA GPUs
nvidia-smi
```

### Install CUDA-enabled PyTorch

**For CUDA 11.8:**
```bash
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
```

**For CUDA 12.1:**
```bash
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
```

**Verify GPU:**
```python
import torch
print(f"CUDA available: {torch.cuda.is_available()}")
print(f"CUDA version: {torch.version.cuda}")
print(f"Device: {torch.cuda.get_device_name(0)}")
```

### Install TensorFlow with GPU

```bash
pip install tensorflow[and-cuda]
```

---

## 🔧 IDE Configuration

### VS Code Setup

1. **Install VS Code**
   - Download from [code.visualstudio.com](https://code.visualstudio.com/)

2. **Install Extensions:**
   - Python (Microsoft)
   - Jupyter
   - Pylance
   - Python Docstring Generator
   - GitLens
   - Docker (if using containers)

3. **Select Python Interpreter:**
   - Press `Ctrl+Shift+P` (Cmd+Shift+P on macOS)
   - Type "Python: Select Interpreter"
   - Choose your `ai-engineer` environment

4. **Configure Settings (settings.json):**
```json
{
    "python.linting.enabled": true,
    "python.linting.pylintEnabled": true,
    "python.formatting.provider": "black",
    "editor.formatOnSave": true,
    "python.terminal.activateEnvironment": true
}
```

### Jupyter Setup

```bash
# Install Jupyter extensions
pip install jupyter_contrib_nbextensions
jupyter contrib nbextension install --user

# Enable useful extensions
jupyter nbextension enable codefolding/main
jupyter nbextension enable execute_time/ExecuteTime
jupyter nbextension enable toc2/main
```

**Launch Jupyter:**
```bash
# Classic Notebook
jupyter notebook

# JupyterLab (recommended)
jupyter lab
```

### PyCharm Setup (Alternative)

1. Download PyCharm from [jetbrains.com/pycharm](https://www.jetbrains.com/pycharm/)
2. Create new project
3. Select existing interpreter (your conda/venv environment)
4. Install plugins: Jupyter, Markdown, .ignore

---

## ☁️ Cloud Setup (Optional)

### Google Colab

**Pros:** Free GPU, no setup
**Cons:** Session limits, storage limits

**Usage:**
1. Go to [colab.research.google.com](https://colab.research.google.com/)
2. Create new notebook
3. Runtime → Change runtime type → GPU

**Mount Google Drive:**
```python
from google.colab import drive
drive.mount('/content/drive')
```

### Kaggle Notebooks

**Pros:** Free GPU/TPU, datasets integrated
**Cons:** Internet disabled for competitions

**Usage:**
1. Sign up at [kaggle.com](https://www.kaggle.com/)
2. Create new notebook
3. Settings → Accelerator → GPU

### AWS/GCP/Azure Setup

For advanced users needing more compute:

**AWS SageMaker:**
```bash
pip install sagemaker boto3
```

**Google Cloud Vertex AI:**
```bash
pip install google-cloud-aiplatform
```

---

## ✅ Verification

### Create Verification Script

Save as `verify_setup.py`:

```python
import sys
print(f"Python version: {sys.version}")

# Test imports
packages = [
    'numpy', 'pandas', 'matplotlib', 'seaborn',
    'sklearn', 'torch', 'torchvision',
    'cv2', 'transformers', 'fastapi'
]

print("\n📦 Package Verification:")
for package in packages:
    try:
        __import__(package)
        print(f"✅ {package}")
    except ImportError:
        print(f"❌ {package} - NOT INSTALLED")

# GPU check
try:
    import torch
    print(f"\n🎮 GPU Status:")
    print(f"CUDA available: {torch.cuda.is_available()}")
    if torch.cuda.is_available():
        print(f"GPU: {torch.cuda.get_device_name(0)}")
        print(f"CUDA version: {torch.version.cuda}")
except:
    print("❌ PyTorch not installed")

print("\n✅ Setup verification complete!")
```

**Run:**
```bash
python verify_setup.py
```

---

## 🔧 Troubleshooting

### Common Issues

**1. Import Error: Module not found**
```bash
# Make sure you're in the right environment
conda activate ai-engineer
# or
source ai-engineer-env/bin/activate

# Reinstall package
pip install <package-name>
```

**2. CUDA not available in PyTorch**
```bash
# Reinstall PyTorch with CUDA
pip uninstall torch torchvision torchaudio
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
```

**3. Jupyter kernel not found**
```bash
python -m ipykernel install --user --name=ai-engineer
```

**4. Permission denied (Linux/macOS)**
```bash
# Use --user flag
pip install --user <package-name>
```

**5. SSL Certificate error**
```bash
pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org <package>
```

**6. Memory errors during training**
```python
# Reduce batch size
batch_size = 16  # try 8 or 4

# Use gradient accumulation
for i, (data, target) in enumerate(train_loader):
    loss = model(data, target)
    loss = loss / accumulation_steps
    loss.backward()

    if (i + 1) % accumulation_steps == 0:
        optimizer.step()
        optimizer.zero_grad()
```

### Getting Help

1. **Check error messages carefully**
2. **Search Stack Overflow**
3. **Check package GitHub issues**
4. **Ask in Discord communities**
5. **Use ChatGPT/Claude for debugging**

---

## 📂 Recommended Directory Structure

```bash
100DaysOfAIEngineer/
├── data/
│   ├── raw/
│   ├── processed/
│   └── external/
├── notebooks/
│   ├── 01_exploration/
│   ├── 02_experiments/
│   └── 03_analysis/
├── src/
│   ├── __init__.py
│   ├── data/
│   ├── models/
│   ├── utils/
│   └── visualization/
├── models/
│   ├── saved_models/
│   └── checkpoints/
├── reports/
│   ├── figures/
│   └── results/
├── projects/
│   ├── project1/
│   ├── project2/
│   └── ...
├── requirements.txt
├── README.md
└── .gitignore
```

**Create structure:**
```bash
mkdir -p data/{raw,processed,external}
mkdir -p notebooks/{01_exploration,02_experiments,03_analysis}
mkdir -p src/{data,models,utils,visualization}
mkdir -p models/{saved_models,checkpoints}
mkdir -p reports/{figures,results}
mkdir -p projects
```

---

## 🎯 Next Steps

After setup is complete:

1. ✅ Verify all installations
2. ✅ Create GitHub repository
3. ✅ Clone this repo
4. ✅ Start Day 1!

---

## 🆘 Support

If you encounter issues:
- Create an issue on GitHub
- Join the Discord community
- Check RESOURCES.md for help

---

**You're all set! Let's start learning!** 🚀
