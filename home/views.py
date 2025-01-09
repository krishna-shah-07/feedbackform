from django.shortcuts import render, redirect

# Create your views here.
from .models import *

def index(request):
    feedbacks = CustomerFeedback.objects.all()
    return render(request, 'surveys.html', {'feedbacks': feedbacks})

def customerfeedback(request, feedback_id):
    feedback = CustomerFeedback.objects.get(id=feedback_id)
    questions = feedback.question.all()
    if request.method == 'POST':
        for question in questions:
            response_text = request.POST.get(f"response-{question.id}")
            selected_option_ids = request.POST.getlist(f"options-{question.id}")
            response = CustomerResponse.objects.create(
                customer=feedback,
                question=question,
                response=response_text if question.question_type in ['text', 'bigtext'] else None,
            )
            if selected_option_ids:
                selected_options = Option.objects.filter(id__in=selected_option_ids)
                response.selected_option.set(selected_options)
        return redirect('/thankyou/')

    return render(request, 'survey.html', {'questions': questions})

def thankyou(request):
    return render(request, 'thankyou.html')