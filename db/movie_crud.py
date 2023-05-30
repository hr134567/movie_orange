# CRUD
# - create : 생성
# - read   : 조회
# - update : 수정
# - delete : 삭제
from db.connection import conn
# 리뷰 저장(MongoDB)
def add_review(data) :
    collection = conn()
    collection.insert_one(data)        #리뷰 저장
# 리뷰 조회(MongoDB)
def get_reviews() :
     pass