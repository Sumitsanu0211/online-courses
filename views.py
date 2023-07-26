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
