from django.contrib import admin
from .models import GPTSession, GPTMessage
from .models import CampusBuilding, SemanticKeyword, IntentKeyword, CampusBuildingKeywordRelation, Facility, FacilityKeywordRelation

admin.site.register(GPTSession)
admin.site.register(GPTMessage)
admin.site.register(CampusBuilding)
admin.site.register(SemanticKeyword)
admin.site.register(IntentKeyword)
admin.site.register(CampusBuildingKeywordRelation)
admin.site.register(Facility)
admin.site.register(FacilityKeywordRelation)
