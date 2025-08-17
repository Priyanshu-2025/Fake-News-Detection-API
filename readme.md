# 📰 Fake News Detection API

This project is a machine learning-powered API that detects whether a news article is **fake** or **real**. It uses natural language processing (NLP) techniques and a trained classification model to analyze news content and make predictions.

## 🚀 Features

- Detects fake vs. real news using trained ML models
- RESTful API built with Python
- Pre-trained model and vectorizer included
- Easy-to-use interface for predictions

## 📁 Project Structure

# 📰 Fake News Detection API

This project is a machine learning-powered API that detects whether a news article is **fake** or **real**. It uses natural language processing (NLP) techniques and a trained classification model to analyze news content and make predictions.

## 🚀 Features

- Detects fake vs. real news using trained ML models
- RESTful API built with Python
- Pre-trained model and vectorizer included
- Easy-to-use interface for predictions

## 📁 Project Structure

├── main.py              # API entry point 
├── train_model.py       # Script to train the model 
├── model.pkl            # Trained classification model 
├── vectorizer.pkl       # TF-IDF vectorizer 
├── Fake.csv             # Dataset of fake news articles 
├── True.csv             # Dataset of real news articles 
├── requirements.txt     # Python dependencies


## 🧠 How It Works

1. **Data Preprocessing**: Combines `Fake.csv` and `True.csv`, cleans text, and labels data.
2. **Vectorization**: Uses TF-IDF to convert text into numerical features.
3. **Model Training**: Trains a classifier (e.g., Logistic Regression or Naive Bayes).
4. **Prediction API**: Accepts news text and returns a prediction.

## 🛠 Installation

```bash
# Clone the repository
git clone https://github.com/your-username/fake-news-detector.git
cd fake-news-detector

# Install dependencies
pip install -r requirements.txt

```

## 🧪 Usage

 1. **Train the Model** 
    ```bash
    python train_model.py
    ```

 2. **Run the API**
    ```bash
    python main.py
    ```

 3. **Example API Request**
    ```bash
    curl -X POST http://localhost:5000/predict \
         -H "Content-Type: application/json" \
         -d '{"text": "The government has announced a new policy today..."}'
    ```

 4. **Response**
    ```json
    {
      "prediction": "Real"
    }
    ```

## 📊 Dataset
├── Fake.csv   
├── True.csv  


## 🙌 Acknowledgments
- Kaggle for the dataset
- Scikit-learn for ML tools
- Flask for building the API
