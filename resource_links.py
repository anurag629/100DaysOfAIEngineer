#!/usr/bin/env python3
"""
Comprehensive resource links for all 100 days
Real, verified links from web searches (2024-2025)
"""

# DataWars links
DATAWARS_BASE = "https://www.datawars.io"
DATAWARS_PANDAS = f"{DATAWARS_BASE}/data-science-skill-track/intro-to-pandas-for-data-analysis"
DATAWARS_PROJECTS = f"{DATAWARS_BASE}/articles/12-free-data-science-projects-to-practice-python-and-pandas"

# PyTorch links
PYTORCH_TUTORIALS = "https://pytorch.org/tutorials/"
PYTORCH_BASICS = "https://pytorch.org/tutorials/beginner/basics/intro.html"
PYTORCH_60MIN = "https://pytorch.org/tutorials/beginner/deep_learning_60min_blitz.html"
LEARN_PYTORCH = "https://www.learnpytorch.io/"

# Hugging Face links
HF_TRANSFORMERS = "https://huggingface.co/docs/transformers/"
HF_TRAINING = "https://huggingface.co/docs/transformers/en/training"
HF_BERT = "https://huggingface.co/docs/transformers/en/model_doc/bert"

# LangChain/RAG links
LANGCHAIN_RAG = "https://python.langchain.com/docs/tutorials/rag/"
LANGCHAIN_DOCS = "https://python.langchain.com/docs/introduction/"

# FastAPI links
FASTAPI_DOCS = "https://fastapi.tiangolo.com/"
FASTAPI_ML = "https://blog.jetbrains.com/pycharm/2024/09/how-to-use-fastapi-for-machine-learning/"

# MLOps links
MLFLOW_DOCS = "https://mlflow.org/docs/latest/index.html"
MLOPS_GUIDE = "https://towardsdatascience.com/machine-learning-operations-mlops-for-beginners-a5686bfe02b2/"

# Topic-specific resource mapping
TOPIC_RESOURCES = {
    # Phase 1: Foundations & Classical ML (Days 1-15)
    "numpy": {
        "articles": [
            "[NumPy Quickstart Tutorial](https://numpy.org/doc/stable/user/quickstart.html) - Official docs",
            "[NumPy for Absolute Beginners](https://numpy.org/doc/stable/user/absolute_beginners.html) - Getting started",
            "[NumPy Array Programming](https://realpython.com/numpy-array-programming/) - Real Python guide"
        ],
        "videos": [
            "[NumPy Tutorial by freeCodeCamp](https://www.youtube.com/watch?v=QUT1VHiLmmI) - 90 min comprehensive",
            "[NumPy Crash Course](https://www.youtube.com/watch?v=8Y0qQEh7dJg) - 30 mins quickstart"
        ],
        "practice": [
            "[100 NumPy Exercises](https://github.com/rougier/numpy-100) - Progressive difficulty",
            "[W3Schools NumPy](https://www.w3schools.com/python/numpy/) - Interactive tutorials",
            "[HackerRank Python](https://www.hackerrank.com/domains/python) - NumPy challenges",
            f"[DataWars Projects]({DATAWARS_BASE}) - Real-world practice"
        ],
        "interactive": [
            "[Google Colab](https://colab.research.google.com) - Free GPU notebooks",
            "[Kaggle Learn Python](https://www.kaggle.com/learn/python) - Interactive course",
            "[Exercism Python Track](https://exercism.org/tracks/python) - Mentored exercises"
        ]
    },

    "pandas": {
        "articles": [
            "[Pandas Documentation](https://pandas.pydata.org/docs/user_guide/index.html) - Official guide",
            "[10 Minutes to Pandas](https://pandas.pydata.org/docs/user_guide/10min.html) - Quick intro",
            "[Pandas Tutorial](https://www.w3schools.com/python/pandas/) - W3Schools guide"
        ],
        "videos": [
            "[Pandas Tutorial by Corey Schafer](https://www.youtube.com/watch?v=ZyhVh-qRZPA) - Complete series",
            "[Data Analysis with Pandas](https://www.youtube.com/watch?v=vmEHCJofslg) - FreeCodeCamp"
        ],
        "practice": [
            f"[12 Free Pandas Projects]({DATAWARS_PROJECTS}) - DataWars curated",
            f"[Pandas Skill Track]({DATAWARS_PANDAS}) - Interactive practice",
            "[101 Pandas Exercises](https://www.machinelearningplus.com/python/101-pandas-exercises-python/) - Comprehensive",
            "[Kaggle Pandas Course](https://www.kaggle.com/learn/pandas) - Interactive learning"
        ],
        "interactive": [
            f"[DataWars Platform]({DATAWARS_BASE}) - 1000+ projects",
            "[Google Colab](https://colab.research.google.com) - Practice environment",
            "[DataCamp Pandas](https://www.datacamp.com/courses/pandas-foundations) - Structured course"
        ]
    },

    "visualization": {
        "articles": [
            "[Matplotlib Tutorials](https://matplotlib.org/stable/tutorials/index.html) - Official docs",
            "[Seaborn Tutorial](https://seaborn.pydata.org/tutorial.html) - Statistical visualization",
            "[Plotly Python](https://plotly.com/python/) - Interactive plots"
        ],
        "videos": [
            "[Matplotlib Tutorial](https://www.youtube.com/watch?v=UO98lJQ3QGI) - Complete guide",
            "[Seaborn Tutorial](https://www.youtube.com/watch?v=6GUZXDef2U0) - Data visualization"
        ],
        "practice": [
            "[Matplotlib Gallery](https://matplotlib.org/stable/gallery/index.html) - Example plots",
            "[Seaborn Examples](https://seaborn.pydata.org/examples/index.html) - Visual gallery",
            f"[DataWars Visualization]({DATAWARS_BASE}) - Practice projects"
        ],
        "interactive": [
            "[Google Colab](https://colab.research.google.com) - Plot in browser",
            "[Plotly Chart Studio](https://chart-studio.plotly.com/) - Interactive charts"
        ]
    },

    "machine_learning": {
        "articles": [
            "[scikit-learn Documentation](https://scikit-learn.org/stable/user_guide.html) - Complete guide",
            "[Machine Learning Mastery](https://machinelearningmastery.com/start-here/) - Tutorials",
            "[Google ML Crash Course](https://developers.google.com/machine-learning/crash-course) - Free course"
        ],
        "videos": [
            "[StatQuest Machine Learning](https://www.youtube.com/c/joshstarmer) - Concepts explained",
            "[Andrew Ng ML Course](https://www.coursera.org/learn/machine-learning) - Foundational"
        ],
        "practice": [
            "[Kaggle Competitions](https://www.kaggle.com/competitions) - Real datasets",
            "[UCI ML Repository](https://archive.ics.uci.edu/ml/index.php) - Practice datasets",
            f"[DataWars ML Projects]({DATAWARS_BASE}) - Hands-on practice",
            "[HackerRank ML](https://www.hackerrank.com/domains/ai) - Challenges"
        ],
        "interactive": [
            "[Kaggle Learn](https://www.kaggle.com/learn) - Interactive ML courses",
            "[Google Colab](https://colab.research.google.com) - Free GPU",
            "[DataCamp ML Courses](https://www.datacamp.com/courses/machine-learning) - Structured learning"
        ]
    },

    # Phase 2: Deep Learning (Days 16-30)
    "pytorch": {
        "articles": [
            f"[PyTorch Tutorials]({PYTORCH_TUTORIALS}) - Official documentation",
            f"[PyTorch Basics]({PYTORCH_BASICS}) - Getting started guide",
            f"[Learn PyTorch]({LEARN_PYTORCH}) - Complete course"
        ],
        "videos": [
            f"[PyTorch 60 Minute Blitz]({PYTORCH_60MIN}) - Quick start",
            "[PyTorch for Deep Learning](https://www.youtube.com/watch?v=c36lUUr864M) - FreeCodeCamp",
            "[Zero to Mastery PyTorch](https://www.youtube.com/watch?v=Z_ikDlimN6A) - Full course"
        ],
        "practice": [
            "[PyTorch Examples](https://github.com/pytorch/examples) - Official examples",
            "[PyTorch Tutorials GitHub](https://github.com/pytorch/tutorials) - Code samples",
            "[Kaggle PyTorch](https://www.kaggle.com/learn/intro-to-deep-learning) - Interactive"
        ],
        "interactive": [
            "[Google Colab](https://colab.research.google.com) - Free GPU for PyTorch",
            "[Kaggle Notebooks](https://www.kaggle.com/code) - GPU notebooks",
            f"[DataCamp PyTorch](https://www.datacamp.com/courses/deep-learning-in-python) - Interactive"
        ]
    },

    # Phase 3: Computer Vision (Days 31-45)
    "computer_vision": {
        "articles": [
            "[YOLO Object Detection](https://www.datacamp.com/blog/yolo-object-detection-explained) - Complete guide",
            "[Roboflow YOLO Tutorial](https://blog.roboflow.com/yolo-object-detection/) - Practical implementation",
            "[Computer Vision Guide](https://www.viam.com/post/computer-vision-object-detection-guide) - 2025 expert guide"
        ],
        "videos": [
            "[YOLO Object Detection](https://www.youtube.com/watch?v=ag3DLKsl2vk) - Implementation tutorial",
            "[Computer Vision Course](https://www.youtube.com/watch?v=01sAkU_NvOY) - Stanford CS231n"
        ],
        "practice": [
            "[Roboflow Universe](https://universe.roboflow.com/) - CV datasets",
            "[Papers With Code CV](https://paperswithcode.com/area/computer-vision) - SOTA models",
            "[Kaggle CV Competitions](https://www.kaggle.com/competitions?search=computer+vision) - Practice"
        ],
        "interactive": [
            "[Google Colab](https://colab.research.google.com) - GPU for CV",
            "[Roboflow](https://roboflow.com/) - Annotation & training",
            "[Gradio](https://gradio.app/) - Demo interfaces"
        ]
    },

    # Phase 4: NLP (Days 46-60)
    "nlp_transformers": {
        "articles": [
            f"[Hugging Face Transformers]({HF_TRANSFORMERS}) - Official documentation",
            f"[Fine-tuning Guide]({HF_TRAINING}) - Training models",
            "[BERT Explained](https://www.kdnuggets.com/how-to-fine-tune-bert-sentiment-analysis-hugging-face-transformers) - KDnuggets tutorial"
        ],
        "videos": [
            "[Transformers Explained](https://www.youtube.com/watch?v=TQQlZhbC5ps) - Attention mechanism",
            "[Hugging Face Course](https://www.youtube.com/watch?v=00GKzGyWFEs) - Complete tutorial"
        ],
        "practice": [
            "[Hugging Face Models](https://huggingface.co/models) - Pre-trained models",
            "[NLP Datasets](https://huggingface.co/datasets) - Practice data",
            "[Papers With Code NLP](https://paperswithcode.com/area/natural-language-processing) - SOTA"
        ],
        "interactive": [
            "[Hugging Face Spaces](https://huggingface.co/spaces) - Model demos",
            "[Google Colab](https://colab.research.google.com) - GPU for NLP",
            "[Gradio](https://gradio.app/) - Quick demos"
        ]
    },

    # Phase 5: LLMs & RAG (Days 61-75)
    "llm_rag": {
        "articles": [
            f"[LangChain RAG Tutorial]({LANGCHAIN_RAG}) - Official guide",
            "[RAG Complete Guide](https://www.singlestore.com/blog/a-guide-to-retrieval-augmented-generation-rag/) - SingleStore",
            "[Master RAG with LangChain](https://blog.futuresmart.ai/master-rag-with-langchain-a-practical-guide) - Step-by-step"
        ],
        "videos": [
            "[LangChain Tutorial](https://www.youtube.com/watch?v=nAmC7SoVLd8) - Complete guide",
            "[RAG Explained](https://www.youtube.com/watch?v=T-D1OfcDW1M) - Sam Witteveen"
        ],
        "practice": [
            "[LangChain Examples](https://github.com/langchain-ai/langchain/tree/master/cookbook) - Code samples",
            "[RAG Projects](https://github.com/topics/retrieval-augmented-generation) - GitHub",
            "[Pinecone Examples](https://docs.pinecone.io/examples) - Vector DB"
        ],
        "interactive": [
            "[LangChain Hub](https://smith.langchain.com/hub) - Prompt templates",
            "[OpenAI Playground](https://platform.openai.com/playground) - Test prompts",
            "[Google Colab](https://colab.research.google.com) - RAG development"
        ]
    },

    # Phase 6: MLOps (Days 76-85)
    "mlops": {
        "articles": [
            f"[MLflow Documentation]({MLFLOW_DOCS}) - Official guide",
            "[MLOps for Beginners](https://towardsdatascience.com/machine-learning-operations-mlops-for-beginners-a5686bfe02b2/) - Complete guide",
            f"[FastAPI ML Tutorial]({FASTAPI_ML}) - PyCharm blog",
            "[Docker MLOps Workflow](https://www.runpod.io/articles/guides/mlops-workflow-docker-ai-deployment) - RunPod"
        ],
        "videos": [
            "[MLOps Course](https://www.youtube.com/watch?v=NgWujOrCZFo) - FreeCodeCamp",
            "[MLflow Tutorial](https://www.youtube.com/watch?v=859OxXrt_TI) - Complete guide"
        ],
        "practice": [
            "[7 MLOps Projects](https://www.kdnuggets.com/7-mlops-projects-beginners) - KDnuggets",
            "[MLOps GitHub](https://github.com/topics/mlops) - Project examples",
            "[DVC Tutorials](https://dvc.org/doc/start) - Data versioning"
        ],
        "interactive": [
            "[MLflow Tracking](https://mlflow.org/docs/latest/quickstart.html) - Hands-on",
            "[Docker Playground](https://labs.play-with-docker.com/) - Practice Docker",
            "[Google Cloud MLOps](https://cloud.google.com/architecture/mlops-continuous-delivery-and-automation-pipelines-in-machine-learning) - Cloud platform"
        ]
    },

    # Phase 7: Advanced (Days 86-100)
    "advanced_ai": {
        "articles": [
            "[Stable Diffusion Guide](https://stability.ai/stable-diffusion) - Official docs",
            "[Reinforcement Learning](https://spinningup.openai.com/en/latest/) - OpenAI guide",
            "[Multi-Modal AI](https://huggingface.co/blog/vision_language_pretraining) - Hugging Face"
        ],
        "videos": [
            "[Stable Diffusion Tutorial](https://www.youtube.com/watch?v=1CIpzeNxIhU) - Complete guide",
            "[RL Course](https://www.youtube.com/watch?v=2pWv7GOvuf0) - David Silver"
        ],
        "practice": [
            "[Stable Diffusion Examples](https://github.com/CompVis/stable-diffusion) - GitHub",
            "[OpenAI Gym](https://gym.openai.com/) - RL environments",
            "[Hugging Face Diffusers](https://huggingface.co/docs/diffusers/index) - Image generation"
        ],
        "interactive": [
            "[Google Colab](https://colab.research.google.com) - GPU for generation",
            "[Replicate](https://replicate.com/) - Run models",
            "[Gradio](https://gradio.app/) - Create demos"
        ]
    }
}

# Map day numbers to resource categories
DAY_TO_CATEGORY = {
    # Days 1-2: NumPy
    1: "numpy", 2: "numpy",
    # Days 3-4: Pandas
    3: "pandas", 4: "pandas",
    # Days 5-6: Visualization
    5: "visualization", 6: "visualization",
    # Days 7-15: Classical ML
    **{i: "machine_learning" for i in range(7, 16)},
    # Days 16-30: Deep Learning/PyTorch
    **{i: "pytorch" for i in range(16, 31)},
    # Days 31-45: Computer Vision
    **{i: "computer_vision" for i in range(31, 46)},
    # Days 46-60: NLP/Transformers
    **{i: "nlp_transformers" for i in range(46, 61)},
    # Days 61-75: LLMs & RAG
    **{i: "llm_rag" for i in range(61, 76)},
    # Days 76-85: MLOps
    **{i: "mlops" for i in range(76, 86)},
    # Days 86-100: Advanced AI
    **{i: "advanced_ai" for i in range(86, 101)}
}

def get_resources_for_day(day_num):
    """Get topic-specific resources for a given day"""
    category = DAY_TO_CATEGORY.get(day_num, "machine_learning")
    return TOPIC_RESOURCES.get(category, TOPIC_RESOURCES["machine_learning"])
