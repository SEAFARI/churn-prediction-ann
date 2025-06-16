# Customer Churn Prediction 

## Live Demo

Experience the Customer Churn Prediction system in action! Check out the deployed Streamlit app here:

Streamlit Application: https://churn-prediction-ann-lm53k58dnarlljerpaobzk.streamlit.app/

## Docker Deployment

To ensure reproducibility and simplify deployment, the application is containerized with Docker. Pull the image from Docker Hub:

```bash
# Pull Docker image
docker pull seafari/churn-prediction-ann
```


## Project Overview

This project delivers a complete customer churn prediction system using an Artificial Neural Network (ANN). It covers data loading, preprocessing (including One-Hot Encoding and standardization), model training with  accuracy tracking. The solution is wrapped in a Streamlit web app for interactive use and containerized with Docker for reliable deployment.

## Key Features & Achievements

Data Loading & Preprocessing: Loaded customer dataset, handled missing values, performed One-Hot Encoding (OHE) on categorical features, and standardized numerical values.

Model Training: Implemented an ANN architecture, achieving 86.14% training accuracy and 86.60% validation accuracy by epoch 8 (loss: 0.3399 train, 0.3408 val).

User Interface: Built a Streamlit app for interactive prediction.

Containerized Deployment: Packaged the Streamlit application in a Docker container for consistent, scalable deployment.

## Tech Stack

* Language & Libraries: Python, scikit-learn, Pandas, tensorflow/keras
* Web Framework: Streamlit
* Containerization: Docker
* Version Control: Git & GitHub

## How to Run Locally

1. **Clone the repository**

   ```bash
   git clone https://github.com/SEAFARI/churn-prediction-ann.git
   cd churn-prediction-ann
   ```
2. **Create and activate a virtual environment (optional but recommended)**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```
4. **Run the Streamlit app**

   ```bash
   streamlit run app.py
   ```

## Docker Usage

1. **Build the Docker image**

   ```bash
   docker build -t seafari/churn-prediction-ann .
   ```
2. **Run the container**

   ```bash
   docker run -p 5000:5000 seafari/churn-prediction-ann
   ```
3. **Access** the app at `http://localhost:5000/`.


**If you find this project useful, feel free to  star the repository and share it with others!**
