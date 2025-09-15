@echo off
REM Move to Backend Root Directory
cd /d %~dp0my-backend

echo [1] Activate: Virtual Env
call .\venv\Scripts\activate.bat

echo [2] Apply Migrations
python manage.py makemigrations
python manage.py migrate

echo [3] Load Static Data
python manage.py loaddata 001_buildings.json
python manage.py loaddata 002_semantic_keywords.json
python manage.py loaddata 003_intent_keywords.json

echo [4] Insert Dynamic Keyword Relations
python mychat\004_building_kw_rel.py
python mychat\005_facilities.py
python mychat\006_facility_kw_rel.py

echo [5] Run Django Server
python manage.py runserver