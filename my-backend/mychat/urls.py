from django.urls import path
from .views import CheckDuplicateIDView, ChatWithGptView, GPTSessionListView, DeleteSessionView

urlpatterns = [
    path('', ChatWithGptView.as_view(), name='chat_with_gpt'),
    path('logs/', GPTSessionListView.as_view(), name='chat_logs'),
    path('delete-session/', DeleteSessionView.as_view(), name='delete_session'),
    path("check-duplicate/", CheckDuplicateIDView.as_view(), name="check-duplicate"),
]