from django.contrib import admin
from .models import MissionQuiz, Quiz, MatchFinalWordMission, MissionLocation, SecretCode


class QuizsInLine(admin.StackedInline):
    model = Quiz
    extra = 0


class MatchFinalWordMissionInLine(admin.StackedInline):
    model = MatchFinalWordMission
    extra = 0


class MissionQuizAdmin(admin.ModelAdmin):
    inlines = [QuizsInLine, MatchFinalWordMissionInLine]


class MissionLocationInLine(admin.StackedInline):
    model = MissionLocation
    extra = 0


class MissionQuizInLine(admin.StackedInline):
    model = MissionQuiz
    extra = 0


class SecretCodeAdmin(admin.ModelAdmin):
    inlines = [MissionLocationInLine, MissionQuizInLine]



admin.site.register(SecretCode)
admin.site.register(MissionQuiz, MissionQuizAdmin)
admin.site.register(MissionLocation)

# admin.site.register(Quiz)
# admin.site.register(MatchFinalWordMission)

