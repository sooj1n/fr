import pickle

def lr_api(length:float):
    """
    물고기 무게 예측

    Args:
        length (float): 물고기 길이(cm)

    Returns:
        weight (float): 물고기 무게(kg)
    """

    ### 모델 불러오기
    with open("/home/sujin/code/fr/src/note/linear_model.pkl", "rb") as f:
        lr_model = pickle.load(f)

    prediction = lr_model.predict([[length **2, length]])

    return float(prediction[0])