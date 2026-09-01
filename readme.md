<div align="center">

  <!-- Header Banner / Title -->
  <h1>📈 ft_linear_regression</h1>
  <p><strong>An implementation of univariate linear regression with gradient descent from scratch.</strong></p>

  <!-- Badges -->
  <p>
    <a href="https://github.com/RadiantVixen/ft_linear_regression/stargazers">
      <img src="https://img.shields.io/github/stars/RadiantVixen/ft_linear_regression?style=for-the-badge&color=ff69b4" alt="Stars" />
    </a>
    <a href="https://github.com/RadiantVixen/ft_linear_regression/network/members">
      <img src="https://img.shields.io/github/forks/RadiantVixen/ft_linear_regression?style=for-the-badge&color=1e90ff" alt="Forks" />
    </a>
    <a href="https://github.com/RadiantVixen/ft_linear_regression/issues">
      <img src="https://img.shields.io/github/issues/RadiantVixen/ft_linear_regression?style=for-the-badge&color=brightgreen" alt="Issues" />
    </a>
    <a href="https://github.com/RadiantVixen/ft_linear_regression/blob/main/LICENSE">
      <img src="https://img.shields.io/github/license/RadiantVixen/ft_linear_regression?style=for-the-badge&color=orange" alt="License" />
    </a>
  </p>

  <!-- Animated Preview / Header Visual -->
  <img src="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExOHp1eXU1ZnRrbTRjc2RmcGhyandhdXQzOWlyN2pxa3ZsdTZwMGx1eCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/L1R1tvI9svkIWwpVYr/giphy.gif" alt="Training Visual Demo" width="650"/>

</div>

<hr />

## 📋 Table of Contents
- [About The Project](#-about-the-project)
- [How It Works](#-how-it-works)
  - [Hypothesis Function](#1-hypothesis-function)
  - [Feature Feature Scaling (Normalization)](#2-feature-scaling-normalization)
  - [Gradient Descent Updates](#3-gradient-descent-updates)
- [Project Architecture](#-project-architecture)
- [Getting Started](#-getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation & Setup](#installation--setup)
- [Usage](#-usage)
  - [1. Train the Model](#1-train-the-model)
  - [2. Predict Mileage / Price](#2-predict-mileage--price)
  - [3. (Bonus) Precision Evaluation & Visualizer](#3-bonus-precision-evaluation--visualizer)
- [Visualizations](#-visualizations)

---

## 💡 About The Project

**ft_linear_regression** is an introductory Machine Learning project designed to predict car prices based on mileage. The core objective is to understand and implement **univariate linear regression with gradient descent** entirely from scratch—without relying on high-level machine learning libraries like `scikit-learn` for model fitting.

### Key Highlights
* ⚙️ **Custom Gradient Descent**: Optimized step-by-step optimization loop.
* 📏 **Feature Normalization**: Implemented **Min-Max Scaling** (or **Z-score Standardization**) to ensure smooth gradient descent convergence.
* 📊 **Data Visualization**: Real-time plots comparing original raw data points against the fitted linear hypothesis line.
* 🎯 **Precision Metrics**: Evaluated performance using Mean Squared Error ($MSE$) and the Coefficient of Determination ($R^2$).

---

## 🧮 How It Works

### 1. Hypothesis Function
The model predicts a car's price ($\hat{y}$) given its mileage ($x$) using a simple linear equation:

$$\hat{y} = f(x) = \theta_0 + (\theta_1 \cdot x)$$

* **$\theta_0$ (bias)**: Intercept on the Y-axis.
* **$\theta_1$ (weight)**: Slope indicating how price changes with mileage.

---

### 2. Feature Scaling (Normalization)
To prevent vanishing or exploding gradients due to differences in scale between mileage (e.g., $10,000 - 240,000$) and price, features are normalized prior to training:

$$x_{norm} = \frac{x - x_{min}}{x_{max} - x_{min}}$$

---

### 3. Gradient Descent Updates
The parameters $\theta_0$ and $\theta_1$ are iteratively updated to minimize the **Mean Squared Error (MSE)** loss function:

$$\theta_0 := \theta_0 - \alpha \cdot \frac{1}{m} \sum_{i=1}^{m} \left( f(x^{(i)}) - y^{(i)} \right)$$

$$\theta_1 := \theta_1 - \alpha \cdot \frac{1}{m} \sum_{i=1}^{m} \left( f(x^{(i)}) - y^{(i)} \right) \cdot x^{(i)}$$

> **Where:**
> * $\alpha$ = Learning rate
> * $m$ = Total number of dataset entries

---

## 📂 Project Architecture

```txt
.
├── data.csv            # Dataset (Mileage vs. Price)
├── train.py            # Gradient descent training algorithm
├── predict.py          # Interactive script to query predictions
├── visualize.py        # Matplotlib visualization script
├── theta.json          # Saved parameters (theta_0 and theta_1)
└── README.md           # Documentation
