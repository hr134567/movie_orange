# 데이터 베이스 사용 방법

# 1. Connection 맺기 (DB ----> Python)
# - IP : 컴퓨터 주소
# - Port : 27017 (Mongodb 권장 포트)
# - ID & PW : 계정 정보
# 2. 명령 보내기 (Python ----> DB)
# 3. 결과 받기 (DB ----> Python)
# 4. Connection 끊기 (Python XXXX DB)

# Mongodb 구조
# - Mongodb(DBMS) : 데이터베이스 관리 시스템
#   → DB(NAVER) : 프로젝트 단위
#       ▶ collection (회원) - CRUD
#       ▶ collection (카페) - CRUD
#       ▶ collection (쇼핑) - CRUD
#       ▶ collection (메일) - CRUD
#   → DB(KAKAO)
#   → DB(BLOG)
# Mongodb 데이터 주고 받기
# - Mongodb는 BSON Type으로 데이터를 주고 받음
# - BSON(Binarty JSON) = JSON과 거의 동일
# - 그냥 JSON Type으로 사용하면 됨(문제 없음)
# - Python에서 JSON은 Dict Type 사용!(Python Dict = JSON)

from pymongo import MongoClient

# MongoDB connetcion
def conn() :
    client = MongoClient("mongodb+srv://cnu:haram1203@cluster0.btlnzq9.mongodb.net/")
    #  → mongodb_web : IP, Port, ID&PW
    # Python-mongodb 연결 -> client
    db = client["review"]   # DB 선택
    # collection 선택
    collection = db.get_collection("movie")
    return collection
