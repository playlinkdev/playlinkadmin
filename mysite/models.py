from django.db import models
from mysite.values import Values
# Create your models here.


class SecretCode(models.Model):

    code = models.CharField('시크릿코드', max_length=10)
    desc = models.CharField('설명', max_length=250)

    def __str__(self):
        return self.desc

    def save(self, *args, **kwargs):
        super(SecretCode, self).save(*args, **kwargs)

        mq = MissionQuiz(secret_code_id=self.id)
        mq.mission_quiz_title = '미션퀴즈제목 : {} 의 미션퀴즈입니다.'.format(self.desc)
        mq.bomb_command_location = Values.bomb_command_location
        mq.mugunghwa_command_location = Values.mugunghwa_command_location
        mq.save()

        ml = MissionLocation(secret_code_id=self.id)
        ml.mission_loc_title = '미션위치제목 : {} 의 미션위치입니다.'.format(self.desc)
        ml.save()

        for quiz in Values.quizs:
            q = Quiz(mission_quiz_id=mq.id)
            q.quiz_no = quiz['quiz_no']
            q.quiz = quiz['quiz']
            q.quiz_answer = quiz['answer']
            q.quiz_wrong_answer1 = quiz['answer_w1']
            q.quiz_wrong_answer2 = quiz['answer_w2']
            q.save()

        for word in Values.words:
            m = MatchFinalWordMission(mission_quiz_id=mq.id)
            m.word = word
            m.save()


class MissionQuiz(models.Model):
    secret_code = models.ForeignKey(SecretCode, on_delete=models.CASCADE)
    mission_quiz_title = models.CharField('미션퀴즈제목', max_length=150, blank=True, null=True, default='')
    bomb_command_location = models.CharField('폭탄해제 지령 위치', max_length=500)          #폭탄해제 지령 위치
    mugunghwa_command_location = models.CharField('무궁화 지령 위치', max_length=500)       #무궁화 지령 위치

    def __str__(self):
        return self.mission_quiz_title

    def save(self, *args, **kwargs):
        super(MissionQuiz, self).save(*args, **kwargs)

    no = 2

    def get_no(self):
        self.no = self.no + 1
        return self.no


class Quiz(models.Model):   #퀴즈는 7개까지 입력가능하도록 한다.
    mission_quiz = models.ForeignKey(MissionQuiz, on_delete=models.CASCADE)

    quiz_no = models.IntegerField('퀴즈번호', null=True)
    quiz = models.CharField('퀴즈질문', max_length=500)
    quiz_answer = models.CharField('퀴즈정답', max_length=100)
    quiz_wrong_answer1 = models.CharField('퀴즈오답1', max_length=100)
    quiz_wrong_answer2 = models.CharField('퀴즈오답2', max_length=100)


class MatchFinalWordMission(models.Model):  #단어는 7개까지 입력가능하도록 한다.
    mission_quiz = models.ForeignKey(MissionQuiz, on_delete=models.CASCADE)
    word = models.CharField('미션단어', max_length=50)


class MissionLocation(models.Model):
    mission_loc_title = models.CharField('미션위치제목', max_length=150, null=True, default='')
    secret_code = models.ForeignKey(SecretCode, on_delete=models.CASCADE)

    loc_mission1_gps_lat = models.CharField(max_length=20, null=True, default="0")
    loc_mission1_gps_lng = models.CharField(max_length=20, null=True, default="0")

    loc_mission2_gps_lat = models.CharField(max_length=20, null=True, default="0")
    loc_mission2_gps_lng = models.CharField(max_length=20, null=True, default="0")

    loc_mission3_gps_lat = models.CharField(max_length=20, null=True, default="0")
    loc_mission3_gps_lng = models.CharField(max_length=20, null=True, default="0")

    loc_mission4_gps_lat = models.CharField(max_length=20, null=True, default="0")
    loc_mission4_gps_lng = models.CharField(max_length=20, null=True, default="0")

    def __str__(self):
        return self.mission_loc_title
