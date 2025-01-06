from django.db import models

# Create your models here.

class Question(models.Model):
    Question_choices = (('text', 'text'), ('bigtext' , 'bigtext'), ('radio', 'radio'), ('checkbox', 'checkbox'))
    question = models.CharField(max_length=200)
    question_type = models.CharField(max_length=200, choices=Question_choices, default='text')

    def __str__(self):
        return f"{self.question} - {self.question_type}"
    
class Option(models.Model):
    #related name is used for reverse relation lookup -- here for options of a question we can use question.options
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='options')
    option_name = models.CharField(max_length=200)
    
    def __str__(self):
        return f"{self.question.question} - {self.option}"
    
class CustomerFeedback(models.Model):
    question = models.ManyToManyField(Question)
    
    def __str__(self):
        return f"{self.question.question} - {self.answer}"
    
class CustomerResponse(models.Model):
    customer = models.ForeignKey(CustomerFeedback, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    response = models.TextField(null=True, blank=True)
    selected_option = models.ManyToManyField(Option, blank=True)
    
    def __str__(self):
        return f"{self.customer.name} - {self.feedback}"