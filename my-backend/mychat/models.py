from django.db import models

# -------------------------------
# 🔹 GPT 대화 관련 모델 (추가)
# -------------------------------

class GPTSession(models.Model):
    user_uid = models.CharField(max_length=128)
    session_id = models.CharField(max_length=128)
    title = models.CharField(max_length=128)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} - {self.user_uid}"

class GPTMessage(models.Model):
    session = models.ForeignKey(GPTSession, on_delete=models.CASCADE)
    role = models.CharField(max_length=10)  # 'user' or 'assistant'
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"[{self.role}] {self.message[:20]}..."

# -------------------------------
# 🔹 기존 캠퍼스 정보 관련 모델
# -------------------------------

# 건물 키워드
class CampusBuilding(models.Model):
    name = models.CharField(max_length=100)        # 예: 제1공학관
    alias = models.CharField(max_length=100)        # 예: G관
    description = models.TextField(blank=True)     # 지리적 설명 등

    def __str__(self):
        return f"{self.alias} ({self.name})"


# 의미 키워드 (의도 파악용)
class SemanticKeyword(models.Model):
    keyword = models.CharField(max_length=50)       # 예: 공부
    alias = models.CharField(max_length=100)         # 예: 시험, 프로젝트, 레포트
    category = models.CharField(max_length=50)      # 예: 학업, 학습 관련

    def __str__(self):
        return f"{self.keyword} ({self.category})"

# 행동 키워드 (질문 의도 유추)
class IntentKeyword(models.Model):
    phrase = models.CharField(max_length=100)      # 예: 가고 싶다, 알고 싶다
    intent_type = models.CharField(max_length=50)  # 예: 이동, 탐색 등

    def __str__(self):
        return f"{self.phrase} ({self.intent_type})"
    
class CampusBuildingKeywordRelation(models.Model):
    building = models.ForeignKey(CampusBuilding, on_delete=models.CASCADE)
    keyword = models.CharField(max_length=50)  # 예: ATM, 동아리방, 인출기 등

    def __str__(self):
        return f"{self.keyword} → {self.building.name}"
    
    
class Facility(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50)  # 예: 식당, 휴게공간, 스터디룸
    description = models.TextField(blank=True)
    building = models.ForeignKey(CampusBuilding, on_delete=models.CASCADE, related_name='facilities')

    def __str__(self):
        return f"{self.building.alias} - {self.name} ({self.category})"

class FacilityKeywordRelation(models.Model):
    keyword = models.CharField(max_length=50)  # SemanticKeyword.keyword와 대응
    facility = models.ForeignKey(Facility, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.keyword} ↔ {self.facility.name}"