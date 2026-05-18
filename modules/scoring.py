def evaluate_answer(answer):
    score = min(10, max(4, len(answer)//40))
    feedback = 'Add measurable business impact and clearer structure.'
    return score, feedback
