Here’s the updated README.md file content with the new commands added:

### Dropout Detection System

## Overview
This project implements a dropout detection system using a neural network model. The system is built using Flask to provide a RESTful API for making predictions and evaluating the model. The model predicts whether a student is likely to drop out or graduate based on various input features.

## Features
- **Prediction**: The `/predict` endpoint allows users to submit input data and receive a prediction on whether the student will drop out or graduate.
- **Evaluation**: The `/evaluate` endpoint calculates and returns key evaluation metrics like accuracy, precision, recall, and F1 score using the test dataset.
- **Model Training**: Includes functionality to load, train, and save machine learning models.

## Setup and Installation
### 1. Clone the repository
```bash
git clone <repository_url>
cd dropdect
```

### 2. Create and activate a virtual environment (optional but recommended)
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install the required dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the Flask application
```bash
python3 src/app.py
```

## Usage

### Make a Prediction
```bash
curl -X POST -H "Content-Type: application/json" -d '{"input": [1, 8, 5, 2, 1, 1, 1, 13, 10, 6, 10, 1, 0, 0, 1, 1, 0, 20, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10.8, 1.4, 1.74]}' http://127.0.0.1:5000/predict
```

### Evaluating the Model
```bash
curl -X POST http://127.0.0.1:5000/evaluate
```

### Test Model Prediction
To test the model prediction, send a GET request to the `/test_model` endpoint:
```bash
curl -X GET http://127.0.0.1:5000/test_model
```
The response will contain the test prediction:
```json
{
  "test_prediction": [true]
}
```

### Uploading Data
```bash
curl -X POST http://127.0.0.1:5000/upload_data -F "file=@data/train/dataset.csv"
```

### Preprocessing Data
```bash
curl -X POST http://127.0.0.1:5000/preprocess_data
```

### Retraining the Model
```bash
curl -X POST http://127.0.0.1:5000/retrain
```

### Evaluating After Retraining
```bash
curl -X POST http://127.0.0.1:5000/evaluate_after_retraining
```

## File Descriptions
- **src/app.py**: Main Flask application file handling API routes.
- **src/model.py**: Contains functions for model training and loading.
- **src/prediction.py**: Handles the model prediction process.
- **src/preprocessing.py**: Preprocessing steps for cleaning and scaling the input data.
- **data/**: Directory containing training and testing datasets.
- **models/**: Directory storing trained model files.
- **notebook/**: Jupyter notebooks used for exploration and initial model training.
- **others/**: Additional files and models that might be used for future development.

## Future Improvements
- Expand the feature set used for predictions.
- Add more robust error handling and input validation.
- Implement additional model evaluation metrics.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

