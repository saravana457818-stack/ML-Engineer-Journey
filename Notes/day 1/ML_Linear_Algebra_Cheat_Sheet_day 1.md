# Machine Learning Linear Algebra Cheat Sheet

## Scalar (0D)
- Single number
- Examples: learning rate, loss, accuracy, bias

```python
learning_rate = 0.001
loss = 0.24
```

## Vector (1D)
- Ordered list of numbers
- Represents one data sample or model weights

```python
student = [18, 92, 8]
weights = [0.6, 1.2, -0.5]
```

## Matrix (2D)
- Rows and columns
- Represents an entire dataset or grayscale image

```python
X = [
    [18,92],
    [20,85],
    [19,88]
]
```

## Tensor (3D+)
- Collection of matrices
- Used for RGB images, videos, and deep learning

## ML Example

Input Matrix:
```text
X = [
 [2,80,6],
 [5,92,7],
 [8,95,8]
]
```

Target Vector:
```text
y = [60,88,98]
```

Weight Vector:
```text
w = [5.2,0.3,2.1]
```

Bias:
```text
b = 4
```

Prediction:
```text
Prediction = Xw + b
```

## Common Operations

| Operation | Purpose |
|---|---|
| Addition | Combine values |
| Subtraction | Compute error |
| Matrix × Vector | Make predictions |
| Dot Product | Weighted sum |
| Transpose | Swap rows/columns |
| Inverse | Solve linear systems |
| Mean | Normalize |
| Sum | Compute loss |

## Algorithms

| Algorithm | Uses |
|---|---|
| Linear Regression | Matrix × Vector |
| Logistic Regression | Matrix × Vector |
| Decision Trees | Matrix |
| Random Forest | Matrix |
| KNN | Vectors |
| SVM | Vectors |
| Neural Networks | Matrices & Tensors |
| CNN | Tensors |
| Transformers | Tensors |

## Key Formula

- y = wx + b
- y = Xw + b
- Loss = Actual − Prediction
- w = w − α × gradient

## Remember

- Scalar = One number
- Vector = One sample
- Matrix = Whole dataset
- Tensor = Multiple matrices
