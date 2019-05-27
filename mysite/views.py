import logging

from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, get_object_or_404

from django.urls import reverse
from mysite.models import *
from mysite.values import *


logger = logging.getLogger('mylogger')

# Create your views here.


def index(request):

    return render(request, 'mysite/index.html')


def login(request):

    try:
        secrectcode_info = SecretCode.objects.get(code=request.POST['code'])

    except(KeyError, SecretCode.DoesNotExist):

        return render(request, 'mysite/index.html',{
            'error_message': "없는 비밀코드 입니다. 관리자에게 문의해주세요.",
        })
    else:
        request.session['secretcode_code'] = secrectcode_info.code
        return HttpResponseRedirect(reverse('mysite:select', args=(secrectcode_info.pk,)))

def logout(request):
    try:
        del request.session['secretcode_code']
    except KeyError:
        pass
    return render(request, 'mysite/index.html')

def select(request, secretcode_id):
    print(request.session['secretcode_code'])
    if 'secretcode_code' not in request.session:
        return render(request, 'mysite/index.html')

    return render(request, 'mysite/select.html', {
        'secretcode_id': secretcode_id,
        'secretcode_code': request.session['secretcode_code'],
    })


def mission_map(request, secretcode_id):
    if 'secretcode_code' not in request.session:
        return render(request, 'mysite/index.html')

    mp = get_object_or_404(MissionLocation, secret_code_id=secretcode_id)

    if mp.loc_mission1_gps_lat == "0":
        btnStyle1 = "primary"
    else:
        btnStyle1 = "success"

    if mp.loc_mission2_gps_lat == "0":
        btnStyle2 = "primary"
    else:
        btnStyle2 = "success"

    if mp.loc_mission3_gps_lat == "0":
        btnStyle3 = "primary"
    else:
        btnStyle3 = "success"

    if mp.loc_mission4_gps_lat == "0":
        btnStyle4 = "primary"
    else:
        btnStyle4 = "success"

    btnStyle = {'btnStyle1':btnStyle1, 'btnStyle2':btnStyle2, 'btnStyle3':btnStyle3, 'btnStyle4':btnStyle4}

    return render(request, 'mysite/mission_map.html', {'secretcode_id':secretcode_id, 'mission_map':mp, 'btnStyle':btnStyle})



def api_save_mission_map(request, secretcode_id):

    mission_loc = get_object_or_404(MissionLocation, secret_code_id=secretcode_id)

    if request.POST['GPS_N'] == "1":
        mission_loc.loc_mission1_gps_lng = request.POST['GPS_LNG']
        mission_loc.loc_mission1_gps_lat = request.POST['GPS_LAT']
    elif request.POST['GPS_N'] == "2":
        mission_loc.loc_mission2_gps_lng = request.POST['GPS_LNG']
        mission_loc.loc_mission2_gps_lat = request.POST['GPS_LAT']
    elif request.POST['GPS_N'] == "3":
        mission_loc.loc_mission3_gps_lng = request.POST['GPS_LNG']
        mission_loc.loc_mission3_gps_lat = request.POST['GPS_LAT']
    elif request.POST['GPS_N'] == "4":
        mission_loc.loc_mission4_gps_lng = request.POST['GPS_LNG']
        mission_loc.loc_mission4_gps_lat = request.POST['GPS_LAT']

    mission_loc.save()

    return HttpResponse("OK")


def api_reset_mission_map(request, secretcode_id):
    mission_loc = get_object_or_404(MissionLocation, secret_code_id=secretcode_id)

    mission_loc.loc_mission1_gps_lng = "0"
    mission_loc.loc_mission1_gps_lat = "0"
    mission_loc.loc_mission2_gps_lng = "0"
    mission_loc.loc_mission2_gps_lat = "0"
    mission_loc.loc_mission3_gps_lng = "0"
    mission_loc.loc_mission3_gps_lat = "0"
    mission_loc.loc_mission4_gps_lng = "0"
    mission_loc.loc_mission4_gps_lat = "0"

    mission_loc.save()

    return HttpResponse("OK")


def mission_quiz(request, secretcode_id):
    if 'secretcode_code' not in request.session:
        return render(request, 'mysite/index.html')

    mq = get_object_or_404(MissionQuiz, secret_code_id=secretcode_id)
    q = Quiz.objects.filter(mission_quiz_id=mq.id)
    w = MatchFinalWordMission.objects.filter(mission_quiz_id=mq.id)

    return render(request, 'mysite/mission_quiz.html', {'secretcode_id':secretcode_id, 'mission_quiz': mq, 'values': Values})


def api_quiz(request):
    for quiz in Values.quizs:
        if(quiz['quiz_no'] == request.GET['quiz_no']):
            quiz_s = quiz
            break

    return JsonResponse(quiz_s, safe=False)


def api_save_mission(request, secretcode_id):
    mission = get_object_or_404(MissionQuiz, secret_code_id=secretcode_id)

    if request.POST['TYPE'] == "B":
        mission.bomb_command_location = request.POST['bomb_command_location']

    if request.POST['TYPE'] == "M":
        mission.mugunghwa_command_location = request.POST['mugunghwa_command_location']

    mission.save()

    return HttpResponse("OK")


def api_save_quizs(request, secretcode_id):
    mission = get_object_or_404(MissionQuiz, secret_code_id=secretcode_id)
    quiz = mission.quiz_set.get(quiz_no=int(request.POST['quiz_no']))

    quiz.quiz = request.POST['question']
    quiz.quiz_answer = request.POST['answer']
    quiz.quiz_wrong_answer1 = request.POST['quiz-wrong-answer1']
    quiz.quiz_wrong_answer2 = request.POST['quiz-wrong-answer2']

    quiz.save()

    return HttpResponse("OK")


def api_save_words(request, secretcode_id):
    mission = get_object_or_404(MissionQuiz, secret_code_id=secretcode_id)

    for w in str(request.POST["wordlist"])[:-1].split(','):
        pk, w = w.split('|')
        word = mission.matchfinalwordmission_set.get(pk=int(pk))
        word.word = w
        word.save()

    return HttpResponse("OK")


def map_test(request):
    return render(request, 'mysite/map_test.html')