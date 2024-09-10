import pickle

def knn_api(length: float, weight:float):
    """
    물고기의 종류 판별기

    Args:
        length (float): 물고기 길이(cm)
        weight (float): 물고기 무게(g)

    Returns:
        dict: 물고기 종류를 담은 딕셔너리
    """

    ### 모델 불러오기
    with open("/home/sujin/code/fr/src/note/knn_model.pkl", "rb") as f:
        knn_model = pickle.load(f)

    prediction = knn_model.predict([[length, weight]])

    if prediction[0] == 1:
        fish_class = "도미"
    else:
        fish_class = "빙어"

    return fish_class