def get_answer(question):
	question = str(question).lower()
	answers = {
	'привет': 'И тебе привет',
	'как дела?': 'Лучше всех',
	'пока': 'Увидимся'}
	return answers[question]

#тестовый код для гита

result = get_answer(input('Введите вопрос: '))
print(result)
