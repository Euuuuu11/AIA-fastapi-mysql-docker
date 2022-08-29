from icecream import ic
import pandas as pd
import numpy as np
import random
import string

class Quiz(object):
    def __init__(self) -> None:
        pass
    
    '''
    Q1. 다음 결과 출력
        a  b  c
    1  1  3  5
    2  2  4  6
    ic| df1:       a  b  c
                1  1  3  5
                2  2  4  6
    '''
    # 사전으로 DataFrame 생성하는 방법 (from_dict()사용) 
    # df = pd.DataFrame.from_dict({}, orient='index', columns=[])
    def quiz_1(self) :
        df = pd.DataFrame.from_dict(
            {'1' : [ 1,  3,  5],'2' : [2,  4,  6]},
            orient='index',
            columns=['a', 'b', 'c'])
        ic(df)
    '''         
    Q2. 다음 결과 출력
        A   B   C
    1   1   2   3
    2   4   5   6
    3   7   8   9
    4  10  11  12
    ic| df2:     A   B   C
                1   1   2   3
                2   4   5   6
                3   7   8   9
                4  10  11  12
    '''
    # 리스트로 DataFrame 생성하는 방법 (디폴트)
    # df = pd.DataFrame([[],[],[],[]], index=[], columns=[])
    def quiz_2(self) :
        df = pd.DataFrame([[1,2,3],
                        [4,5,6],
                        [7,8,9],
                        [10,11,12]], index=range(1,5), columns=['A','B','C'])
        ic(df)
    '''
    Q3 두자리 정수를 랜덤으로 2행 3열 데이터프레임을 생성
    ic| df3:     0   1   2
                0  95  25  74
                1  44  24  97
    '''
    def quiz_3(self) :    
       df = pd.DataFrame(np.random.randint(10, 100, size=(2,3)))
       ic(df) 
    ''' 
    Q4 국어, 영어, 수학, 사회 4과목을 시험치른 10명의 학생들의 성적표 작성. 단 점수 0 ~ 100이고 학생은 랜덤 알파벳 5자리 ID 로 표기
    ic| self.id(): 'HKKHc'
    ic| self.score(): 22
    ic| df4:        국어  영어  수학  사회
            lDZid  57  90  55  24
            Rnvtg  12  66  43  11
            ljfJt  80  33  89  10
            ZJaje  31  28  37  34
            OnhcI  15  28  89  19
            claDN  69  41  66  74
            LYawb  65  16  13  20
            QDBCw  44  32   8  29
            PZOTP  94  78  79  96
            GOJKU  62  17  75  49
    
    '''
    def id(self):
        return [ "".join([random.choice(string.ascii_letters) 
                          for i in range(5)]) for i in range(10)]
    def score(self):
        return np.random.randint(0,100,(10, 4))
    
    def quiz_4(self) :
        df = pd.DataFrame(
            self.score(), 
            index=self.id(), 
            columns=['국어', '영어', '수학', '사회'])
        ic(df) 
        return df
    
    ''' 
    Q5 원하는 과목 점수만 출력하시오. (만약 국어라고 입력하면 아래와 같이 출력됨)
        hVoGW    93
        QkpKK    25
        oDmky    82
        qdTeX    51
        XGzWk    34
        PAwgj    85
        vnTmB    28
        wuxIm    58
        AOQFG    32
        jHChe    59
        Name: 국어, dtype: int64
    
    '''
    def quiz_5(self, subject) :
        scores = self.quiz_4()
        
