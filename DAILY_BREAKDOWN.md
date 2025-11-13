# 📅 Detailed Daily Breakdown

This document provides granular, day-by-day tasks for the 100-day journey.

---

## 🔥 Phase 1: Foundations & Classical ML (Days 1-15)

### Day 1: NumPy Basics & Array Operations

**Learning Objectives:**
- Understand NumPy arrays vs Python lists
- Master array creation and manipulation
- Learn vectorization for performance

**Tasks:**
1. Install environment and setup Jupyter
2. NumPy array creation (zeros, ones, arange, linspace)
3. Array indexing, slicing, and reshaping
4. Broadcasting rules
5. Mathematical operations

**Code Challenge:**
```python
# Implement these without loops:
# 1. Normalize a 2D array (mean=0, std=1)
# 2. Calculate pairwise distances between points
# 3. Implement moving average
```

**Resources:**
- NumPy documentation: https://numpy.org/doc/
- Real Python NumPy tutorial
- 100 NumPy exercises (GitHub)

**Time Allocation:**
- Learning: 2 hours
- Coding: 1.5 hours
- Challenge: 30 minutes

---

### Day 2: Advanced NumPy & Linear Algebra

**Learning Objectives:**
- Matrix operations for ML
- Random sampling
- Performance optimization

**Tasks:**
1. Matrix multiplication, transpose, inverse
2. Eigenvalues and eigenvectors
3. Random number generation and seeding
4. np.einsum for complex operations
5. Memory management and views vs copies

**Mini Project: Image Filters**
Build basic image filters using NumPy:
- Grayscale conversion
- Blur filter
- Edge detection (Sobel)
- Brightness/contrast adjustment

**Code Template:**
```python
import numpy as np
from PIL import Image

def apply_blur(image, kernel_size=5):
    # Your implementation
    pass

def edge_detection(image):
    # Implement Sobel filter
    pass
```

**Deliverable:** Jupyter notebook with filter implementations + example images

---

### Day 3: Pandas Fundamentals

**Learning Objectives:**
- DataFrames and Series
- Data loading from multiple formats
- Basic data exploration

**Tasks:**
1. Read CSV, Excel, JSON files
2. DataFrame creation and manipulation
3. Indexing: loc, iloc, boolean indexing
4. Basic statistics: describe(), info()
5. Sorting and filtering

**Dataset:** Download Titanic dataset from Kaggle

**Exercises:**
```python
# 1. Load Titanic dataset
# 2. Find survival rate by class and gender
# 3. Identify missing values
# 4. Calculate average age by passenger class
# 5. Filter passengers by criteria
```

**Resources:**
- Pandas documentation
- Kaggle Pandas course
- "Python for Data Analysis" by Wes McKinney

---

### Day 4: Advanced Pandas & Data Cleaning

**Learning Objectives:**
- Handle missing data
- Data transformation and aggregation
- Merging and joining datasets

**Tasks:**
1. Missing value strategies (fillna, dropna, interpolate)
2. GroupBy operations
3. Pivot tables and cross-tabulations
4. Merging, joining, concatenating DataFrames
5. Apply and map functions

**Mini Project: COVID-19 Data Analysis**
Analyze COVID-19 dataset:
- Load time-series data
- Clean and handle missing values
- Calculate growth rates
- Group by country/region
- Create summary statistics

**Dataset:** Johns Hopkins COVID-19 dataset or Our World in Data

**Deliverable:** Analysis notebook with insights

---

### Day 5: Data Visualization - Matplotlib & Seaborn

**Learning Objectives:**
- Create effective visualizations
- Understand plot types and when to use them
- Customize plots for presentation

**Tasks:**
1. Matplotlib basics: line, scatter, bar, histogram
2. Subplots and figure customization
3. Seaborn statistical plots
4. Distribution plots (distplot, violinplot, boxplot)
5. Correlation heatmaps

**Exercises:**
```python
# Using Titanic dataset:
# 1. Age distribution histogram
# 2. Survival rate by class (bar chart)
# 3. Correlation heatmap
# 4. Pairplot for numerical features
# 5. Create a dashboard with 4 subplots
```

**Resources:**
- Matplotlib gallery
- Seaborn tutorial
- "Storytelling with Data" principles

---

### Day 6: Interactive Visualizations & EDA

**Learning Objectives:**
- Create interactive plots
- Perform comprehensive EDA
- Generate insights from data

**Tasks:**
1. Plotly for interactive visualizations
2. 3D plots and animations
3. Dashboard creation with Plotly Dash basics
4. Complete EDA workflow

**Mini Project: Titanic EDA Dashboard**
Create comprehensive exploratory analysis:
- Data overview and statistics
- Missing value analysis
- Univariate analysis (distributions)
- Bivariate analysis (relationships)
- Multivariate analysis
- Interactive visualizations

**Deliverable:** HTML dashboard or Jupyter notebook with rich visualizations

---

### Day 7: Mathematics for Machine Learning

**Learning Objectives:**
- Linear algebra for ML
- Calculus fundamentals
- Probability and statistics

**Topics:**
1. **Linear Algebra:**
   - Vectors and vector spaces
   - Matrix operations
   - Eigenvalues/eigenvectors intuition
   - PCA mathematical foundation

2. **Calculus:**
   - Derivatives and partial derivatives
   - Gradient intuition
   - Chain rule

3. **Probability & Statistics:**
   - Distributions (Normal, Bernoulli, Binomial)
   - Expected value, variance
   - Bayes theorem
   - Maximum Likelihood Estimation (MLE)

**Implementation:**
```python
# Implement from scratch:
# 1. Gradient descent for simple function
# 2. Calculate covariance matrix
# 3. Apply Bayes theorem to a problem
```

**Resources:**
- 3Blue1Brown: Linear Algebra & Calculus series
- Khan Academy
- "Mathematics for Machine Learning" book

---

### Day 8: Linear Regression - Theory

**Learning Objectives:**
- Understand regression fundamentals
- Implement from scratch
- Learn cost functions and optimization

**Topics:**
1. Problem formulation
2. Cost function (MSE)
3. Normal equation
4. Gradient descent for linear regression
5. Assumptions of linear regression

**Implementation:**
```python
class LinearRegression:
    def __init__(self, learning_rate=0.01, iterations=1000):
        self.lr = learning_rate
        self.iterations = iterations
        self.weights = None
        self.bias = None

    def fit(self, X, y):
        # Implement gradient descent
        pass

    def predict(self, X):
        # Implement prediction
        pass
```

**Exercise:**
- Implement linear regression from scratch
- Test on simple 1D dataset
- Visualize cost function convergence

---

### Day 9: Linear Regression - Practice & Regularization

**Learning Objectives:**
- Multiple linear regression
- Regularization techniques
- Model evaluation

**Topics:**
1. Multiple features
2. Feature scaling importance
3. Ridge (L2) regularization
4. Lasso (L1) regularization
5. Elastic Net
6. Evaluation metrics (MSE, RMSE, MAE, R²)

**Mini Project: House Price Prediction**
Dataset: California Housing or Kaggle House Prices

Tasks:
- Load and explore data
- Handle missing values
- Feature engineering (create new features)
- Scale features
- Train linear regression (from scratch + sklearn)
- Compare Ridge, Lasso, and Elastic Net
- Evaluate and visualize results

**Deliverable:** Jupyter notebook with complete analysis

---

### Day 10: Classification - Logistic Regression

**Learning Objectives:**
- Binary and multi-class classification
- Logistic function and decision boundaries
- Implementation from scratch

**Topics:**
1. Sigmoid function
2. Binary cross-entropy loss
3. Gradient descent for logistic regression
4. Decision boundary
5. Multi-class: One-vs-Rest, Softmax

**Implementation:**
```python
class LogisticRegression:
    def __init__(self, learning_rate=0.01, iterations=1000):
        pass

    def sigmoid(self, z):
        return 1 / (1 + np.exp(-z))

    def fit(self, X, y):
        # Implement gradient descent
        pass

    def predict_proba(self, X):
        pass

    def predict(self, X, threshold=0.5):
        pass
```

**Exercise:**
- Implement on iris dataset (binary: setosa vs others)
- Visualize decision boundary
- Test different thresholds

---

### Day 11: Tree-Based Models

**Learning Objectives:**
- Decision trees
- Ensemble methods
- Random Forests

**Topics:**
1. Decision tree algorithm (ID3, CART)
2. Information gain, Gini impurity
3. Overfitting in trees
4. Random Forest ensemble
5. Feature importance

**Tasks:**
- Implement simple decision tree (or use sklearn)
- Visualize decision tree
- Train Random Forest
- Compare single tree vs forest
- Analyze feature importances

**Mini Project: Spam Email Classifier**
Dataset: SMS Spam Collection

Steps:
1. Text preprocessing (TF-IDF)
2. Train Logistic Regression, Decision Tree, Random Forest
3. Compare performance
4. Analyze important features (words)

**Deliverable:** Classifier with >95% accuracy

---

### Day 12: Unsupervised Learning - Clustering

**Learning Objectives:**
- K-Means algorithm
- Hierarchical clustering
- Cluster evaluation

**Topics:**
1. K-Means algorithm and implementation
2. Elbow method for K selection
3. Silhouette score
4. Hierarchical clustering (agglomerative)
5. Dendrograms
6. DBSCAN for density-based clustering

**Implementation:**
```python
class KMeans:
    def __init__(self, k=3, max_iters=100):
        self.k = k
        self.max_iters = max_iters

    def fit(self, X):
        # Initialize centroids
        # Iterate: assign clusters, update centroids
        pass

    def predict(self, X):
        pass
```

**Exercise:**
- Implement K-Means from scratch
- Apply to customer segmentation dataset
- Visualize clusters
- Compare with sklearn implementation

---

### Day 13: Dimensionality Reduction - PCA

**Learning Objectives:**
- Principal Component Analysis
- Feature extraction vs selection
- Visualization of high-dimensional data

**Topics:**
1. Curse of dimensionality
2. PCA algorithm and intuition
3. Eigendecomposition
4. Explained variance
5. PCA for visualization

**Implementation:**
```python
class PCA:
    def __init__(self, n_components):
        self.n_components = n_components
        self.components = None
        self.mean = None

    def fit(self, X):
        # Center data
        # Compute covariance matrix
        # Get eigenvectors
        pass

    def transform(self, X):
        pass
```

**Mini Project: Customer Segmentation**
Dataset: Mall Customer Segmentation or Online Retail

Tasks:
1. Load and explore data
2. Apply PCA for dimensionality reduction
3. Use K-Means on reduced data
4. Visualize clusters in 2D/3D
5. Interpret customer segments

---

### Day 14: Model Evaluation & Cross-Validation

**Learning Objectives:**
- Proper model evaluation techniques
- Cross-validation strategies
- Handling imbalanced data

**Topics:**
1. Train-test split
2. K-fold cross-validation
3. Stratified K-fold
4. Metrics:
   - Classification: Accuracy, Precision, Recall, F1, ROC-AUC, Confusion Matrix
   - Regression: MSE, RMSE, MAE, R², MAPE
5. Handling imbalanced datasets:
   - SMOTE
   - Class weights
   - Undersampling/Oversampling

**Exercises:**
```python
# Implement:
# 1. K-fold CV from scratch
# 2. Calculate all classification metrics manually
# 3. Plot ROC curve and calculate AUC
# 4. Apply SMOTE to imbalanced dataset
```

**Resources:**
- Scikit-learn model evaluation guide
- "Imbalanced Learning" best practices

---

### Day 15: 🎯 PROJECT 1 - End-to-End ML Pipeline

**Project: Credit Card Fraud Detection**

**Objective:** Build a complete production-ready ML pipeline

**Requirements:**

1. **Data Collection & Exploration**
   - Load dataset (Kaggle Credit Card Fraud)
   - Comprehensive EDA
   - Identify patterns and anomalies

2. **Data Preprocessing**
   - Handle missing values
   - Feature scaling
   - Handle imbalanced data (SMOTE)

3. **Feature Engineering**
   - Create new features
   - Feature selection (correlation, importance)
   - Dimensionality reduction if needed

4. **Model Training**
   - Train multiple models:
     - Logistic Regression
     - Random Forest
     - XGBoost
   - Hyperparameter tuning (GridSearch/RandomSearch)

5. **Model Evaluation**
   - Cross-validation
   - Confusion matrix
   - ROC-AUC, Precision-Recall curves
   - Feature importance analysis

6. **Deployment Preparation**
   - Save model (pickle/joblib)
   - Create prediction function
   - Write documentation

**Deliverable:**
- Jupyter notebook with full pipeline
- Python script for model training
- Saved model file
- README with instructions

**Bonus:**
- Create simple Streamlit app for predictions
- Unit tests for pipeline components

---

## 🧠 Phase 2: Deep Learning Fundamentals (Days 16-30)

### Day 16: Neural Network Fundamentals

**Learning Objectives:**
- Understand perceptron
- Activation functions
- Network architecture basics

**Topics:**
1. Biological inspiration
2. Single perceptron
3. Activation functions:
   - Sigmoid
   - Tanh
   - ReLU and variants
4. Multi-layer perceptron (MLP)
5. Universal approximation theorem

**Implementation:**
```python
class Perceptron:
    def __init__(self, n_inputs):
        self.weights = np.random.randn(n_inputs)
        self.bias = 0

    def activation(self, x):
        return 1 if x >= 0 else 0

    def predict(self, inputs):
        total = np.dot(inputs, self.weights) + self.bias
        return self.activation(total)

    def train(self, X, y, epochs=100, lr=0.1):
        # Implement perceptron learning rule
        pass
```

**Exercises:**
- Implement AND, OR, XOR gates
- Understand XOR problem (linearly inseparable)
- Visualize decision boundaries

---

### Day 17: Forward Propagation & Loss Functions

**Learning Objectives:**
- Forward propagation algorithm
- Loss functions for different tasks
- Initialization strategies

**Topics:**
1. Forward pass mathematics
2. Loss functions:
   - Mean Squared Error (regression)
   - Binary Cross-Entropy (binary classification)
   - Categorical Cross-Entropy (multi-class)
3. Weight initialization (Xavier, He)

**Implementation:**
```python
class NeuralNetwork:
    def __init__(self, layer_sizes):
        self.layer_sizes = layer_sizes
        self.weights = []
        self.biases = []
        self._initialize_weights()

    def _initialize_weights(self):
        # Xavier/He initialization
        pass

    def relu(self, z):
        return np.maximum(0, z)

    def softmax(self, z):
        exp_z = np.exp(z - np.max(z, axis=1, keepdims=True))
        return exp_z / np.sum(exp_z, axis=1, keepdims=True)

    def forward(self, X):
        # Implement forward propagation
        pass
```

**Exercise:**
- Implement forward pass for 2-layer network
- Test with random weights on MNIST subset
- Understand output distributions

---

### Day 18: Backpropagation - Theory

**Learning Objectives:**
- Chain rule for derivatives
- Backpropagation algorithm
- Computational graphs

**Topics:**
1. Derivative chain rule
2. Backpropagation intuition
3. Computational graphs
4. Gradient flow

**Mathematics:**
```
For L = loss, y = output, z = weighted sum:
∂L/∂w = ∂L/∂y * ∂y/∂z * ∂z/∂w
```

**Tasks:**
1. Derive backprop equations manually for 2-layer network
2. Understand gradient computation
3. Draw computational graph

**Resources:**
- Andrej Karpathy: "Yes you should understand backprop"
- 3Blue1Brown: Neural Networks series
- Stanford CS231n notes

---

### Day 19: Backpropagation - Implementation

**Learning Objectives:**
- Implement backpropagation from scratch
- Train a neural network
- Understand gradient descent variants

**Implementation:**
```python
class NeuralNetwork:
    # ... (continued from Day 17)

    def backward(self, X, y):
        m = X.shape[0]

        # Output layer gradient
        dZ_output = self.cache['A_output'] - y
        dW_output = (1/m) * np.dot(self.cache['A_hidden'].T, dZ_output)
        db_output = (1/m) * np.sum(dZ_output, axis=0, keepdims=True)

        # Hidden layer gradient
        dA_hidden = np.dot(dZ_output, self.weights[-1].T)
        dZ_hidden = dA_hidden * self.relu_derivative(self.cache['Z_hidden'])
        dW_hidden = (1/m) * np.dot(X.T, dZ_hidden)
        db_hidden = (1/m) * np.sum(dZ_hidden, axis=0, keepdims=True)

        return {'dW_output': dW_output, 'db_output': db_output,
                'dW_hidden': dW_hidden, 'db_hidden': db_hidden}

    def update_weights(self, gradients, learning_rate):
        # Update weights using gradients
        pass

    def train(self, X, y, epochs, learning_rate):
        losses = []
        for epoch in range(epochs):
            # Forward pass
            output = self.forward(X)
            loss = self.compute_loss(output, y)
            losses.append(loss)

            # Backward pass
            gradients = self.backward(X, y)

            # Update weights
            self.update_weights(gradients, learning_rate)

            if epoch % 100 == 0:
                print(f'Epoch {epoch}, Loss: {loss}')

        return losses
```

**Exercise:**
- Complete neural network implementation
- Train on XOR problem
- Train on MNIST (small subset)
- Visualize training loss

**Deliverable:** Working neural network trained on MNIST (>90% accuracy)

---

### Day 20: Introduction to PyTorch

**Learning Objectives:**
- PyTorch basics
- Tensors and autograd
- Building models with nn.Module

**Topics:**
1. Tensors vs NumPy arrays
2. GPU acceleration (CUDA)
3. Autograd system
4. nn.Module and nn.Linear

**Code:**
```python
import torch
import torch.nn as nn
import torch.optim as optim

# Tensor basics
x = torch.tensor([1.0, 2.0, 3.0], requires_grad=True)
y = x ** 2
y.sum().backward()
print(x.grad)  # dy/dx

# Simple model
class SimpleNN(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super(SimpleNN, self).__init__()
        self.fc1 = nn.Linear(input_size, hidden_size)
        self.relu = nn.ReLU()
        self.fc2 = nn.Linear(hidden_size, output_size)

    def forward(self, x):
        x = self.fc1(x)
        x = self.relu(x)
        x = self.fc2(x)
        return x

# Training loop
model = SimpleNN(784, 128, 10)
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)

for epoch in range(epochs):
    # Forward pass
    outputs = model(inputs)
    loss = criterion(outputs, labels)

    # Backward pass
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()
```

**Exercise:**
- Reimplement Day 19 network in PyTorch
- Compare performance
- Experiment with different optimizers

---

### Day 21: MNIST Classification with PyTorch

**Learning Objectives:**
- Complete training pipeline in PyTorch
- DataLoaders and Datasets
- Model evaluation

**Tasks:**

1. **Data Loading:**
```python
from torchvision import datasets, transforms

transform = transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize((0.1307,), (0.3081,))
])

train_dataset = datasets.MNIST('./data', train=True, download=True, transform=transform)
train_loader = torch.utils.data.DataLoader(train_dataset, batch_size=64, shuffle=True)
```

2. **Model Training:**
```python
def train(model, device, train_loader, optimizer, epoch):
    model.train()
    for batch_idx, (data, target) in enumerate(train_loader):
        data, target = data.to(device), target.to(device)
        optimizer.zero_grad()
        output = model(data.view(data.shape[0], -1))
        loss = F.cross_entropy(output, target)
        loss.backward()
        optimizer.step()

        if batch_idx % 100 == 0:
            print(f'Epoch {epoch} [{batch_idx * len(data)}/{len(train_loader.dataset)}]'
                  f' Loss: {loss.item():.6f}')

def test(model, device, test_loader):
    model.eval()
    test_loss = 0
    correct = 0
    with torch.no_grad():
        for data, target in test_loader:
            data, target = data.to(device), target.to(device)
            output = model(data.view(data.shape[0], -1))
            test_loss += F.cross_entropy(output, target, reduction='sum').item()
            pred = output.argmax(dim=1, keepdims=True)
            correct += pred.eq(target.view_as(pred)).sum().item()

    accuracy = 100. * correct / len(test_loader.dataset)
    print(f'Test Accuracy: {accuracy:.2f}%')
```

**Mini Project:**
- Build MNIST classifier (>98% accuracy)
- Visualize predictions
- Analyze mistakes (confusion matrix)
- Save and load model

---

### Day 22: Regularization & Optimization

**Learning Objectives:**
- Prevent overfitting
- Advanced optimization techniques
- Hyperparameter tuning

**Topics:**

1. **Regularization:**
```python
# Dropout
class RegularizedNN(nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = nn.Linear(784, 256)
        self.dropout1 = nn.Dropout(0.3)
        self.bn1 = nn.BatchNorm1d(256)
        self.fc2 = nn.Linear(256, 128)
        self.dropout2 = nn.Dropout(0.2)
        self.fc3 = nn.Linear(128, 10)

    def forward(self, x):
        x = F.relu(self.bn1(self.fc1(x)))
        x = self.dropout1(x)
        x = F.relu(self.fc2(x))
        x = self.dropout2(x)
        x = self.fc3(x)
        return x

# L2 Regularization (weight decay)
optimizer = optim.Adam(model.parameters(), lr=0.001, weight_decay=1e-5)
```

2. **Learning Rate Scheduling:**
```python
scheduler = optim.lr_scheduler.StepLR(optimizer, step_size=5, gamma=0.5)
# Or
scheduler = optim.lr_scheduler.ReduceLROnPlateau(optimizer, mode='min', patience=3)
```

3. **Early Stopping:**
```python
class EarlyStopping:
    def __init__(self, patience=5, min_delta=0):
        self.patience = patience
        self.min_delta = min_delta
        self.counter = 0
        self.best_loss = None
        self.early_stop = False

    def __call__(self, val_loss):
        if self.best_loss is None:
            self.best_loss = val_loss
        elif val_loss > self.best_loss - self.min_delta:
            self.counter += 1
            if self.counter >= self.patience:
                self.early_stop = True
        else:
            self.best_loss = val_loss
            self.counter = 0
```

**Exercise:**
- Train model with and without regularization
- Compare overfitting
- Experiment with different dropouts, learning rates
- Implement early stopping

---

*Continue with Days 23-100 following the same detailed format...*

---

## 📝 Note

This is a comprehensive breakdown for the first 22 days. The remaining days (23-100) follow the same detailed structure with:
- Clear learning objectives
- Specific tasks and code implementations
- Mini projects and exercises
- Resources and deliverables

Each day builds progressively on previous knowledge, ensuring a solid foundation for becoming an AI Engineer.

**The complete day-by-day breakdown for all 100 days is available in the repository, organized by phases and weeks.**

