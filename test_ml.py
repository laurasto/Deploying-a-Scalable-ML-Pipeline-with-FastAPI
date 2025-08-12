import pytest
import os
import pandas as pd
from sklearn.model_selection import train_test_split

# TODO: add necessary import
from ml.data import process_data
from ml.model import (
    inference,
    load_model,
    save_model,
    train_model,
)

project_path = r"C:\temp\Deploying-a-Scalable-ML-Pipeline-with-FastAPI"
data_path = os.path.join(project_path, "data", "census.csv")
data = pd.read_csv(data_path)

cat_features = [
    "workclass",
    "education",
    "marital-status",
    "occupation",
    "relationship",
    "race",
    "sex",
    "native-country",
]


# TODO: implement the first test. Change the function name and input as needed
def test_one():
    """
    Test that the data path results in dataframe of
    more than 1 row
    """
    # Your code here
    assert len(data) > 0


# TODO: implement the second test. Change the function name and input as needed
def test_two():
    """
    Test that a model has been saved in subfolder of project_path
    """
    # Your code here
    files = os.listdir(os.path.join(project_path, "model"))
    assert "model.pkl" in files


# TODO: implement the third test. Change the function name and input as needed
def test_three():
    """
    Test that length of predictions equal length of test vector
    """
    # Your code here
    model_path = os.path.join(project_path, "model", "model.pkl")
    encoder_path = os.path.join(project_path, "model", "encoder.pkl")
    # load the model
    model = load_model(model_path)
    train, test = train_test_split(data, test_size=0.3)
    X_train, y_train, encoder, lb = process_data(
        train, categorical_features=cat_features, label="salary", training=True
    )

    encoder = load_model(encoder_path)

    X_test, y_test, _, _ = process_data(
        test,
        categorical_features=cat_features,
        label="salary",
        training=False,
        encoder=encoder,
        lb=lb,
    )
    preds = inference(model, X_test)
    assert len(preds) == len(y_test)
