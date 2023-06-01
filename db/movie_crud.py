# CRUD
# - create : 생성
# - read   : 조회
# - update : 수정
# - delete : 삭제
from db.connection import conn
# 리뷰 저장(MongoDB)
def add_review(data) :
    collection = conn()  # Conn(DB : review, Collection : movie) 정보
    # insert_one : 1건 저장(CREATE)
    collection.insert_one(data)    #리뷰 저장
# 리뷰 조회(MongoDB)
def get_reviews() :
     review_list = []    # Mongodb에서 가져온 Data 저장!
     collection = conn()   # connection 맺기!
     # find({조건}, {컬럼 선택}) : 데이터 조회
     # - 조건 예 : 평점 8점 이상 조회
     # - 컬럼 선택 예 : review, score 조회
     #    *컬럼(title, review, scroe, writer, regdate)
     #    *_id(고유한 식별값) 기본으로 조회 설정
     # find()를 통해서 MongoDB에서 데이터를 가져옴(MongoDB Type)
     for one in collection.find({}, {"_id" : 0, "title" : 1, "score" : 1, "review" : 1}) :
         review_list.append([
             one["title"],
             one["review"],
             one["score"]
         ])
     return review_list
