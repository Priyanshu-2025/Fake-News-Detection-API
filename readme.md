# Fake News Detection API
**Tools:** Python · NLP · TF-IDF · Scikit-learn · Flask
**Accuracy:** 85% classification accuracy on test set

## What this does
A machine learning API that classifies news articles as Real or Fake.
Input: raw news text → Output: prediction with confidence

## How it works
1. **Data:** 40,000+ labelled news articles (Kaggle dataset)
2. **Preprocessing:** Text cleaning, tokenisation, stop-word removal
3. **Vectorisation:** TF-IDF to convert text into numerical features
4. **Model:** Logistic Regression classifier — 85% accuracy on held-out test set
5. **Deployment:** Flask REST API with /predict endpoint

## Results
| Metric | Score |
|--------|-------|
| Accuracy | 85% |
| Precision | ~86% |
| Recall | ~84% |

## API Usage
```bash
# Start the API
python main.py

# Make a prediction
curl -X POST http://localhost:5000/predict \
  -H 'Content-Type: application/json' \
  -d '{"text": "Paste your news article here..."}'

# Response
{ "prediction": "Real", "confidence": 0.91 }
```

## Setup
```bash
git clone https://github.com/Priyanshu-2025/Fake-News-Detection-API.git
pip install -r requirements.txt
python train_model.py   # train and save model
python main.py          # start API
```

## Contact
Priyanshu Rawat · priyanshurawat315@gmail.com
LinkedIn: linkedin.com/in/priyanshu-rawat-b63894249
