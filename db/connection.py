# 데이터 베이스 사용 방법

# 1. Connection 맺기 (DB ----> Python)
# - IP : 컴퓨터 주소
# - Port : 27017 (Mongodb 권장 포트)
# - ID & PW : 계정 정보
# 2. 명령 보내기 (Python ----> DB)
# 3. 결과 받기 (DB ----> Python)
# 4. Connection 끊기 (Python XXXX DB)

from pymongo import MongoClient

# MongoDB connetcion
def conn() :
    client = MongoClient("mongodb+srv://cnu:haram1203@cluster0.btlnzq9.mongodb.net/")
    #  → IP, Port, ID&PW
    db = client["movie"]

    collection = db.get_collection("movie")
    return collection
