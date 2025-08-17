# 📰 Fake News Detection API

This project is a machine learning-powered API that detects whether a news article is **fake** or **real**.  
It uses Natural Language Processing (NLP) techniques and a trained classification model to analyze news content and make predictions.

---

## 🚀 Features

- Detects **fake vs. real news** using trained ML models  
- RESTful API built with **Flask (Python)**  
- Includes a **pre-trained model and vectorizer**  
- Easy-to-use interface for predictions  

---

## 📁 Project Structure

├── main.py              # API entry point  
├── train_model.py       # Script to train the model  
├── model.pkl            # Trained classification model  
├── vectorizer.pkl       # TF-IDF vectorizer  
├── Fake.csv             # Dataset of fake news articles  
├── True.csv             # Dataset of real news articles  
├── requirements.txt     # Python dependencies  




---

## 🧠 How It Works

1. **Data Preprocessing**  
   - Combines `Fake.csv` and `True.csv`  
   - Cleans and labels the text data  

2. **Vectorization**  
   - Uses **TF-IDF Vectorizer** to convert text into numerical features  

3. **Model Training**  
   - Trains a classifier (e.g., Logistic Regression / Naive Bayes)  

4. **Prediction API**  
   - Accepts news text (JSON format)  
   - Returns prediction: `"Fake"` or `"Real"`  

---

## 🛠 Installation

```bash
# Clone the repository
git clone https://github.com/your-username/fake-news-detector.git
cd fake-news-detector

# Install dependencies
pip install -r requirements.txt
```

## 🧪 Usage
Train the Model
```bash
python train_model.py
```

Run the API
```bash
python main.py
```

Example API Request (using curl)
```bash
curl -X POST http://localhost:5000/predict \
     -H "Content-Type: application/json" \
     -d '{"text": "The government has announced a new policy today..."}'
```

Example Response
```json
{
  "prediction": "Real"
}
```

## 📊 Dataset
The dataset consists of two files:
1. Fake.csv → Fake news articles
2. True.csv → Real news articles  
📌 Source: [Kaggle Fake News Dataset](https://www.kaggle.com/clmentbisaillon/fake-and-real-news-dataset)


## 🙌 Acknowledgments
1. Kaggle → For the dataset
2. Scikit-learn → For ML tools
3. Flask → For building the API