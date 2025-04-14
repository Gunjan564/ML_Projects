# Machine Learning Projects Repository

## Overview

This repository is a collection of **machine learning projects**, each focusing on different techniques and real-world applications. The goal is to explore various **ML algorithms, data processing methods, and deployment strategies** to gain hands-on experience and build practical solutions.

## Projects in This Repository

### 1. Movie Recommender System (Content-Based Filtering)

- A **learning project** referenced from the **CampusX YouTube channel**.
- Recommends movies based on movie features such as genre, actors, and director.
- Uses **TF-IDF vectorization and cosine similarity** to generate recommendations.
- **Dataset:** The dataset used in this project is from **Kaggle**.
- Project files are structured as follows:
  ```
  Movie Recommender/
  │── Dataset/               # Contains dataset files
  │── MovieRecommender.py                 # Main application script
  │── download_files.py      # Script for downloading necessary pkl files
  │── requirements.txt       # Dependencies
  ```

### 2. Laptop Price Prediction (Regression Models)

- Built a **regression-based pipeline** to predict laptop prices based on hardware specifications.
- Performed detailed **feature engineering**, such as:
- Extracting clock speed from CPU names
- Standardizing and converting storage values
- Used a `ColumnTransformer` to manage both numerical and categorical preprocessing.
- Trained and compared several models:
- Linear Regression
- Ridge Regression
- Decision Tree
- Random Forest (best performer with r² ≈ 0.81)
- XGBoost
- Voting and Stacking Regressors
- **Dataset:** Sourced from **Kaggle**.
- Project files are structured as follows:
```
Laptop Price Predictor/ 
│── dataset.csv # Raw dataset 
│── Laptop_Price_Predictor.ipynb # Main notebook 
│── model_comparison.png # Visual comparison of model scores 
│── requirements.txt # Dependencies
```
## Features

- Multiple machine learning techniques implemented
- Interactive UI for user-friendly experience (if applicable)
- Scalable and efficient algorithms

## Technologies Used

- **Programming Language**: Python
- **Libraries**: Pandas, NumPy, Scikit-learn, TensorFlow/PyTorch (if applicable), Streamlit (if deploying UI)
- **Datasets**: Kaggle, MovieLens, TMDB, or other relevant datasets

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Gunjan564/ML_Projects.git
   cd ML_Projects
   ```
2. Navigate to the specific project directory:
   ```bash
   cd "Movie Recommender"
   ```
3. Create and activate a virtual environment:
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate
   ```
4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the project:
   ```bash
   python MovieRecommender.py
   ```
2. If using Streamlit for UI:
   ```bash
   streamlit run MovieRecommender.py
   ```
3. Interact with the project and analyze results!

## Datasets

- Each project will use appropriate datasets, such as **Kaggle** for movies or **Kaggle/UCI datasets** for other applications.
- Datasets should be placed in the respective `Dataset/` directory inside each project folder.

## Future Projects and Improvements

- Implement **classification models** (e.g., spam detection, sentiment analysis).
- Develop **regression models** (e.g., house price prediction, stock forecasting).
- Work on **computer vision applications** (e.g., object detection, image classification).
- Explore **NLP projects** (e.g., text summarization, chatbot development).
- Enhance UI/UX for better interaction.

## Contributing

Feel free to fork this repository and contribute by submitting a pull request.

## License

This project is licensed under the **MIT License**.

### MIT License

```
MIT License

Copyright (c) 2025 Gunjan564

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

