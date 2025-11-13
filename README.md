# 🚀 100 Days of AI Engineer

> A comprehensive, project-driven roadmap to becoming an AI Engineer in 100 days

## 📋 Overview

This is a structured 100-day program designed to transform you from a Python developer into a skilled AI Engineer. The curriculum is **project-focused**, **hands-on**, and covers the **modern AI stack** used in production environments.

### 📅 NEW! Daily Checklists with Social Media Templates

**🎯 [Daily Checklists Directory](daily_checklists/)** - Track your progress day by day!

Each day includes:
- ✅ **Checklist format** - Mark tasks as you complete them
- ✅ **Learning objectives** - Clear daily goals
- ✅ **Coding tasks** - Specific implementations
- ✅ **Social media templates** - Ready-to-post updates for Twitter, LinkedIn, Instagram
- ✅ **Reflection prompts** - Document your journey

**Why share on social media?**
- 📢 Accountability through public commitment
- 🤝 Connect with other learners (#100DaysOfAIEngineer)
- 💼 Build your professional brand
- 📊 Track your progress publicly
- 🎯 Stay motivated through community support

**👉 Start with [Day 1 Checklist](daily_checklists/day01.md)**

### What You'll Build

- 7 Major Real-World Projects
- 15+ Mini Projects
- Production-ready ML/AI applications
- Full MLOps pipeline
- LLM-powered applications

### Prerequisites

- ✅ Python programming knowledge
- ✅ Basic understanding of programming concepts
- ✅ Willingness to code daily
- ✅ 2-4 hours daily commitment

---

## 🎯 Learning Path

```
Phase 1: Foundations & Classical ML (Days 1-15)
Phase 2: Deep Learning Fundamentals (Days 16-30)
Phase 3: Computer Vision (Days 31-45)
Phase 4: Natural Language Processing (Days 46-60)
Phase 5: LLMs & Modern NLP (Days 61-75)
Phase 6: MLOps & Production (Days 76-85)
Phase 7: Capstone & Advanced Topics (Days 86-100)
```

---

## 📚 Phase 1: Foundations & Classical ML (Days 1-15)

**Goal:** Master data manipulation, classical ML algorithms, and build your first ML pipeline

### Week 1: Python for AI & Data Science

**Day 1-2: NumPy Mastery**
- Array operations, broadcasting, vectorization
- Linear algebra operations (dot products, matrix multiplication)
- Random sampling and statistical operations
- **Exercise:** Implement matrix operations from scratch
- **Mini Project:** Build a simple image filter using NumPy

**Day 3-4: Pandas for Data Manipulation**
- DataFrames, Series, indexing
- Data cleaning, handling missing values
- Groupby, pivot tables, merging
- **Exercise:** Analyze a real dataset (Kaggle dataset)
- **Mini Project:** COVID-19 data analysis dashboard

**Day 5-6: Data Visualization**
- Matplotlib, Seaborn, Plotly
- Statistical plots, distributions
- Interactive visualizations
- **Mini Project:** Exploratory Data Analysis (EDA) on Titanic dataset

**Day 7: Mathematics for ML**
- Linear algebra review (vectors, matrices, eigenvalues)
- Calculus basics (derivatives, gradients)
- Probability and statistics fundamentals
- **Exercise:** Implement gradient descent from scratch

### Week 2: Classical Machine Learning

**Day 8-9: Supervised Learning - Regression**
- Linear regression (theory + implementation from scratch)
- Polynomial regression, regularization (Ridge, Lasso)
- Gradient descent optimization
- **Exercise:** Predict house prices using linear regression
- **Code:** Implement linear regression without sklearn

**Day 10-11: Supervised Learning - Classification**
- Logistic regression
- Decision trees and Random Forests
- Support Vector Machines (SVM)
- **Exercise:** Binary and multi-class classification problems
- **Mini Project:** Spam email classifier

**Day 12-13: Unsupervised Learning**
- K-Means clustering
- Hierarchical clustering
- Principal Component Analysis (PCA)
- DBSCAN
- **Mini Project:** Customer segmentation using clustering

**Day 14: Model Evaluation & Feature Engineering**
- Cross-validation, train-test split
- Metrics: Accuracy, Precision, Recall, F1, ROC-AUC
- Feature scaling, encoding categorical variables
- Handling imbalanced datasets
- **Exercise:** Compare multiple models on a dataset

**Day 15: 🎯 PROJECT 1 - End-to-End ML Pipeline**
- **Build:** Complete ML pipeline for a real-world problem
- Data collection and cleaning
- Feature engineering and selection
- Model training, evaluation, hyperparameter tuning
- **Deliverable:** Jupyter notebook with full pipeline
- **Suggested:** Predict customer churn or credit card fraud detection

---

## 🧠 Phase 2: Deep Learning Fundamentals (Days 16-30)

**Goal:** Understand neural networks and implement deep learning models

### Week 3: Neural Networks from Scratch

**Day 16-17: Neural Network Fundamentals**
- Perceptron, activation functions
- Forward propagation
- Loss functions (MSE, Cross-entropy)
- **Exercise:** Implement a perceptron from scratch

**Day 18-19: Backpropagation**
- Chain rule and backpropagation algorithm
- Gradient descent variants (SGD, Momentum, Adam)
- **Exercise:** Implement backpropagation from scratch
- **Code:** Build a 2-layer neural network without frameworks

**Day 20-21: Introduction to PyTorch**
- Tensors, autograd, computational graphs
- Building models with nn.Module
- Training loops, optimizers
- **Exercise:** Reimplement Day 19 network in PyTorch
- **Mini Project:** MNIST digit classification

**Day 22: Regularization & Optimization**
- Dropout, Batch Normalization, L1/L2 regularization
- Learning rate scheduling
- Early stopping
- **Exercise:** Prevent overfitting on a deep network

### Week 4: Advanced Deep Learning

**Day 23-24: Convolutional Neural Networks (CNNs) - Part 1**
- Convolution operation, pooling
- CNN architectures (LeNet, AlexNet)
- **Exercise:** Visualize filters and feature maps
- **Code:** Build a simple CNN for image classification

**Day 25-26: CNNs - Part 2 & Transfer Learning**
- Modern architectures (VGG, ResNet, EfficientNet)
- Transfer learning and fine-tuning
- Data augmentation
- **Mini Project:** Fine-tune ResNet on a custom dataset

**Day 27-28: Recurrent Neural Networks (RNNs)**
- Sequence modeling, RNN architecture
- LSTM and GRU
- Vanishing gradient problem
- **Exercise:** Time series prediction with LSTM
- **Mini Project:** Stock price prediction

**Day 29: Handling Real-World Data**
- Data preprocessing pipelines
- DataLoaders and Dataset classes in PyTorch
- Handling large datasets
- **Exercise:** Build efficient data pipelines

**Day 30: 🎯 PROJECT 2 - Image Classification System**
- **Build:** End-to-end image classifier with web interface
- Custom dataset creation and preprocessing
- Train CNN from scratch + transfer learning comparison
- Model evaluation and visualization
- **Deliverable:** Streamlit/Gradio app for image classification
- **Suggested:** Plant disease classifier or animal species identifier

---

## 👁️ Phase 3: Computer Vision (Days 31-45)

**Goal:** Master computer vision techniques and build production-ready CV applications

### Week 5: Advanced Computer Vision

**Day 31-32: Object Detection - Part 1**
- R-CNN family (R-CNN, Fast R-CNN, Faster R-CNN)
- YOLO (You Only Look Once) architecture
- **Exercise:** Understand anchor boxes and IoU
- **Code:** Implement basic object detection with YOLOv5

**Day 33-34: Object Detection - Part 2**
- YOLOv8, DETR (Detection Transformer)
- Non-maximum suppression (NMS)
- mAP (mean Average Precision) metric
- **Mini Project:** Real-time object detection with webcam

**Day 35-36: Semantic Segmentation**
- U-Net architecture
- Mask R-CNN
- DeepLab
- **Exercise:** Image segmentation on medical images
- **Mini Project:** Background removal tool

**Day 37: Instance Segmentation & Pose Estimation**
- Instance segmentation with Mask R-CNN
- Human pose estimation (OpenPose, MediaPipe)
- **Mini Project:** Pose-based fitness rep counter

### Week 6: Advanced CV Techniques

**Day 38-39: Generative Models - Part 1**
- Autoencoders and Variational Autoencoders (VAE)
- Image denoising and reconstruction
- **Exercise:** Build an autoencoder for MNIST
- **Mini Project:** Image denoising application

**Day 40-41: Generative Models - Part 2 (GANs)**
- Generative Adversarial Networks (GANs)
- DCGAN, StyleGAN basics
- GAN training challenges
- **Mini Project:** Generate synthetic images

**Day 42-43: Modern CV Techniques**
- Vision Transformers (ViT)
- CLIP (Contrastive Language-Image Pre-training)
- Image captioning
- **Exercise:** Use CLIP for zero-shot classification
- **Mini Project:** Image search engine using CLIP

**Day 44: Model Optimization for CV**
- Model quantization and pruning
- ONNX export
- TensorRT optimization
- **Exercise:** Optimize a model for edge deployment

**Day 45: 🎯 PROJECT 3 - Smart Surveillance System**
- **Build:** Real-time object detection and tracking system
- Multiple object tracking (MOT)
- Alert system for specific objects/behaviors
- Performance optimization for real-time processing
- **Deliverable:** Real-time video analysis application
- **Suggested:** People counter, vehicle detection, or safety monitoring

---

## 💬 Phase 4: Natural Language Processing (Days 46-60)

**Goal:** Master NLP fundamentals and build text-based AI applications

### Week 7: NLP Fundamentals

**Day 46-47: Text Preprocessing & Feature Engineering**
- Tokenization, stemming, lemmatization
- Stop words removal, text cleaning
- Bag of Words, TF-IDF
- **Exercise:** Build a text preprocessing pipeline
- **Mini Project:** Document similarity finder

**Day 48-49: Word Embeddings**
- Word2Vec (CBOW, Skip-gram)
- GloVe, FastText
- Embedding visualization (t-SNE)
- **Exercise:** Train custom word embeddings
- **Mini Project:** Word analogy solver (king - man + woman = queen)

**Day 50-51: Text Classification**
- Sentiment analysis
- Naive Bayes, Logistic Regression for text
- Deep learning for text (CNN, LSTM)
- **Mini Project:** Movie review sentiment classifier
- **Exercise:** Multi-label text classification

**Day 52: Named Entity Recognition (NER)**
- NER with spaCy
- Custom NER models
- **Mini Project:** Extract entities from news articles

### Week 8: Sequence Models & Attention

**Day 53-54: Sequence-to-Sequence Models**
- Encoder-decoder architecture
- Seq2Seq with attention
- **Exercise:** Build a simple translation model
- **Mini Project:** Text summarization tool

**Day 55-56: Attention Mechanism & Transformers**
- Self-attention, multi-head attention
- Transformer architecture deep dive
- Positional encoding
- **Exercise:** Implement self-attention from scratch
- **Code:** Build a mini transformer

**Day 57-58: Pre-trained Language Models**
- BERT, RoBERTa, DistilBERT
- Fine-tuning BERT for classification
- Feature extraction with BERT
- **Mini Project:** Question-answering system with BERT

**Day 59: Advanced NLP Tasks**
- Text generation
- Zero-shot classification
- Few-shot learning with GPT
- **Exercise:** Experiment with Hugging Face Transformers

**Day 60: 🎯 PROJECT 4 - NLP Multi-Task Application**
- **Build:** Comprehensive text analysis tool
- Sentiment analysis
- Named entity recognition
- Text summarization
- Topic modeling
- **Deliverable:** Web API (FastAPI) with multiple NLP endpoints
- **Suggested:** News article analyzer or social media insights tool

---

## 🤖 Phase 5: Large Language Models & Modern NLP (Days 61-75)

**Goal:** Master LLMs, RAG systems, and build production LLM applications

### Week 9: Large Language Models

**Day 61-62: Understanding LLMs**
- GPT architecture deep dive
- Tokenization (BPE, WordPiece)
- LLM training process (pre-training, fine-tuning)
- **Exercise:** Explore GPT-2/GPT-3 API
- **Mini Project:** Text completion app

**Day 63-64: Prompt Engineering**
- Zero-shot, few-shot, chain-of-thought prompting
- Prompt templates and optimization
- In-context learning
- **Exercise:** Build a prompt library for common tasks
- **Mini Project:** AI assistant with optimized prompts

**Day 65-66: Fine-Tuning LLMs**
- Full fine-tuning vs LoRA vs QLoRA
- Parameter-efficient fine-tuning (PEFT)
- Instruction tuning
- **Exercise:** Fine-tune a small LLM (Flan-T5, GPT-2)
- **Mini Project:** Domain-specific chatbot

**Day 67-68: LangChain Framework**
- LangChain basics (chains, agents, memory)
- Prompt templates and output parsers
- LLM chains and sequential chains
- **Exercise:** Build complex chains
- **Mini Project:** Research assistant with LangChain

### Week 10: RAG & Vector Databases

**Day 69-70: Vector Databases & Embeddings**
- Embedding models (OpenAI, Sentence-Transformers)
- Vector databases (Pinecone, Weaviate, ChromaDB, FAISS)
- Similarity search
- **Exercise:** Build a semantic search engine
- **Mini Project:** Document similarity search

**Day 71-72: Retrieval-Augmented Generation (RAG)**
- RAG architecture and workflow
- Document loading, chunking strategies
- Retrieval optimization
- **Exercise:** Build a basic RAG system
- **Mini Project:** "Chat with your PDF" application

**Day 73: Advanced RAG Techniques**
- Hybrid search (keyword + semantic)
- Re-ranking and MMR (Maximal Marginal Relevance)
- Metadata filtering
- **Exercise:** Improve RAG system accuracy

**Day 74: LLM Evaluation & Safety**
- Evaluation metrics for LLMs
- Guardrails and content filtering
- Handling hallucinations
- Cost optimization
- **Exercise:** Benchmark different LLM approaches

**Day 75: 🎯 PROJECT 5 - Production RAG Application**
- **Build:** ChatGPT-like application with custom knowledge base
- Multi-document RAG system
- Conversation memory and context management
- Source attribution
- **Deliverable:** Full-stack application (FastAPI + React/Streamlit)
- **Suggested:** Company knowledge base chatbot or legal document Q&A

---

## 🚀 Phase 6: MLOps & Production (Days 76-85)

**Goal:** Learn to deploy, monitor, and maintain ML models in production

### Week 11: Deployment & MLOps

**Day 76-77: Model Serving & APIs**
- FastAPI for ML models
- REST API design for ML
- Request/response handling
- Model versioning
- **Exercise:** Create API endpoints for multiple models
- **Mini Project:** Model serving API with FastAPI

**Day 78: Docker for ML**
- Containerization basics
- Docker for ML applications
- Multi-stage builds
- **Exercise:** Dockerize ML application
- **Mini Project:** Docker Compose setup for ML app + database

**Day 79: Model Optimization**
- Model quantization (int8, fp16)
- Knowledge distillation
- ONNX Runtime
- **Exercise:** Optimize model for inference
- **Mini Project:** Compare inference speeds

**Day 80-81: ML Experiment Tracking**
- MLflow for experiment tracking
- Weights & Biases (W&B)
- Model registry
- **Exercise:** Track experiments for a model
- **Mini Project:** Complete ML experiment pipeline

**Day 82: Model Monitoring & Observability**
- Model drift detection
- Data drift monitoring
- Logging and alerting
- **Exercise:** Set up monitoring dashboard
- **Tools:** Evidently AI, WhyLabs

**Day 83: CI/CD for ML**
- GitHub Actions for ML
- Automated testing for ML code
- Continuous training
- **Exercise:** Build CI/CD pipeline
- **Mini Project:** Automated model retraining pipeline

**Day 84: Cloud Deployment**
- AWS SageMaker basics (or GCP Vertex AI)
- Serverless deployment (AWS Lambda)
- Scaling strategies
- **Exercise:** Deploy model to cloud

**Day 85: 🎯 PROJECT 6 - Production ML System**
- **Build:** End-to-end production ML system
- Model training pipeline
- Automated deployment
- Monitoring and alerting
- CI/CD integration
- **Deliverable:** Fully deployed, monitored ML application
- **Suggested:** Real-time recommendation system or fraud detection

---

## 🏆 Phase 7: Capstone & Advanced Topics (Days 86-100)

**Goal:** Build a comprehensive AI project and explore cutting-edge topics

### Week 12-13: Advanced Topics

**Day 86-87: Multi-Modal AI**
- Vision-language models (CLIP, BLIP)
- Audio processing (Whisper)
- Multi-modal applications
- **Mini Project:** Image captioning or visual question answering

**Day 88-89: AI Agents & LangGraph**
- Autonomous agents
- ReAct framework
- Tool use with LLMs
- **Mini Project:** AI agent that can browse and use tools

**Day 90-91: Reinforcement Learning Basics**
- MDP, Q-learning basics
- Policy gradients
- RL for practical applications
- **Exercise:** Train an agent in a simple environment
- **Mini Project:** Game-playing AI

**Day 92-93: Advanced Generative AI**
- Stable Diffusion and image generation
- ControlNet, LoRA for Stable Diffusion
- Text-to-image applications
- **Mini Project:** AI art generator

**Day 94-100: 🎯 CAPSTONE PROJECT - Full-Stack AI Application**

Build a comprehensive, production-ready AI application that combines multiple concepts:

**Project Ideas:**
1. **AI-Powered Content Platform**
   - Text generation, image generation
   - RAG-based Q&A
   - Content moderation
   - User analytics

2. **Intelligent Personal Assistant**
   - Voice input (Whisper)
   - Multi-turn conversations with memory
   - Tool use (calendar, email, web search)
   - Task automation

3. **AI-Powered Healthcare Assistant**
   - Medical image analysis
   - Symptom checker with RAG
   - Health record summarization
   - Privacy-preserving design

4. **Smart Education Platform**
   - Personalized learning paths
   - Auto-grading with explanations
   - Interactive tutoring chatbot
   - Progress tracking

**Requirements:**
- Frontend (React/Vue or Streamlit)
- Backend API (FastAPI)
- Multiple AI models (CV + NLP + LLM)
- Database integration
- Authentication & authorization
- Docker deployment
- Monitoring and logging
- Documentation

**Deliverables:**
- Complete codebase on GitHub
- Deployed application
- Technical documentation
- Demo video
- Blog post explaining architecture

---

## 🛠️ Tech Stack & Tools

### Essential Tools
- **Languages:** Python
- **DL Frameworks:** PyTorch, TensorFlow/Keras
- **ML Libraries:** scikit-learn, XGBoost, LightGBM
- **NLP:** Hugging Face Transformers, spaCy, NLTK
- **LLM:** OpenAI API, LangChain, LlamaIndex
- **Vector DBs:** ChromaDB, FAISS, Pinecone
- **Computer Vision:** OpenCV, torchvision, timm
- **Data:** NumPy, Pandas, Polars
- **Visualization:** Matplotlib, Seaborn, Plotly
- **MLOps:** MLflow, Weights & Biases, DVC
- **Deployment:** FastAPI, Docker, AWS/GCP
- **Version Control:** Git, GitHub

### Development Environment
```bash
# Create conda environment
conda create -n ai-engineer python=3.10
conda activate ai-engineer

# Install core packages
pip install torch torchvision torchaudio
pip install transformers datasets
pip install langchain openai chromadb
pip install fastapi uvicorn
pip install mlflow wandb
pip install streamlit gradio
pip install scikit-learn pandas numpy matplotlib seaborn
```

---

## 📊 Progress Tracking

Create a daily log:

```markdown
## Day X: [Topic]

### What I Learned
- Key concept 1
- Key concept 2

### Code Implemented
- [Link to code/notebook]

### Challenges Faced
- Challenge and how I solved it

### Resources Used
- Tutorial/article links

### Tomorrow's Goal
- What I plan to learn next
```

---

## 🎓 Learning Resources

### 📝 Blog Articles (NEW!)

**🔥 [BLOG_ARTICLES.md](BLOG_ARTICLES.md) - 150+ Curated Blog Posts**

We've researched and compiled **150+ high-quality blog articles** from trusted sources for every topic in the curriculum:

- ✅ **Organized by Phase**: Articles matched to each day's learning
- ✅ **2024-2025 Content**: Latest tutorials and best practices
- ✅ **Code Examples**: All include practical implementations
- ✅ **Verified Quality**: Hand-picked from top platforms (Medium, Towards Data Science, official docs)

**Topics Include:** NumPy, Pandas, ML algorithms, PyTorch, CNNs, YOLO, NLP, BERT, Transformers, LLMs, Fine-tuning, RAG, LangChain, Vector Databases, MLOps, Docker, and more!

**👉 See [BLOG_ARTICLES.md](BLOG_ARTICLES.md) for the complete collection**

Also check [RESOURCES.md](RESOURCES.md) for comprehensive books, courses, tools, and platforms.

---

### Free Courses
- **Fast.ai** - Practical Deep Learning
- **Stanford CS229** - Machine Learning
- **Stanford CS224N** - NLP with Deep Learning
- **DeepLearning.AI** - Deep Learning Specialization
- **Hugging Face Course** - NLP with Transformers

### Books
- "Hands-On Machine Learning" by Aurélien Géron
- "Deep Learning" by Ian Goodfellow
- "Natural Language Processing with Transformers" by Lewis Tunstall
- "Designing Machine Learning Systems" by Chip Huyen

### Platforms
- **Kaggle** - Competitions and datasets
- **Papers with Code** - Latest research
- **Hugging Face** - Models and datasets
- **GitHub** - Open source projects

### YouTube Channels
- Andrej Karpathy
- StatQuest
- 3Blue1Brown (Math)
- Yannic Kilcher (Paper reviews)

---

## 💡 Tips for Success

1. **Code Every Day** - Even 30 minutes counts
2. **Build Projects** - Theory without practice is useless
3. **Read Research Papers** - Stay updated with latest techniques
4. **Join Communities** - Reddit (r/MachineLearning), Discord servers
5. **Document Your Journey** - Blog, GitHub, LinkedIn posts
6. **Don't Just Tutorial Hell** - Build original projects
7. **Understand, Don't Memorize** - Focus on concepts, not code
8. **Debug and Experiment** - Break things and fix them
9. **Review Regularly** - Revisit concepts weekly
10. **Stay Consistent** - 100 days straight is better than random practice

---

## 🎯 Success Metrics

By Day 100, you should be able to:

✅ Build and deploy ML models end-to-end
✅ Implement neural networks from scratch
✅ Fine-tune and deploy LLMs
✅ Create RAG applications
✅ Build computer vision applications
✅ Design and implement MLOps pipelines
✅ Read and implement research papers
✅ Contribute to open source ML projects
✅ Pass AI Engineer technical interviews

---

## 📁 Repository Structure

```
100DaysOfAIEngineer/
├── Phase1_Foundations/
│   ├── day01_numpy/
│   ├── day02_pandas/
│   └── ...
├── Phase2_DeepLearning/
├── Phase3_ComputerVision/
├── Phase4_NLP/
├── Phase5_LLMs/
├── Phase6_MLOps/
├── Phase7_Capstone/
├── projects/
│   ├── project1_ml_pipeline/
│   ├── project2_image_classifier/
│   └── ...
├── resources/
│   ├── cheatsheets/
│   ├── papers/
│   └── datasets/
└── daily_logs/
    ├── week01.md
    └── ...
```

---

## 🤝 Contributing

Found an error or want to improve the curriculum? Feel free to:
- Open an issue
- Submit a pull request
- Share your progress and projects

---

## 📜 License

MIT License - Feel free to use and adapt this roadmap for your learning journey!

---

## 🚀 Let's Begin!

Start with Day 1 and commit to the journey. Remember: **Consistency beats intensity.**

**Your AI Engineering journey starts now!** 🎉

---

**Created with ❤️ for aspiring AI Engineers**

*Last Updated: 2025*
