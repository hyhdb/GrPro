# firebase_helper.py
import firebase_admin
from firebase_admin import auth, credentials

# Firebase 초기화 (앱 중복 방지)
if not firebase_admin._apps:
    cred = credentials.Certificate("path/to/your/firebase-adminsdk.json")
    firebase_admin.initialize_app(cred)

def verify_id_token(id_token):
    try:
        print(f"✅ 검증 요청받은 토큰 (앞부분): {id_token[:30]}")
        decoded_token = auth.verify_id_token(id_token)
        print(f"✅ 검증 성공, UID: {decoded_token['uid']}")
        return decoded_token["uid"]
    except Exception as e:
        print(f"❌ Firebase 토큰 검증 실패: {e}")
        return None