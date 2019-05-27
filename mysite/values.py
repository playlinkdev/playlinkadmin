
class Values():
    bomb_command_location = "주변에 붙어있는 노란색 폭탄해제 지령카드를 찾아보세요."
    mugunghwa_command_location = "음악이 나올 때만 이동해서 뒤편에 설치되어 있는 녹색 미션완료 카드를 태그해보세요."

    quizs = [
        {'quiz_no':'1', 'quiz':'우리나라 최초 한글소설은 허균이 쓴 홍길동전 입니다. 그러면 우리나라 최초 한문 소설은 무엇일까요?​','answer': '금요신화', 'answer_w1': '한중록', 'answer_w2': '사시남정기'},
        {'quiz_no':'2','quiz':'다음 중 시침과 분침이 일직선이 되는 시간은 무엇일까요?​', 'answer': '06:00','answer_w1':  '03:45', 'answer_w2':'12:30'},
        {'quiz_no':'3','quiz':'공기 중 가장 많은 비중을 차지하고 있는 기체는?​', 'answer': '질소', 'answer_w1': '산소', 'answer_w2':'이상화탄소'},
        {'quiz_no':'4','quiz':'1부터 100사이에 9라는 숫자는 모두 몇개일까요?​', 'answer': '20', 'answer_w1': '18', 'answer_w2':'19'},
        {'quiz_no':'5','quiz':'다음중 한글 맞춤법이 틀린 단어는?​', 'answer': '암돼지', 'answer_w1': '칠흑', 'answer_w2': '해님'},
        {'quiz_no':'6','quiz':'다음중 진짜 새의 이름은 무엇일까요?​','answer':  '참새', 'answer_w1': '까마귀', 'answer_w2':'황조롱이'},
        {'quiz_no':'7','quiz':'세상에서 가장 쉬운 숫자는?​​', 'answer': '190,000', 'answer_w1': '1', 'answer_w2':'333'},
    ]

    words = ['고릴라', '냉장고', '선생님', '창의력', '화장실', '휴대폰', '중학교']

    @property
    def get_words(self):
        return '|'.join([w for w in self.words])

    @property
    def cal_no(counter):
        return counter + 2
