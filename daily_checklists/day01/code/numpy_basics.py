"""
Day 1: NumPy Basics - Example Code
This script demonstrates fundamental NumPy operations for AI/ML

Author: 100 Days of AI Engineer
Date: Day 01
"""

import numpy as np


def array_creation_examples():
    """Demonstrates various ways to create NumPy arrays"""
    print("=" * 50)
    print("1. ARRAY CREATION")
    print("=" * 50)

    # Create arrays from lists
    arr_1d = np.array([1, 2, 3, 4, 5])
    print(f"1D Array: {arr_1d}")

    arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
    print(f"2D Array:\n{arr_2d}")

    # Create arrays with built-in functions
    zeros = np.zeros((3, 3))
    print(f"\nZeros Array:\n{zeros}")

    ones = np.ones((2, 4))
    print(f"\nOnes Array:\n{ones}")

    range_arr = np.arange(0, 10, 2)
    print(f"\nRange Array: {range_arr}")

    linspace_arr = np.linspace(0, 1, 5)
    print(f"Linspace Array: {linspace_arr}")

    # Random arrays (important for ML)
    random_arr = np.random.rand(3, 3)
    print(f"\nRandom Array:\n{random_arr}")
    print()


def array_operations():
    """Demonstrates basic array operations"""
    print("=" * 50)
    print("2. ARRAY OPERATIONS")
    print("=" * 50)

    a = np.array([1, 2, 3, 4])
    b = np.array([5, 6, 7, 8])

    print(f"Array a: {a}")
    print(f"Array b: {b}")

    # Arithmetic operations
    print(f"\nAddition (a + b): {a + b}")
    print(f"Subtraction (a - b): {a - b}")
    print(f"Multiplication (a * b): {a * b}")
    print(f"Division (a / b): {a / b}")

    # Element-wise operations
    print(f"\nSquare (a ** 2): {a ** 2}")
    print(f"Square root: {np.sqrt(a)}")

    # Aggregation functions
    print(f"\nSum: {np.sum(a)}")
    print(f"Mean: {np.mean(a)}")
    print(f"Max: {np.max(a)}")
    print(f"Min: {np.min(a)}")
    print(f"Std Dev: {np.std(a)}")
    print()


def indexing_and_slicing():
    """Demonstrates array indexing and slicing"""
    print("=" * 50)
    print("3. INDEXING & SLICING")
    print("=" * 50)

    arr = np.array([[1, 2, 3, 4],
                    [5, 6, 7, 8],
                    [9, 10, 11, 12]])

    print(f"Original Array:\n{arr}")

    # Indexing
    print(f"\nElement at [0, 0]: {arr[0, 0]}")
    print(f"Element at [1, 2]: {arr[1, 2]}")

    # Slicing
    print(f"\nFirst row: {arr[0, :]}")
    print(f"Second column: {arr[:, 1]}")
    print(f"First 2 rows, first 3 cols:\n{arr[:2, :3]}")

    # Boolean indexing (crucial for ML)
    mask = arr > 5
    print(f"\nBoolean mask (arr > 5):\n{mask}")
    print(f"Elements greater than 5: {arr[mask]}")
    print()


def array_reshaping():
    """Demonstrates array reshaping operations"""
    print("=" * 50)
    print("4. ARRAY RESHAPING")
    print("=" * 50)

    arr = np.arange(12)
    print(f"Original Array: {arr}")
    print(f"Shape: {arr.shape}")

    # Reshape to 2D
    reshaped = arr.reshape(3, 4)
    print(f"\nReshaped to (3, 4):\n{reshaped}")

    # Reshape to 3D
    reshaped_3d = arr.reshape(2, 2, 3)
    print(f"\nReshaped to (2, 2, 3):\n{reshaped_3d}")

    # Transpose
    transposed = reshaped.T
    print(f"\nTransposed:\n{transposed}")

    # Flatten
    flattened = reshaped.flatten()
    print(f"\nFlattened: {flattened}")
    print()


def matrix_operations():
    """Demonstrates matrix operations (important for ML)"""
    print("=" * 50)
    print("5. MATRIX OPERATIONS")
    print("=" * 50)

    A = np.array([[1, 2], [3, 4]])
    B = np.array([[5, 6], [7, 8]])

    print(f"Matrix A:\n{A}")
    print(f"\nMatrix B:\n{B}")

    # Matrix multiplication (dot product)
    mat_mul = np.dot(A, B)
    print(f"\nMatrix Multiplication (A @ B):\n{mat_mul}")

    # Element-wise multiplication
    elem_mul = A * B
    print(f"\nElement-wise Multiplication:\n{elem_mul}")

    # Matrix determinant
    det = np.linalg.det(A)
    print(f"\nDeterminant of A: {det}")

    # Matrix inverse
    inv = np.linalg.inv(A)
    print(f"\nInverse of A:\n{inv}")

    # Eigenvalues and eigenvectors
    eigenvalues, eigenvectors = np.linalg.eig(A)
    print(f"\nEigenvalues: {eigenvalues}")
    print(f"Eigenvectors:\n{eigenvectors}")
    print()


def ml_relevant_operations():
    """Demonstrates operations commonly used in ML"""
    print("=" * 50)
    print("6. ML-RELEVANT OPERATIONS")
    print("=" * 50)

    # Simulating a dataset (features)
    np.random.seed(42)
    data = np.random.randn(5, 3)  # 5 samples, 3 features

    print(f"Sample Dataset (5 samples, 3 features):\n{data}")

    # Normalization (zero mean, unit variance)
    mean = np.mean(data, axis=0)
    std = np.std(data, axis=0)
    normalized = (data - mean) / std

    print(f"\nMean per feature: {mean}")
    print(f"Std per feature: {std}")
    print(f"\nNormalized Data:\n{normalized}")

    # Min-Max scaling
    min_val = np.min(data, axis=0)
    max_val = np.max(data, axis=0)
    scaled = (data - min_val) / (max_val - min_val)

    print(f"\nMin-Max Scaled Data:\n{scaled}")

    # Computing distances (Euclidean)
    point1 = data[0]
    point2 = data[1]
    distance = np.linalg.norm(point1 - point2)
    print(f"\nEuclidean distance between sample 0 and 1: {distance:.4f}")

    # Broadcasting example
    weights = np.array([0.5, 0.3, 0.2])
    weighted_data = data * weights
    print(f"\nWeighted Data (broadcasting):\n{weighted_data}")
    print()


def main():
    """Main function to run all examples"""
    print("\n" + "=" * 50)
    print("DAY 1: NumPy Basics for AI Engineering")
    print("=" * 50 + "\n")

    array_creation_examples()
    array_operations()
    indexing_and_slicing()
    array_reshaping()
    matrix_operations()
    ml_relevant_operations()

    print("=" * 50)
    print("Day 1 Complete! You've learned NumPy basics.")
    print("Next: Practice these operations and explore more!")
    print("=" * 50 + "\n")


if __name__ == "__main__":
    main()
