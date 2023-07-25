from django import template

register = template.Library()

@register.filter
def get_challenge_answer(challenges, challenge_id):
    for challenge in challenges:
        if challenge['id'] == challenge_id:
            return challenge['solution']
    return ""
