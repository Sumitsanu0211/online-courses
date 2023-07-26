<form action="{% url 'submit_exam' %}" method="post">
    {% csrf_token %}
    {% for question in questions %}
    <fieldset>
        <legend>{{ question.question_text }}</legend>
        {% for choice in question.choice_set.all %}
        <input type="radio" name="choice" value="{{ choice.id }}"> {{ choice.choice_text }}<br>
        {% endfor %}
    </fieldset>
    {% endfor %}
    <input type="submit" value="Submit">
</form>


from django.shortcuts import render, get_object_or_404
from .models import Submission

def evaluate_submission(request, submission_id):
    submission = get_object_or_404(Submission, pk=submission_id)
    
    # Perform evaluation logic here and set the score based on the answers in the submission
    # For example:
    # score = 0
    # for answer in submission.answers.all():
    #     if answer.choice.is_correct:
    #         score += 1
    
    # You can then update the submission model with the calculated score, if needed.
    # For example:
    # submission.score = score
    # submission.save()
    
    # Prepare data to pass to the evaluation_result template
    context = {
        'submission': submission,
        # Include any other data you want to display in the evaluation result template
    }
    
    return render(request, 'evaluation_result.html', context)
