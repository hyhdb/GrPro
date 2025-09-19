# scripts/006_facility_kw_rel.py

import os
import sys
import django

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myproject.settings")
django.setup()

from mychat.models import Facility, FacilityKeywordRelation

# -------------------------------
# mychat/006_facility_kw_rel.py
# -------------------------------
print("\n" + "-" * 40)
print("# mychat/006_facility_kw_rel.py")
print("-" * 40 + "\n")

facility_kw_map = {
    "공부": [
        "스터디룸", "리라", "리딩라운지", "열람실", "혁신융합파크",
        "그룹 스터디룸", "자료실", "CLP", "오름교육 라운지",
        "자유공부공간"           #추가
    ],
    "휴게": [
        "학생휴게실", "라운지(센터)", "자하마루",
        "휴식공간(1F)", "휴식공간(5F)",
        "여학생 휴게실"           #추가
    ],
    "식사": [
        "편의점", "학생식당", "애니이츠월드"
    ],
    "편의": [
        "편의점"
    ],
    "음악": [
        "레슨실",
        "음악대학 공간"           #추가
    ],
    "카페": [
        "블루포트", "카페드림", "무인 카페"
    ],
    "프린터": [
        "유료 프린터기"
    ],
    "현금": [
        "ATM", "atm", "ATM기", "atm기", "Atm기",
        "국민은행 ATM기", "우리은행 ATM기"
    ],
    "주차": [
        "주차장(1F 외부)", "주차장", "주차장 연결 입구"   #추가
    ],
    "행정": [
        "학생입학처", "자유전공학부지원센터(N101)", "교직지원센터",
        "취업/진로지원팀", "보건건강관리센터", "교육미디어혁신센터",
        "총무인사팀", "재무회계팀", "국제관계센터", "학사운영팀",
        "대학원교학팀"   #행정 관련 부서들 묶음
    ],
    "문화": [
        "소강당", "밀레홀", "상명아트센터", "야외 무대"   #행사/공연 관련
    ],
    "체육": [
        "운동장", "무용연습실"   #체육 활동 관련
    ],
    "상징": [
        "사슴상"   #학교 상징물
    ]
}

# ✅ 기존 FacilityKeywordRelation 데이터 모두 삭제
deleted_count, _ = FacilityKeywordRelation.objects.all().delete()
print(f"🗑 기존 FacilityKeywordRelation {deleted_count}개 삭제 완료")

created_count = 0
keyword_created_map = {}

for keyword, facility_names in facility_kw_map.items():
    for name in facility_names:
        facility_qs = Facility.objects.filter(name=name)
        if facility_qs.exists():
            facility = facility_qs.first()
            FacilityKeywordRelation.objects.create(
                keyword=keyword,
                facility=facility
            )
            created_count += 1
            keyword_created_map[keyword] = keyword_created_map.get(keyword, 0) + 1
        else:
            print(f"❌ 시설 '{name}'이 존재하지 않아요.")

# ✅ 요약 출력
print("\n📊 키워드별 Facility 매핑 결과")
for kw, count in keyword_created_map.items():
    print(f" - '{kw}': {count} 개 연결")

print(f"\n총 FacilityKeywordRelation 등록 개수: {created_count}")