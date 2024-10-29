import random
from datetime import datetime, timedelta

# nutrient_data의 샘플 데이터
nutrient_data = {
    "김치찌개": {"kcal": 250, "carbohydrate": 10, "protein": 15, "fat": 18},
    "된장찌개": {"kcal": 200, "carbohydrate": 12, "protein": 10, "fat": 8},
    "순두부찌개": {"kcal": 300, "carbohydrate": 8, "protein": 20, "fat": 15},
    "콩나물국": {"kcal": 150, "carbohydrate": 5, "protein": 8, "fat": 3},
    "떡국": {"kcal": 350, "carbohydrate": 60, "protein": 10, "fat": 5},
    "김치볶음밥": {"kcal": 550, "carbohydrate": 85, "protein": 12, "fat": 20},
    "순대": {"kcal": 400, "carbohydrate": 10, "protein": 18, "fat": 30},
    "제육볶음": {"kcal": 500, "carbohydrate": 20, "protein": 35, "fat": 25},
    "오징어볶음": {"kcal": 300, "carbohydrate": 15, "protein": 30, "fat": 10},
    "열무김치": {"kcal": 50, "carbohydrate": 5, "protein": 2, "fat": 1},
    "아귀찜": {"kcal": 450, "carbohydrate": 12, "protein": 40, "fat": 15},
    "삼계탕": {"kcal": 800, "carbohydrate": 10, "protein": 60, "fat": 50},
    "김치전": {"kcal": 400, "carbohydrate": 40, "protein": 10, "fat": 20},
    "채소전": {"kcal": 350, "carbohydrate": 35, "protein": 8, "fat": 15},
    "파전": {"kcal": 450, "carbohydrate": 45, "protein": 12, "fat": 20},
    "해물파전": {"kcal": 500, "carbohydrate": 40, "protein": 20, "fat": 25},
    "중화비빔면": {"kcal": 600, "carbohydrate": 90, "protein": 15, "fat": 18},
    "해물탕": {"kcal": 300, "carbohydrate": 10, "protein": 40, "fat": 8},
    "오징어국": {"kcal": 200, "carbohydrate": 5, "protein": 20, "fat": 5},
    "설렁탕": {"kcal": 600, "carbohydrate": 20, "protein": 40, "fat": 30},
    "육개장": {"kcal": 400, "carbohydrate": 10, "protein": 30, "fat": 15},
    "우거지국": {"kcal": 150, "carbohydrate": 5, "protein": 10, "fat": 5},
    "김치국": {"kcal": 200, "carbohydrate": 8, "protein": 10, "fat": 7},
    "북엇국": {"kcal": 180, "carbohydrate": 5, "protein": 15, "fat": 3},
    "시래기국": {"kcal": 150, "carbohydrate": 5, "protein": 8, "fat": 3},
    "배추국": {"kcal": 130, "carbohydrate": 6, "protein": 6, "fat": 2},
    "황태국": {"kcal": 200, "carbohydrate": 5, "protein": 25, "fat": 2},
    "피쉬 앤 칩스": {"kcal": 800, "carbohydrate": 60, "protein": 40, "fat": 40},
    "닭갈비": {"kcal": 600, "carbohydrate": 20, "protein": 35, "fat": 30},
    "감자탕": {"kcal": 700, "carbohydrate": 30, "protein": 50, "fat": 30},
    "육회": {"kcal": 300, "carbohydrate": 5, "protein": 30, "fat": 20},
    "족발": {"kcal": 800, "carbohydrate": 10, "protein": 50, "fat": 60},
    "오삼불고기": {"kcal": 550, "carbohydrate": 20, "protein": 35, "fat": 30},
    "꼬막비빔밥": {"kcal": 500, "carbohydrate": 80, "protein": 20, "fat": 10},
    "황태해장국": {"kcal": 180, "carbohydrate": 5, "protein": 25, "fat": 2},
    "김치볶음면": {"kcal": 600, "carbohydrate": 90, "protein": 15, "fat": 18},
    "곰탕": {"kcal": 600, "carbohydrate": 10, "protein": 50, "fat": 40},
    "비지찌개": {"kcal": 350, "carbohydrate": 10, "protein": 20, "fat": 15},
    "청국장": {"kcal": 300, "carbohydrate": 20, "protein": 25, "fat": 10},
    "매운갈비찜": {"kcal": 800, "carbohydrate": 30, "protein": 60, "fat": 40},
    "보리밥": {"kcal": 200, "carbohydrate": 45, "protein": 6, "fat": 2},
    "떡만두국": {"kcal": 450, "carbohydrate": 60, "protein": 15, "fat": 10},
    "오징어순대": {"kcal": 300, "carbohydrate": 12, "protein": 25, "fat": 10},
    "삼합": {"kcal": 600, "carbohydrate": 20, "protein": 50, "fat": 30},
    "부대찌개": {"kcal": 700, "carbohydrate": 30, "protein": 30, "fat": 40},
    "해물라면": {"kcal": 550, "carbohydrate": 80, "protein": 20, "fat": 15},
    "쭈꾸미볶음": {"kcal": 350, "carbohydrate": 10, "protein": 30, "fat": 10},
    "꽁치구이": {"kcal": 300, "carbohydrate": 5, "protein": 25, "fat": 15},
    "멘보샤": {"kcal": 450, "carbohydrate": 30, "protein": 15, "fat": 25},
    "양꼬치": {"kcal": 350, "carbohydrate": 5, "protein": 30, "fat": 20},
    "마라탕": {"kcal": 600, "carbohydrate": 20, "protein": 30, "fat": 30},
    "마라샹궈": {"kcal": 550, "carbohydrate": 15, "protein": 35, "fat": 35},
    "소룡포": {"kcal": 300, "carbohydrate": 25, "protein": 15, "fat": 10},
    "북경오리": {"kcal": 900, "carbohydrate": 10, "protein": 60, "fat": 70},
    "짜장밥": {"kcal": 600, "carbohydrate": 90, "protein": 20, "fat": 25},
    "유니짜장": {"kcal": 550, "carbohydrate": 80, "protein": 15, "fat": 20},
    "마파면": {"kcal": 650, "carbohydrate": 90, "protein": 25, "fat": 20},
    "훈툰": {"kcal": 300, "carbohydrate": 35, "protein": 10, "fat": 10},
    "깐쇼새우덮밥": {"kcal": 500, "carbohydrate": 70, "protein": 20, "fat": 15},
    "사천식 돼지고기 볶음": {"kcal": 600, "carbohydrate": 15, "protein": 40, "fat": 30},
    "라조기": {"kcal": 700, "carbohydrate": 20, "protein": 45, "fat": 35},
    "꿔바로우": {"kcal": 800, "carbohydrate": 60, "protein": 30, "fat": 50},
    "꿔바로우 샐러드": {"kcal": 700, "carbohydrate": 50, "protein": 20, "fat": 40},
    "삼선짬뽕밥": {"kcal": 600, "carbohydrate": 80, "protein": 25, "fat": 20},
    "건두부볶음": {"kcal": 400, "carbohydrate": 15, "protein": 20, "fat": 20},
    "마라양념탕수육": {"kcal": 750, "carbohydrate": 50, "protein": 35, "fat": 45},
    "해물볶음우동": {"kcal": 550, "carbohydrate": 85, "protein": 20, "fat": 10},
    "초밥": {"kcal": 400, "carbohydrate": 60, "protein": 15, "fat": 5},
    "우동": {"kcal": 450, "carbohydrate": 70, "protein": 10, "fat": 5},
    "덴푸라": {"kcal": 600, "carbohydrate": 40, "protein": 15, "fat": 40},
    "규동": {"kcal": 500, "carbohydrate": 60, "protein": 30, "fat": 15},
    "오니기리": {"kcal": 350, "carbohydrate": 70, "protein": 8, "fat": 3},
    "카츠돈": {"kcal": 700, "carbohydrate": 80, "protein": 30, "fat": 30},
    "라멘": {"kcal": 550, "carbohydrate": 85, "protein": 20, "fat": 15},
    "미소시루": {"kcal": 50, "carbohydrate": 5, "protein": 5, "fat": 1},
    "타코야키": {"kcal": 350, "carbohydrate": 45, "protein": 10, "fat": 15},
    "오코노미야키": {"kcal": 600, "carbohydrate": 60, "protein": 20, "fat": 30},
    "소바": {"kcal": 300, "carbohydrate": 50, "protein": 10, "fat": 5},
    "규카츠 덮밥": {"kcal": 700, "carbohydrate": 80, "protein": 30, "fat": 25},
    "하이라이스": {"kcal": 550, "carbohydrate": 70, "protein": 15, "fat": 15},
    "오차즈케": {"kcal": 300, "carbohydrate": 60, "protein": 10, "fat": 2},
    "규카츠": {"kcal": 600, "carbohydrate": 15, "protein": 30, "fat": 35},
    "장어덮밥": {"kcal": 650, "carbohydrate": 80, "protein": 30, "fat": 20},
    "니쿠자가": {"kcal": 500, "carbohydrate": 20, "protein": 40, "fat": 25},
    "가이센동": {"kcal": 400, "carbohydrate": 70, "protein": 15, "fat": 5},
    "타마고야키": {"kcal": 150, "carbohydrate": 5, "protein": 6, "fat": 10},
    "오야코동": {"kcal": 600, "carbohydrate": 80, "protein": 20, "fat": 20},
    "시메사바": {"kcal": 300, "carbohydrate": 5, "protein": 25, "fat": 15},
    "카마메시": {"kcal": 550, "carbohydrate": 80, "protein": 20, "fat": 15},
    "이카메시": {"kcal": 400, "carbohydrate": 60, "protein": 20, "fat": 10},
    "나가사키 짬뽕": {"kcal": 550, "carbohydrate": 80, "protein": 20, "fat": 10},
    "우나기": {"kcal": 400, "carbohydrate": 10, "protein": 30, "fat": 20},
    "샤케동": {"kcal": 500, "carbohydrate": 80, "protein": 20, "fat": 10},
    "에비텐동": {"kcal": 600, "carbohydrate": 70, "protein": 20, "fat": 25},
    "가츠샌드": {"kcal": 550, "carbohydrate": 80, "protein": 25, "fat": 20},
    "메밀국수 샐러드": {"kcal": 300, "carbohydrate": 50, "protein": 10, "fat": 5},
    "피자": {"kcal": 800, "carbohydrate": 100, "protein": 25, "fat": 35},
    "햄버거": {"kcal": 600, "carbohydrate": 50, "protein": 25, "fat": 30},
    "스테이크": {"kcal": 700, "carbohydrate": 5, "protein": 60, "fat": 40},
    "치즈버거": {"kcal": 750, "carbohydrate": 45, "protein": 30, "fat": 40},
    "브루스케타": {"kcal": 250, "carbohydrate": 30, "protein": 5, "fat": 10},
    "타코": {"kcal": 350, "carbohydrate": 40, "protein": 15, "fat": 15},
    "부리또": {"kcal": 600, "carbohydrate": 80, "protein": 25, "fat": 25},
    "퀘사디아": {"kcal": 550, "carbohydrate": 65, "protein": 20, "fat": 30},
    "프렌치 토스트": {"kcal": 450, "carbohydrate": 60, "protein": 10, "fat": 15},
    "페퍼로니 피자": {"kcal": 850, "carbohydrate": 90, "protein": 30, "fat": 40},
    "바베큐 치킨 피자": {"kcal": 900, "carbohydrate": 85, "protein": 35, "fat": 45},
    "감자 샐러드": {"kcal": 250, "carbohydrate": 30, "protein": 5, "fat": 10},
    "새우 크림 리조또": {"kcal": 550, "carbohydrate": 70, "protein": 15, "fat": 25},
    "마르게리타 피자": {"kcal": 700, "carbohydrate": 85, "protein": 20, "fat": 30},
    "알리오 올리오": {"kcal": 600, "carbohydrate": 85, "protein": 15, "fat": 25},
    "까르보나라 파스타": {"kcal": 800, "carbohydrate": 90, "protein": 20, "fat": 40},
    "랍스터 롤": {"kcal": 500, "carbohydrate": 60, "protein": 25, "fat": 20},
    "맥 앤 치즈": {"kcal": 700, "carbohydrate": 75, "protein": 20, "fat": 35},
    "치킨 너겟": {"kcal": 400, "carbohydrate": 20, "protein": 20, "fat": 25},
    "연어 스테이크": {"kcal": 500, "carbohydrate": 5, "protein": 40, "fat": 30},
    "비스크 수프": {"kcal": 400, "carbohydrate": 30, "protein": 15, "fat": 20},
    "클램 차우더": {"kcal": 500, "carbohydrate": 40, "protein": 20, "fat": 25},
    "스테이크 타르타르": {"kcal": 450, "carbohydrate": 0, "protein": 35, "fat": 30},
    "훈제 연어 샐러드": {"kcal": 300, "carbohydrate": 5, "protein": 20, "fat": 15},
    "바질 페스토 샌드위치": {"kcal": 500, "carbohydrate": 60, "protein": 10, "fat": 20},
    "파인애플 볶음밥": {"kcal": 600, "carbohydrate": 85, "protein": 10, "fat": 15},
    "갈릭 새우 파스타": {"kcal": 650, "carbohydrate": 80, "protein": 20, "fat": 30},
    "참치 샌드위치": {"kcal": 450, "carbohydrate": 50, "protein": 20, "fat": 15},
    "포크 롤": {"kcal": 550, "carbohydrate": 60, "protein": 25, "fat": 20},
    "비프 브루기뇽": {"kcal": 600, "carbohydrate": 10, "protein": 50, "fat": 35},
    "치킨 알프레도": {"kcal": 700, "carbohydrate": 85, "protein": 25, "fat": 30},
    "수제비": {"kcal": 300, "carbohydrate": 60, "protein": 10, "fat": 5},
    "철판 볶음밥": {"kcal": 600, "carbohydrate": 80, "protein": 15, "fat": 20},
    "잔치국수": {"kcal": 400, "carbohydrate": 70, "protein": 10, "fat": 8},
    "초계국수": {"kcal": 350, "carbohydrate": 60, "protein": 15, "fat": 5},
    "오삼불고기 찌개": {"kcal": 500, "carbohydrate": 25, "protein": 30, "fat": 20},
    "초계비빔국수": {"kcal": 450, "carbohydrate": 65, "protein": 15, "fat": 10},
    "연어구이": {"kcal": 350, "carbohydrate": 5, "protein": 30, "fat": 20},
    "방어구이": {"kcal": 400, "carbohydrate": 5, "protein": 35, "fat": 25},
    "전어구이": {"kcal": 300, "carbohydrate": 5, "protein": 25, "fat": 10},
    "도미구이": {"kcal": 350, "carbohydrate": 5, "protein": 30, "fat": 15},
    "새우완자": {"kcal": 300, "carbohydrate": 15, "protein": 20, "fat": 15},
    "갈치구이": {"kcal": 350, "carbohydrate": 5, "protein": 30, "fat": 20},
    "우렁강된장": {"kcal": 200, "carbohydrate": 10, "protein": 20, "fat": 8},
    "차돌박이 된장찌개": {"kcal": 450, "carbohydrate": 15, "protein": 25, "fat": 30},
    "수박 샐러드": {"kcal": 100, "carbohydrate": 25, "protein": 2, "fat": 0},
    "무채 비빔국수": {"kcal": 400, "carbohydrate": 70, "protein": 10, "fat": 10},
    "숙성지 김치찌개": {"kcal": 300, "carbohydrate": 12, "protein": 18, "fat": 20},
    "임연수구이": {"kcal": 300, "carbohydrate": 0, "protein": 30, "fat": 18},
    "가자미구이": {"kcal": 250, "carbohydrate": 0, "protein": 25, "fat": 12},
    "붕장어구이": {"kcal": 500, "carbohydrate": 5, "protein": 40, "fat": 35},
    "고추참치 김밥": {"kcal": 350, "carbohydrate": 55, "protein": 12, "fat": 8},
    "날치알 김밥": {"kcal": 320, "carbohydrate": 50, "protein": 10, "fat": 8},
    "유부 김밥": {"kcal": 300, "carbohydrate": 55, "protein": 6, "fat": 5},
    "곱창볶음": {"kcal": 600, "carbohydrate": 20, "protein": 40, "fat": 40},
    "백합탕": {"kcal": 250, "carbohydrate": 8, "protein": 30, "fat": 10},
    "파김치장어전골": {"kcal": 500, "carbohydrate": 15, "protein": 45, "fat": 30},
    "해물 수제비": {"kcal": 400, "carbohydrate": 70, "protein": 20, "fat": 10},
    "감자찌개": {"kcal": 300, "carbohydrate": 40, "protein": 10, "fat": 10},
    "애호박찌개": {"kcal": 250, "carbohydrate": 20, "protein": 8, "fat": 5},
    "비빔냉면": {"kcal": 450, "carbohydrate": 70, "protein": 12, "fat": 10},
    "두부전골": {"kcal": 350, "carbohydrate": 15, "protein": 25, "fat": 20},
    "매운 갈비찜 찌개": {"kcal": 700, "carbohydrate": 30, "protein": 50, "fat": 40},
    "갈비탕": {"kcal": 550, "carbohydrate": 15, "protein": 45, "fat": 30},
    "잡채밥": {"kcal": 600, "carbohydrate": 90, "protein": 20, "fat": 15},
    "잡채": {"kcal": 600, "carbohydrate": 90, "protein": 20, "fat": 15},
    "라면": {"kcal": 500, "carbohydrate": 70, "protein": 15, "fat": 20},
    "불닭": {"kcal": 700, "carbohydrate": 30, "protein": 40, "fat": 35},
    "팥죽": {"kcal": 300, "carbohydrate": 60, "protein": 5, "fat": 3},
    "어묵탕": {"kcal": 250, "carbohydrate": 10, "protein": 15, "fat": 10},
    "돈카츠 회오리 오므라이스": {"kcal": 700, "carbohydrate": 50, "protein": 25, "fat": 40},
    "호박전": {"kcal": 300, "carbohydrate": 40, "protein": 10, "fat": 12},
    "크림수프": {"kcal": 400, "carbohydrate": 30, "protein": 10, "fat": 25},
    "새우볶음밥": {"kcal": 500, "carbohydrate": 80, "protein": 20, "fat": 8},
    "짬뽕": {"kcal": 650, "carbohydrate": 90, "protein": 20, "fat": 15},
    "닭강정": {"kcal": 550, "carbohydrate": 40, "protein": 30, "fat": 25},
    "고등어조림": {"kcal": 400, "carbohydrate": 5, "protein": 35, "fat": 25},
    "칼국수": {"kcal": 500, "carbohydrate": 70, "protein": 25, "fat": 10},
    "마늘빵": {"kcal": 400, "carbohydrate": 50, "protein": 8, "fat": 15},
    "토마토 바질 스프": {"kcal": 200, "carbohydrate": 30, "protein": 5, "fat": 5},
    "애호박전": {"kcal": 150, "carbohydrate": 10, "protein": 5, "fat": 8},
    "동태찌개": {"kcal": 300, "carbohydrate": 10, "protein": 25, "fat": 8},
    "가자미조림": {"kcal": 350, "carbohydrate": 10, "protein": 30, "fat": 15},
    "고등어구이": {"kcal": 500, "carbohydrate": 20, "protein": 35, "fat": 25},
    "베이글 샌드위치": {"kcal": 400, "carbohydrate": 40, "protein": 20, "fat": 15},
    "참치국": {"kcal": 180, "carbohydrate": 5, "protein": 20, "fat": 7},
    "사골국": {"kcal": 300, "carbohydrate": 10, "protein": 25, "fat": 18},
    "버섯국": {"kcal": 150, "carbohydrate": 6, "protein": 8, "fat": 4},
    "낙지탕탕이": {"kcal": 200, "carbohydrate": 5, "protein": 25, "fat": 6},
    "우렁 된장찌개": {"kcal": 250, "carbohydrate": 12, "protein": 20, "fat": 10},
    "해물된장찌개": {"kcal": 280, "carbohydrate": 15, "protein": 22, "fat": 12},
    "필라프": {"kcal": 550, "carbohydrate": 85, "protein": 15, "fat": 20},
    "연어 김밥": {"kcal": 350, "carbohydrate": 55, "protein": 15, "fat": 10},
    "전주비빔밥": {"kcal": 550, "carbohydrate": 80, "protein": 15, "fat": 10},
    "리조또": {"kcal": 600, "carbohydrate": 85, "protein": 15, "fat": 20},
    "돈부리": {"kcal": 650, "carbohydrate": 85, "protein": 20, "fat": 20},
    "카레라이스": {"kcal": 600, "carbohydrate": 90, "protein": 15, "fat": 10},
    "굴밥": {"kcal": 400, "carbohydrate": 60, "protein": 25, "fat": 10},
    "가마솥밥": {"kcal": 550, "carbohydrate": 85, "protein": 10, "fat": 10},
    "소고기덮밥": {"kcal": 700, "carbohydrate": 90, "protein": 30, "fat": 25},
    "참치마요덮밥": {"kcal": 550, "carbohydrate": 85, "protein": 20, "fat": 15},
    "참치볶음밥": {"kcal": 500, "carbohydrate": 80, "protein": 15, "fat": 10},
    "깻잎 김밥": {"kcal": 320, "carbohydrate": 50, "protein": 10, "fat": 5},
    "야채 김밥": {"kcal": 300, "carbohydrate": 60, "protein": 5, "fat": 5},
    "참치 김밥": {"kcal": 350, "carbohydrate": 55, "protein": 15, "fat": 8},
    "소고기 김밥": {"kcal": 350, "carbohydrate": 55, "protein": 12, "fat": 10},
    "버섯 리소토": {"kcal": 550, "carbohydrate": 75, "protein": 15, "fat": 15},
    "로코모코": {"kcal": 650, "carbohydrate": 85, "protein": 25, "fat": 20},
    "참치 비빔밥": {"kcal": 500, "carbohydrate": 75, "protein": 20, "fat": 10},
    "트러플 리소토": {"kcal": 600, "carbohydrate": 85, "protein": 15, "fat": 25},
    "계란 김밥": {"kcal": 300, "carbohydrate": 55, "protein": 8, "fat": 5},
    "토마토 리소토": {"kcal": 500, "carbohydrate": 75, "protein": 10, "fat": 15},
    "감바스 리조또": {"kcal": 600, "carbohydrate": 85, "protein": 20, "fat": 20},
    "멸치 김밥": {"kcal": 320, "carbohydrate": 55, "protein": 10, "fat": 5},
    "새우 김밥": {"kcal": 350, "carbohydrate": 55, "protein": 15, "fat": 10},
    "유부 초밥": {"kcal": 300, "carbohydrate": 65, "protein": 6, "fat": 5},
    "불고기 덮밥": {"kcal": 600, "carbohydrate": 85, "protein": 25, "fat": 15},
    "제육덮밥": {"kcal": 650, "carbohydrate": 80, "protein": 30, "fat": 20},
    "돈가스 김밥": {"kcal": 450, "carbohydrate": 55, "protein": 20, "fat": 18},
    "카레": {"kcal": 600, "carbohydrate": 90, "protein": 15, "fat": 10},
    "치킨 필라프": {"kcal": 550, "carbohydrate": 85, "protein": 20, "fat": 15},
    "타이 그린 카레": {"kcal": 600, "carbohydrate": 80, "protein": 15, "fat": 25},
    "버섯 볶음밥": {"kcal": 450, "carbohydrate": 80, "protein": 10, "fat": 10},
    "마파두부밥": {"kcal": 550, "carbohydrate": 75, "protein": 20, "fat": 20},
    "베이컨 김밥": {"kcal": 350, "carbohydrate": 55, "protein": 15, "fat": 10},
    "닭갈비 덮밥": {"kcal": 650, "carbohydrate": 80, "protein": 25, "fat": 20},
    "새우 카레라이스": {"kcal": 550, "carbohydrate": 80, "protein": 15, "fat": 15},
    "날치알 주먹밥": {"kcal": 350, "carbohydrate": 55, "protein": 8, "fat": 6},
    "회덮밥": {"kcal": 400, "carbohydrate": 70, "protein": 30, "fat": 8},
    "부타동": {"kcal": 650, "carbohydrate": 85, "protein": 25, "fat": 20},
    "가츠동": {"kcal": 700, "carbohydrate": 80, "protein": 30, "fat": 30},
    "새우가츠동": {"kcal": 750, "carbohydrate": 85, "protein": 30, "fat": 35},
    "가라아게가츠동": {"kcal": 700, "carbohydrate": 80, "protein": 30, "fat": 35},
    "월남쌈": {"kcal": 300, "carbohydrate": 60, "protein": 10, "fat": 8},
    "짬짜면": {"kcal": 700, "carbohydrate": 100, "protein": 20, "fat": 25},
    "회냉면": {"kcal": 450, "carbohydrate": 70, "protein": 15, "fat": 10},
    "트러플 파스타": {"kcal": 750, "carbohydrate": 95, "protein": 20, "fat": 35},
    "양송이 크림파스타": {"kcal": 700, "carbohydrate": 80, "protein": 15, "fat": 30},
    "아부라소바": {"kcal": 600, "carbohydrate": 75, "protein": 15, "fat": 25},
    "연어 파스타": {"kcal": 550, "carbohydrate": 75, "protein": 25, "fat": 15},
    "카라이라멘": {"kcal": 650, "carbohydrate": 90, "protein": 20, "fat": 15},
    "미트볼 파스타": {"kcal": 700, "carbohydrate": 85, "protein": 25, "fat": 25},
    "유산슬": {"kcal": 500, "carbohydrate": 30, "protein": 25, "fat": 20},
    "돈코츠라멘": {"kcal": 600, "carbohydrate": 90, "protein": 20, "fat": 25},
    "고추짬뽕": {"kcal": 700, "carbohydrate": 95, "protein": 20, "fat": 20},
    "야끼소바": {"kcal": 650, "carbohydrate": 90, "protein": 15, "fat": 20},
    "쌀국수": {"kcal": 500, "carbohydrate": 80, "protein": 15, "fat": 8},
    "라볶이": {"kcal": 550, "carbohydrate": 90, "protein": 10, "fat": 10},
    "교카이라멘": {"kcal": 600, "carbohydrate": 85, "protein": 20, "fat": 20},
    "명란 크림파스타": {"kcal": 750, "carbohydrate": 90, "protein": 20, "fat": 35},
    "토마토 갈릭 파스타": {"kcal": 650, "carbohydrate": 85, "protein": 15, "fat": 25},
    "차슈 라멘": {"kcal": 700, "carbohydrate": 90, "protein": 25, "fat": 20},
    "블랙 올리브 파스타": {"kcal": 650, "carbohydrate": 85, "protein": 15, "fat": 25},
    "투움바 파스타": {"kcal": 800, "carbohydrate": 90, "protein": 25, "fat": 40},
    "바질소바": {"kcal": 500, "carbohydrate": 75, "protein": 10, "fat": 15},
    "크림 시금치 파스타": {"kcal": 700, "carbohydrate": 90, "protein": 20, "fat": 35},
    "마라짬뽕": {"kcal": 700, "carbohydrate": 90, "protein": 25, "fat": 20},
    "쫄면": {"kcal": 500, "carbohydrate": 80, "protein": 12, "fat": 10},
    "바질 파스타": {"kcal": 650, "carbohydrate": 90, "protein": 15, "fat": 25},
    "트러플 마카로니": {"kcal": 700, "carbohydrate": 85, "protein": 15, "fat": 35},
    "시저 파스타 샐러드": {"kcal": 400, "carbohydrate": 60, "protein": 10, "fat": 15},
    "살몬 크림 파스타": {"kcal": 650, "carbohydrate": 85, "protein": 25, "fat": 30},
    "까르보나라 불닭볶음면": {"kcal": 800, "carbohydrate": 90, "protein": 20, "fat": 40},
    "매콤로제파스타": {"kcal": 700, "carbohydrate": 85, "protein": 20, "fat": 35},
    "상하이볶음면": {"kcal": 750, "carbohydrate": 90, "protein": 25, "fat": 25},
    "아란치니": {"kcal": 400, "carbohydrate": 60, "protein": 10, "fat": 20},
    "에그 베네딕트": {"kcal": 300, "carbohydrate": 25, "protein": 15, "fat": 15},
    "베이컨 에그 베네딕트": {"kcal": 400, "carbohydrate": 30, "protein": 20, "fat": 20},
    "크로와상 샌드위치": {"kcal": 350, "carbohydrate": 35, "protein": 15, "fat": 20},
    "햄 치즈 파니니": {"kcal": 500, "carbohydrate": 50, "protein": 20, "fat": 25},
    "샐러드 피자": {"kcal": 600, "carbohydrate": 70, "protein": 20, "fat": 25},
    "감자 피자": {"kcal": 700, "carbohydrate": 90, "protein": 20, "fat": 30},
    "시금치 피자": {"kcal": 650, "carbohydrate": 80, "protein": 20, "fat": 25},
    "찐빵": {"kcal": 250, "carbohydrate": 50, "protein": 6, "fat": 4},
    "애호박 라자냐": {"kcal": 400, "carbohydrate": 45, "protein": 15, "fat": 18},
    "치킨 팟파이": {"kcal": 500, "carbohydrate": 50, "protein": 25, "fat": 20},
    "클럽 샌드위치": {"kcal": 550, "carbohydrate": 60, "protein": 25, "fat": 25},
    "디아블로 피자": {"kcal": 800, "carbohydrate": 90, "protein": 25, "fat": 35},
    "포테이토베이컨 피자": {"kcal": 750, "carbohydrate": 85, "protein": 30, "fat": 40},
    "와플 샌드위치": {"kcal": 500, "carbohydrate": 60, "protein": 15, "fat": 25},
    "페스토 샌드위치": {"kcal": 450, "carbohydrate": 50, "protein": 15, "fat": 20},
    "시나몬 롤": {"kcal": 400, "carbohydrate": 70, "protein": 5, "fat": 15},
    "치킨 시저랩": {"kcal": 500, "carbohydrate": 45, "protein": 25, "fat": 25},
    "바나나 브레드": {"kcal": 350, "carbohydrate": 60, "protein": 5, "fat": 10},
    "토마토 모차렐라 피자": {"kcal": 700, "carbohydrate": 90, "protein": 25, "fat": 30},
    "크로크무슈": {"kcal": 450, "carbohydrate": 40, "protein": 20, "fat": 25},
    "크림 바질 피자": {"kcal": 800, "carbohydrate": 85, "protein": 25, "fat": 35},
    "바질페스토 피자": {"kcal": 750, "carbohydrate": 90, "protein": 20, "fat": 30},
    "프레즐": {"kcal": 300, "carbohydrate": 60, "protein": 5, "fat": 5},
    "토마토 치즈 타르트": {"kcal": 400, "carbohydrate": 50, "protein": 10, "fat": 20},
    "베지터블 라자냐": {"kcal": 450, "carbohydrate": 50, "protein": 20, "fat": 20},
    "아보카도 토스트": {"kcal": 350, "carbohydrate": 40, "protein": 10, "fat": 15},
    "비건 버거": {"kcal": 500, "carbohydrate": 60, "protein": 15, "fat": 20},
    "브런치 세트": {"kcal": 600, "carbohydrate": 70, "protein": 25, "fat": 25},
    "살사 치킨 타코": {"kcal": 400, "carbohydrate": 50, "protein": 15, "fat": 15},
    "청포묵": {"kcal": 50, "carbohydrate": 10, "protein": 1, "fat": 0},
    "라따뚜이": {"kcal": 150, "carbohydrate": 15, "protein": 3, "fat": 8},
    "레몬 허니 샐러드": {"kcal": 120, "carbohydrate": 25, "protein": 1, "fat": 2},
    "버팔로 치킨 샐러드": {"kcal": 300, "carbohydrate": 15, "protein": 20, "fat": 18},
    "사우전 아일랜드 샐러드": {"kcal": 180, "carbohydrate": 20, "protein": 2, "fat": 10},
    "브로콜리 샐러드": {"kcal": 80, "carbohydrate": 15, "protein": 3, "fat": 2},
    "토마토 달걀 볶음": {"kcal": 200, "carbohydrate": 10, "protein": 10, "fat": 12},
    "치즈 옥수수": {"kcal": 250, "carbohydrate": 30, "protein": 10, "fat": 12},
    "트로피컬 샐러드": {"kcal": 150, "carbohydrate": 30, "protein": 2, "fat": 3},
    "오리엔탈 드레싱 샐러드": {"kcal": 120, "carbohydrate": 10, "protein": 2, "fat": 8},
    "파파야 샐러드": {"kcal": 100, "carbohydrate": 25, "protein": 2, "fat": 1},
    "비트 샐러드": {"kcal": 60, "carbohydrate": 12, "protein": 2, "fat": 1},
    "렌틸콩 샐러드": {"kcal": 200, "carbohydrate": 30, "protein": 10, "fat": 5},
    "참치 니스와 샐러드": {"kcal": 350, "carbohydrate": 25, "protein": 20, "fat": 15},
    "푸아그라": {"kcal": 450, "carbohydrate": 3, "protein": 13, "fat": 43},
    "한우구이": {"kcal": 400, "carbohydrate": 1, "protein": 20, "fat": 35},
    "양고기 찹스": {"kcal": 300, "carbohydrate": 0, "protein": 25, "fat": 20},
    "닭다리 구이": {"kcal": 210, "carbohydrate": 0, "protein": 28, "fat": 10},
    "꽃목살": {"kcal": 380, "carbohydrate": 0, "protein": 25, "fat": 30},
    "양갈비": {"kcal": 350, "carbohydrate": 0, "protein": 30, "fat": 25},
    "오향장육": {"kcal": 500, "carbohydrate": 10, "protein": 40, "fat": 30},
    "미트로프": {"kcal": 320, "carbohydrate": 15, "protein": 25, "fat": 18},
    "소대창": {"kcal": 400, "carbohydrate": 0, "protein": 30, "fat": 30},
    "소막창": {"kcal": 450, "carbohydrate": 0, "protein": 30, "fat": 35},
    "사과 소스 포크": {"kcal": 350, "carbohydrate": 20, "protein": 25, "fat": 15},
    "토마호크 스테이크": {"kcal": 600, "carbohydrate": 0, "protein": 60, "fat": 40},
    "비프 타르타르": {"kcal": 250, "carbohydrate": 0, "protein": 20, "fat": 18},
    "갈비구이": {"kcal": 450, "carbohydrate": 5, "protein": 40, "fat": 30},
    "코코넛 치킨": {"kcal": 300, "carbohydrate": 15, "protein": 20, "fat": 18},
    "닭봉구이": {"kcal": 180, "carbohydrate": 0, "protein": 22, "fat": 10},
    "소갈비살": {"kcal": 450, "carbohydrate": 0, "protein": 30, "fat": 35},
    "모듬카츠": {"kcal": 700, "carbohydrate": 60, "protein": 30, "fat": 35},
    "히레카츠": {"kcal": 600, "carbohydrate": 50, "protein": 25, "fat": 30},
    "갈매기살": {"kcal": 350, "carbohydrate": 0, "protein": 30, "fat": 25},
    "튀김만두": {"kcal": 450, "carbohydrate": 50, "protein": 10, "fat": 20},
    "고구마튀김": {"kcal": 350, "carbohydrate": 80, "protein": 2, "fat": 15},
    "단호박튀김": {"kcal": 300, "carbohydrate": 60, "protein": 2, "fat": 10},
    "스윗 칠리 새우": {"kcal": 500, "carbohydrate": 45, "protein": 20, "fat": 25},
    "오징어 튀김": {"kcal": 400, "carbohydrate": 30, "protein": 20, "fat": 25},
    "치즈스틱": {"kcal": 350, "carbohydrate": 20, "protein": 10, "fat": 25},
    "양파 링": {"kcal": 400, "carbohydrate": 50, "protein": 5, "fat": 20},
    "고로케": {"kcal": 500, "carbohydrate": 60, "protein": 10, "fat": 20},
    "튀김우동": {"kcal": 400, "carbohydrate": 55, "protein": 8, "fat": 15},
    "칠리 치즈 감자튀김": {"kcal": 600, "carbohydrate": 60, "protein": 10, "fat": 35},
    "야채튀김": {"kcal": 300, "carbohydrate": 40, "protein": 5, "fat": 15},
    "트러플 감자튀김": {"kcal": 550, "carbohydrate": 60, "protein": 5, "fat": 30},
    "블랙빈 수프": {"kcal": 350, "carbohydrate": 50, "protein": 15, "fat": 10},
    "토마토 수프": {"kcal": 180, "carbohydrate": 30, "protein": 5, "fat": 5},
    "랍스터 비스크": {"kcal": 450, "carbohydrate": 20, "protein": 25, "fat": 30},
    "양송이 수프": {"kcal": 300, "carbohydrate": 25, "protein": 5, "fat": 15},
    "아스파라거스 수프": {"kcal": 250, "carbohydrate": 20, "protein": 5, "fat": 15},
    "브로콜리 체다 수프": {"kcal": 400, "carbohydrate": 30, "protein": 15, "fat": 25},
    "감자크림수프": {"kcal": 350, "carbohydrate": 35, "protein": 5, "fat": 20},
    "시금치 수프": {"kcal": 200, "carbohydrate": 25, "protein": 5, "fat": 10},
    "호박 수프": {"kcal": 180, "carbohydrate": 35, "protein": 3, "fat": 5},
    "프렌치 어니언 수프": {"kcal": 300, "carbohydrate": 40, "protein": 5, "fat": 10},
    "호박죽": {"kcal": 300, "carbohydrate": 60, "protein": 5, "fat": 3},
    "랍스터 크림 스프": {"kcal": 450, "carbohydrate": 20, "protein": 25, "fat": 30},
    "비트 수프": {"kcal": 180, "carbohydrate": 35, "protein": 5, "fat": 3},
    "전복죽": {"kcal": 400, "carbohydrate": 50, "protein": 15, "fat": 10},
    "계란말이": {"kcal": 250, "carbohydrate": 5, "protein": 15, "fat": 20},
    "계란찜": {"kcal": 150, "carbohydrate": 2, "protein": 10, "fat": 12},
    "고구마전": {"kcal": 300, "carbohydrate": 60, "protein": 5, "fat": 5},
    "깻잎전": {"kcal": 200, "carbohydrate": 20, "protein": 5, "fat": 10},
    "감자전": {"kcal": 250, "carbohydrate": 50, "protein": 5, "fat": 5},
    "부추전": {"kcal": 220, "carbohydrate": 40, "protein": 5, "fat": 5},
    "굴전": {"kcal": 180, "carbohydrate": 15, "protein": 12, "fat": 7},
    "체다 치즈 튀김": {"kcal": 400, "carbohydrate": 30, "protein": 10, "fat": 25},
    "체다 치즈 칩": {"kcal": 500, "carbohydrate": 45, "protein": 7, "fat": 30},
    "허니 버터 칩": {"kcal": 550, "carbohydrate": 50, "protein": 5, "fat": 35},
    "체다 감자 크림": {"kcal": 350, "carbohydrate": 40, "protein": 6, "fat": 20},
    "베이컨 감자 샐러드": {"kcal": 300, "carbohydrate": 25, "protein": 10, "fat": 15},
    "구운 감자 샐러드": {"kcal": 250, "carbohydrate": 30, "protein": 5, "fat": 10},
    "한치물회": {"kcal": 150, "carbohydrate": 10, "protein": 25, "fat": 3},
    "레몬 버터 새우": {"kcal": 250, "carbohydrate": 5, "protein": 20, "fat": 18},
    "불고기덮밥": {"kcal": 575, "carbohydrate": 65, "protein": 30, "fat": 20},
    "홍합찜": {"kcal": 180, "carbohydrate": 6, "protein": 25, "fat": 7},
    "광어 사시미": {"kcal": 120, "carbohydrate": 0, "protein": 25, "fat": 3},
    "로제쉬림프": {"kcal": 400, "carbohydrate": 20, "protein": 25, "fat": 25},
    "연어 사시미": {"kcal": 200, "carbohydrate": 0, "protein": 30, "fat": 10},
    "참치 사시미": {"kcal": 220, "carbohydrate": 0, "protein": 30, "fat": 12},
    "장어정식": {"kcal": 600, "carbohydrate": 80, "protein": 35, "fat": 15},
    "크림통새우": {"kcal": 450, "carbohydrate": 20, "protein": 25, "fat": 30},
    "고추장찌개": {"kcal": 280, "carbohydrate": 15, "protein": 18, "fat": 12},
    "미소 된장국": {"kcal": 50, "carbohydrate": 5, "protein": 5, "fat": 1},
    "곱창전골": {"kcal": 600, "carbohydrate": 20, "protein": 35, "fat": 40},
    "바질페스토 파스타": {"kcal": 650, "carbohydrate": 75, "protein": 15, "fat": 25},
    "새우튀김": {"kcal": 350, "carbohydrate": 30, "protein": 15, "fat": 20},
    "바지락 칼국수": {"kcal": 450, "carbohydrate": 70, "protein": 15, "fat": 10},
    "푸실리 파스타": {"kcal": 600, "carbohydrate": 85, "protein": 15, "fat": 20},
    "떡볶이": {"kcal": 400, "carbohydrate": 80, "protein": 8, "fat": 8},
    "물막국수": {"kcal": 400, "carbohydrate": 70, "protein": 12, "fat": 5},
    "새우 스캄피 파스타": {"kcal": 650, "carbohydrate": 85, "protein": 20, "fat": 25},
    "탄탄멘": {"kcal": 650, "carbohydrate": 80, "protein": 25, "fat": 30},
    "바질페스토 라비올리": {"kcal": 650, "carbohydrate": 85, "protein": 20, "fat": 25},
    "크림치즈 파스타": {"kcal": 750, "carbohydrate": 85, "protein": 20, "fat": 35},
    "치킨 크림파스타": {"kcal": 700, "carbohydrate": 90, "protein": 25, "fat": 30},
    "닭칼국수": {"kcal": 450, "carbohydrate": 65, "protein": 15, "fat": 10},
    "콩국수": {"kcal": 400, "carbohydrate": 60, "protein": 10, "fat": 10},
    "버팔로 치킨 샌드위치": {"kcal": 500, "carbohydrate": 50, "protein": 25, "fat": 20},
    "갈릭 토스트": {"kcal": 400, "carbohydrate": 50, "protein": 8, "fat": 15},
    "연어 샌드위치": {"kcal": 450, "carbohydrate": 50, "protein": 20, "fat": 15},
    "그릴드 치즈 샌드위치": {"kcal": 450, "carbohydrate": 40, "protein": 20, "fat": 20},
    "치즈 퀘사디아": {"kcal": 550, "carbohydrate": 65, "protein": 20, "fat": 30},
    "참치 카나페": {"kcal": 200, "carbohydrate": 20, "protein": 10, "fat": 10},
    "피자 토스트": {"kcal": 400, "carbohydrate": 50, "protein": 10, "fat": 15},
    "미니 햄버거": {"kcal": 350, "carbohydrate": 35, "protein": 15, "fat": 15},
    "토마토 브루스케타": {"kcal": 200, "carbohydrate": 30, "protein": 5, "fat": 5},
    "시저 치킨랩": {"kcal": 450, "carbohydrate": 50, "protein": 25, "fat": 15},
    "살몬 아보카도 샐러드": {"kcal": 350, "carbohydrate": 10, "protein": 25, "fat": 20},
    "새우 토스트": {"kcal": 350, "carbohydrate": 30, "protein": 15, "fat": 18},
    "오이 샐러드": {"kcal": 50, "carbohydrate": 10, "protein": 1, "fat": 1},
    "매운탕": {"kcal": 300, "carbohydrate": 20, "protein": 25, "fat": 15},
    "미역국": {"kcal": 50, "carbohydrate": 7, "protein": 3, "fat": 2},
    "순대국": {"kcal": 400, "carbohydrate": 25, "protein": 30, "fat": 25},
    "순대국밥": {"kcal": 450, "carbohydrate": 30, "protein": 35, "fat": 20},
    "홍합탕": {"kcal": 150, "carbohydrate": 10, "protein": 20, "fat": 5},
    "계란국": {"kcal": 80, "carbohydrate": 5, "protein": 5, "fat": 4},
    "무국": {"kcal": 50, "carbohydrate": 10, "protein": 2, "fat": 0},
    "낙지국": {"kcal": 120, "carbohydrate": 15, "protein": 15, "fat": 3},
    "해물순두부찌개": {"kcal": 250, "carbohydrate": 20, "protein": 15, "fat": 12},
    "만두국": {"kcal": 220, "carbohydrate": 30, "protein": 12, "fat": 7},
    "순두부국": {"kcal": 150, "carbohydrate": 12, "protein": 10, "fat": 5},
    "시래기된장국": {"kcal": 90, "carbohydrate": 12, "protein": 5, "fat": 3},
    "황태찌개": {"kcal": 200, "carbohydrate": 12, "protein": 18, "fat": 6},
    "짜장면": {"kcal": 600, "carbohydrate": 80, "protein": 15, "fat": 20},
    "불닭볶음면": {"kcal": 600, "carbohydrate": 85, "protein": 20, "fat": 25},
    "물냉면": {"kcal": 400, "carbohydrate": 90, "protein": 10, "fat": 5},
    "비빔국수": {"kcal": 450, "carbohydrate": 80, "protein": 12, "fat": 10},
    "샌드위치": {"kcal": 300, "carbohydrate": 40, "protein": 15, "fat": 10},
    "쉬림프 타코": {"kcal": 400, "carbohydrate": 50, "protein": 20, "fat": 15},
    "불고기 타코": {"kcal": 450, "carbohydrate": 55, "protein": 25, "fat": 20},
    "파스타": {"kcal": 500, "carbohydrate": 75, "protein": 15, "fat": 20},
    "브리또": {"kcal": 600, "carbohydrate": 70, "protein": 25, "fat": 25},
    "라자냐": {"kcal": 700, "carbohydrate": 80, "protein": 20, "fat": 35},
    "크림치즈 베이글": {"kcal": 450, "carbohydrate": 50, "protein": 10, "fat": 20},
    "햄 치즈 토스트": {"kcal": 400, "carbohydrate": 45, "protein": 20, "fat": 15},
    "샐러드롤": {"kcal": 300, "carbohydrate": 35, "protein": 8, "fat": 10},
    "시저 샐러드": {"kcal": 200, "carbohydrate": 10, "protein": 6, "fat": 15},
    "두부조림": {"kcal": 150, "carbohydrate": 10, "protein": 12, "fat": 5},
    "로메인 샐러드": {"kcal": 20, "carbohydrate": 4, "protein": 1, "fat": 0},
    "두부김치": {"kcal": 150, "carbohydrate": 10, "protein": 12, "fat": 8},
    "포테이토 샐러드": {"kcal": 200, "carbohydrate": 30, "protein": 3, "fat": 10},
    "양고기 스테이크": {"kcal": 300, "carbohydrate": 0, "protein": 25, "fat": 20},
    "오리 로스트": {"kcal": 350, "carbohydrate": 0, "protein": 30, "fat": 25},
    "닭가슴살 스테이크": {"kcal": 250, "carbohydrate": 0, "protein": 40, "fat": 8},
    "버팔로윙": {"kcal": 200, "carbohydrate": 5, "protein": 15, "fat": 12},
    "불고기": {"kcal": 400, "carbohydrate": 20, "protein": 30, "fat": 20},
    "삼겹살": {"kcal": 600, "carbohydrate": 0, "protein": 20, "fat": 50},
    "갈비찜": {"kcal": 500, "carbohydrate": 15, "protein": 35, "fat": 30},
    "보쌈": {"kcal": 550, "carbohydrate": 10, "protein": 40, "fat": 35},
    "마파두부": {"kcal": 300, "carbohydrate": 20, "protein": 20, "fat": 15},
    "탕수육": {"kcal": 450, "carbohydrate": 50, "protein": 20, "fat": 20},
    "유린기": {"kcal": 400, "carbohydrate": 30, "protein": 25, "fat": 15},
    "군만두": {"kcal": 300, "carbohydrate": 40, "protein": 10, "fat": 15},
    "깐풍기": {"kcal": 500, "carbohydrate": 40, "protein": 30, "fat": 25},
    "동파육": {"kcal": 600, "carbohydrate": 30, "protein": 40, "fat": 35},
    "가라아게": {"kcal": 300, "carbohydrate": 15, "protein": 20, "fat": 20},
    "깐쇼새우": {"kcal": 400, "carbohydrate": 30, "protein": 25, "fat": 15},
    "돼지갈비": {"kcal": 500, "carbohydrate": 15, "protein": 35, "fat": 30},
    "닭볶음탕": {"kcal": 450, "carbohydrate": 25, "protein": 30, "fat": 20},
    "안동찜닭": {"kcal": 400, "carbohydrate": 35, "protein": 25, "fat": 10},
    "고추기름 닭고기": {"kcal": 500, "carbohydrate": 20, "protein": 35, "fat": 30},
    "닭가슴살 샐러드": {"kcal": 200, "carbohydrate": 10, "protein": 25, "fat": 5},
    "바베큐 폭립": {"kcal": 600, "carbohydrate": 30, "protein": 45, "fat": 35},
    "레몬 치킨": {"kcal": 350, "carbohydrate": 5, "protein": 35, "fat": 15},
    "바베큐 치킨": {"kcal": 400, "carbohydrate": 15, "protein": 35, "fat": 15},
    "치킨 파마산": {"kcal": 350, "carbohydrate": 20, "protein": 40, "fat": 15},
    "닭가슴살 튀김": {"kcal": 280, "carbohydrate": 10, "protein": 35, "fat": 12},
    "오렌지 치킨": {"kcal": 400, "carbohydrate": 30, "protein": 25, "fat": 20},
    "돼지고기묵은지찜": {"kcal": 300, "carbohydrate": 15, "protein": 20, "fat": 12},
    "연어 타르타르": {"kcal": 220, "carbohydrate": 0, "protein": 25, "fat": 12},
    "산적": {"kcal": 250, "carbohydrate": 5, "protein": 30, "fat": 10},
    "타이 새우 볶음": {"kcal": 280, "carbohydrate": 25, "protein": 20, "fat": 12},
    "소이 글레이즈드 연어": {"kcal": 350, "carbohydrate": 20, "protein": 30, "fat": 15},
    "치킨 카레": {"kcal": 500, "carbohydrate": 40, "protein": 35, "fat": 20},
    "매운돼지갈비": {"kcal": 450, "carbohydrate": 10, "protein": 35, "fat": 25},
    "냉채족발": {"kcal": 300, "carbohydrate": 5, "protein": 25, "fat": 15},
    "후라이드 치킨": {"kcal": 600, "carbohydrate": 30, "protein": 35, "fat": 35},
    "치즈계란말이": {"kcal": 250, "carbohydrate": 5, "protein": 15, "fat": 20},
    "소곱창": {"kcal": 350, "carbohydrate": 0, "protein": 25, "fat": 30},
    "소갈비찜": {"kcal": 500, "carbohydrate": 15, "protein": 40, "fat": 25},
    "라임 치킨": {"kcal": 350, "carbohydrate": 5, "protein": 35, "fat": 15},
    "떡갈비": {"kcal": 450, "carbohydrate": 20, "protein": 25, "fat": 30},
    "찜닭": {"kcal": 500, "carbohydrate": 35, "protein": 40, "fat": 15},
    "소불고기": {"kcal": 450, "carbohydrate": 20, "protein": 35, "fat": 25},
    "백숙": {"kcal": 300, "carbohydrate": 5, "protein": 40, "fat": 10},
    "사천식 양꼬치": {"kcal": 400, "carbohydrate": 5, "protein": 35, "fat": 25},
    "돼지갈비 스튜": {"kcal": 500, "carbohydrate": 25, "protein": 30, "fat": 20},
    "소시지 그라탱": {"kcal": 450, "carbohydrate": 25, "protein": 20, "fat": 30},
    "돼지고기볶음": {"kcal": 300, "carbohydrate": 10, "protein": 25, "fat": 15},
    "항정살": {"kcal": 400, "carbohydrate": 0, "protein": 25, "fat": 35},
    "파삼겹": {"kcal": 550, "carbohydrate": 5, "protein": 30, "fat": 45},
    "초벌 막창": {"kcal": 450, "carbohydrate": 5, "protein": 30, "fat": 35},
    "로스카츠": {"kcal": 550, "carbohydrate": 20, "protein": 30, "fat": 30},
    "치즈카츠": {"kcal": 600, "carbohydrate": 25, "protein": 35, "fat": 35},
    "고구마치즈카츠": {"kcal": 650, "carbohydrate": 30, "protein": 30, "fat": 40},
    "닭튀김": {"kcal": 500, "carbohydrate": 20, "protein": 35, "fat": 25},
    "크로켓": {"kcal": 300, "carbohydrate": 35, "protein": 10, "fat": 15},
    "치즈 감자튀김": {"kcal": 400, "carbohydrate": 40, "protein": 10, "fat": 25},
    "할라피뇨 팝퍼": {"kcal": 300, "carbohydrate": 30, "protein": 10, "fat": 15},
    "감자튀김": {"kcal": 350, "carbohydrate": 50, "protein": 5, "fat": 15},
    "감자그라탕": {"kcal": 350, "carbohydrate": 25, "protein": 10, "fat": 25},
    "낙지볶음": {"kcal": 200, "carbohydrate": 10, "protein": 30, "fat": 5},
    "새우구이": {"kcal": 150, "carbohydrate": 0, "protein": 20, "fat": 8},
    "해물찜": {"kcal": 350, "carbohydrate": 20, "protein": 30, "fat": 10},
    "갈치조림": {"kcal": 250, "carbohydrate": 10, "protein": 20, "fat": 15},
    "낙지전골": {"kcal": 300, "carbohydrate": 20, "protein": 25, "fat": 10},
    "게장": {"kcal": 200, "carbohydrate": 10, "protein": 20, "fat": 5},
    "꽁치조림": {"kcal": 350, "carbohydrate": 10, "protein": 30, "fat": 15},
    "장어구이": {"kcal": 400, "carbohydrate": 5, "protein": 35, "fat": 25},
    "조기구이": {"kcal": 300, "carbohydrate": 0, "protein": 35, "fat": 15},
    "감바스 알 아히요": {"kcal": 400, "carbohydrate": 5, "protein": 25, "fat": 30},
    "어묵볶음": {"kcal": 200, "carbohydrate": 15, "protein": 10, "fat": 10},
    "그릴드 연어": {"kcal": 350, "carbohydrate": 5, "protein": 40, "fat": 20},
    "삼치구이": {"kcal": 300, "carbohydrate": 0, "protein": 35, "fat": 15},
    "조개찜": {"kcal": 150, "carbohydrate": 5, "protein": 20, "fat": 3},
    "명태구이": {"kcal": 200, "carbohydrate": 0, "protein": 25, "fat": 5}
}

# 무작위로 선택할 음식 이름 목록
meal_names = list(nutrient_data.keys())

# meal 테이블에 삽입할 SQL 구문을 생성하는 함수
def generate_meal_inserts(start_date, num_days):
    with open("db/meal_inserts.sql", "w", encoding="utf-8") as file:
        for i in range(num_days):
            meal_date = start_date + timedelta(days=i)
            breakfast = random.choice(meal_names)
            lunch = random.choice(meal_names)
            dinner = random.choice(meal_names)
            sql = (
                f"INSERT INTO meal (id, breakfast, lunch, dinner, meal_date) "
                f"VALUES ({i + 1}, '{breakfast}', '{lunch}', '{dinner}', '{meal_date.strftime('%Y-%m-%d')}');\n"
            )
            file.write(sql)

# 예시 실행
start_date = datetime.strptime("2024-01-01", "%Y-%m-%d")
generate_meal_inserts(start_date, 365)
print("SQL 파일이 meal_inserts.sql로 생성되었습니다.")
