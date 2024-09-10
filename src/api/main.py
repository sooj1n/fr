from typing import Union
from fastapi import FastAPI
from api.knn import knn_api
from api.lr import lr_api

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello", "world"}

@app.get("/items/{item_id}")
def read_time(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.get("/how_weight")
def lr_api(length:float):
    """
    물고기 무게 예측

    Args:
        length (float): 물고기 길이(cm)

    Returns:
        weight (float): 물고기 무게(kg)
    """

    weight = lr_api(l)
    return {"weight": weight}


@app.get("/fish")
def knn_api(length: float, weight:float):
    """
    물고기의 종류 판별기

    Args:
        length (float): 물고기 길이(cm)
        weight (float): 물고기 무게(g)

    Returns:
        dict: 물고기 종류를 담은 딕셔너리
    """

    fish = knn_api(length,weight)

    return {
                "prediction": fish,
                "length": length,
                "weight": weight
            }
