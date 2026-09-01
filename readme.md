<div align="center">

  <h1>📈 ft_linear_regression</h1>
  <p><strong>A implementation of univariate linear regression with gradient descent from scratch.</strong></p>

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

  <!-- Header Visual GIF -->
  <img src="https://miro.medium.com/1*OG1d4edy5BFYeQ0yHjBOJA.gif" alt="Gradient Descent Convergence GIF" width="650"/>

</div>

<hr />

## 📋 Table of Contents
- [About The Project](#-about-the-project)
- [How It Works](#-how-it-works)
  - [1. Hypothesis Function](#1-hypothesis-function)
  - [2. Feature Normalization](#2-feature-normalization)
  - [3. Gradient Descent Optimization](#3-gradient-descent-optimization)
- [Project Architecture](#-project-architecture)
- [Getting Started](#-getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#-usage)
  - [1. Train the Model](#1-train-the-model)
  - [2. Predict Car Price](#2-predict-car-price)
  - [3. Plot & Evaluate](#3-plot--evaluate)
- [Visualizations](#-visualizations)

---

## 💡 About The Project

**`ft_linear_regression`** is a machine learning project designed to predict car prices based on mileage. The goal is to build a complete **univariate linear regression model trained via gradient descent** entirely from scratch in Python—without relying on external ML frameworks like `scikit-learn` or `TensorFlow`.

### Key Features
* ⚙️ **From-Scratch Gradient Descent**: Custom batch gradient descent optimization loop.
* 📏 **Feature Scaling**: Min-Max feature normalization to guarantee gradient stability and quick convergence.
* 💾 **State Persistence**: Serializes trained parameters ($\theta_0$ and $\theta_1$) into a JSON configuration for instant prediction retrieval.
* 📊 **Data Visualization**: Real-time plots tracking cost reduction and displaying the linear fit over raw data points.

---

## 🧮 How It Works

### 1. Hypothesis Function
The model estimates the car price ($\hat{y}$) given a input mileage ($x$) using a simple linear equation:

$$\hat{y} = f(x) = \theta_0 + (\theta_1 \cdot x)$$

* **$\theta_0$ (bias)**: Y-intercept representing base price value.
* **$\theta_1$ (weight)**: Rate of price decrease relative to mileage increase.

---

### 2. Feature Normalization
To prevent vanishing or exploding gradients due to high mileage values, features are scaled to the range $[0, 1]$ before training:

$$x_{\text{scaled}} = \frac{x - x_{\text{min}}}{x_{\text{max}} - x_{\text{min}}}$$

---

### 3. Gradient Descent Optimization
Parameters $\theta_0$ and $\theta_1$ are updated iteratively over batch epochs to minimize the **Mean Squared Error (MSE)** cost function:

$$\theta_0 := \theta_0 - \alpha \cdot \frac{1}{m} \sum_{i=1}^{m} \left( f(x^{(i)}) - y^{(i)} \right)$$

$$\theta_1 := \theta_1 - \alpha \cdot \frac{1}{m} \sum_{i=1}^{m} \left( f(x^{(i)}) - y^{(i)} \right) \cdot x_{\text{scaled}}^{(i)}$$

> **Where:**
> * $\alpha$ = Learning rate
> * $m$ = Number of dataset examples

---

## 📂 Project Architecture

```txt
.
├── data.csv            # Dataset containing Mileage (km) and Price
├── train.py            # Gradient descent model trainer
├── predict.py          # Interactive car price estimator
├── visualize.py        # Matplotlib plotting utility
├── theta.json          # Persistent file storing trained parameters
└── README.md           # Documentation
