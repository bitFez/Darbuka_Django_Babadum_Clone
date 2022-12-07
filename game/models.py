from django.db import models

# Create your models here.
class League(models.Model):
    language = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    questionCount = models.PositiveBigIntegerField(default=0)
    
    def __str__(self):
        return self.language
    
    def increase_q_count(self):
        self.questionCount +=1
        return self.questionCount
    

class Word(models.Model):
    language = models.ForeignKey(League, on_delete=models.CASCADE)
    word = models.CharField(max_length=200)
    code = models.CharField(max_length=10)
    image = models.CharField(max_length=200)
    correctAnswerCount = models.PositiveBigIntegerField(default=0)
    incorrectAnswerCount = models.PositiveBigIntegerField(default=0)

    def __str__(self):
        return self.word
    
    def correctCount(self):
        self.correctAnswerCount +=1

    def incorrectCount(self):
        self.incorrectAnswerCount +=1   