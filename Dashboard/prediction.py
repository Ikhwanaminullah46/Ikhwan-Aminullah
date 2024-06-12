import joblib

model = joblib.load('Dashboard/model/ada_model.joblib')
result_target = joblib.load('Dashboard/model/encoder_target.joblib')


def prediction(data):
    """Making prediction
 
    Args:
        data (Pandas DataFrame): Dataframe that contain all the preprocessed data
 
    Returns:
        str: Prediction result (Dropout, Enrolled, Graduate)
    """
    result = model.predict(data)
    final_result = result_target.inverse_transform(result)[0]
    return final_result
