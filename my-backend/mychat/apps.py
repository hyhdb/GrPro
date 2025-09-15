# mychat/apps.py
from django.apps import AppConfig
import os
import firebase_admin
from firebase_admin import credentials

class MychatConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'mychat'

    def ready(self):
        # Firebase가 이미 초기화된 경우 중복 방지
        if not firebase_admin._apps:
            cred_path = os.getenv("FIREBASE_KEY_PATH")
            if cred_path:
                cred = credentials.Certificate(cred_path)
                firebase_admin.initialize_app(cred)
