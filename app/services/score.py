from app.models.score import Score

class ScoreService(object): 
    def __init__(self) -> None:
        pass
        
        
    def Score2(self, name, korean, english, mathl): 
        score = Score(name, korean, english, mathl)
        print(f'이름 : {score.name}')
        print(f'국어 : {score.korean}')
        print(f'국어 : {score.korean}')
        print(f'수학: {score.math}')
        print(f'영어: {score.english}')
        
               
         