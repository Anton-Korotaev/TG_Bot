from telebot import TeleBot, types

bot = TeleBot(token='вставь токен', parse_mode='html')

DEFINITOINS = {
 'тестирование': 'Процесс оценки системы или её компонентов с целью проверки их соответствия заданным требованиям.',
 'тест-план': 'Документ, описывающий объем тестирования, подходы, ресурсы и график, необходимые для выполнения тестирования проекта.',
 'тест-дизайн': 'Процесс создания тест-кейсов, покрывающих самые важные узлы работы программы. Множество техник — например, классы эквивалентности, граничные значения, попарное тестирование, таблица принятия решений и другие.',
 'тест-кейс': 'Набор условий или переменных, по которым проводится тестирование программного обеспечения для проверки соответствия требованиям.',
 'баг': 'Ошибка или дефект в программном обеспечении, который приводит к некорректной работе или результатам.',
 'регрес': 'Повторное тестирование программного обеспечения для проверки того, что изменения или исправления не внесли новых ошибок в уже работающий функционал.',
 'смоук': 'Набор тестов, выполняемых для проверки основных функций программного обеспечения перед более детальным тестированием.',
 'функциональное тестирование': 'Тестирование функциональности программного обеспечения для проверки, что оно работает в соответствии с требованиями.',
 'нагрузочное тестирование': 'Тестирование системы под ожидаемой нагрузкой для оценки её производительности и поведения.',
 'стресс-тестирование': 'Тестирование системы под экстремальными условиями или нагрузками, чтобы определить её пределы и устойчивость.',
 'юнит-тестирование': 'Тестирование отдельных модулей или компонентов программного обеспечения для проверки их правильной работы.',
 'интеграционное тестирование': 'Тестирование комбинации модулей или компонентов, чтобы убедиться, что они правильно взаимодействуют друг с другом.',
 'приемочное тестирование': 'Тестирование системы на соответствие требованиям пользователя и готовность к эксплуатации.',
 'api': 'Тестирование интерфейсов программирования приложений (API) для проверки взаимодействия между различными компонентами программного обеспечения.',
 'автоматизация тестирования': 'Использование специальных программ и инструментов для автоматизации процесса тестирования.',
 'тестовые данные': 'Набор данных, используемых для проведения тестов.',
 'кросс-браузерное тестирование': 'Тестирование веб-приложений в разных браузерах для обеспечения их корректной работы.',
 'отчет о тестировании': 'Документ, содержащий результаты проведенного тестирования, выявленные баги и рекомендации.',
 'тестовое окружение': 'Аппаратное и программное окружение, в котором выполняется тестирование.',
 'ci': 'Практика непрерывной интеграции, где разработчики регулярно интегрируют свои изменения в общую ветку разработки, после чего выполняется автоматическое тестирование.',
 'cd': 'Практика непрерывного развертывания, при которой изменения, прошедшие тестирование, автоматически внедряются в рабочую среду.',
 'qa': 'Обеспечение качества, набор действий для гарантии соответствия продукта или услуги установленным требованиям.',
 'qc': 'Контроль качества, действия по проверке и контролю продуктов и услуг для обеспечения их соответствия требованиям.',
 'test suite': 'Набор тестов, предназначенный для тестирования программного обеспечения в различных аспектах.',
 'http-запрос': ' HTTP Request Запрос от клиента (обычно браузера) к серверу, состоящий из строки запроса, заголовков и (в некоторых случаях) тела запроса.',
 'http-ответ': ' HTTP Response Ответ сервера на запрос клиента, включающий статусный код, заголовки и тело ответа.',
 'архитектура rest': 'Стиль архитектуры для разработки веб-сервисов, использующий HTTP методы (GET, POST, PUT, DELETE) и принципы ресурсо-ориентированного дизайна.',
 'soap': 'Протокол обмена структурированными сообщениями в рамках сети, часто использующий XML.',
 'devtools': 'Набор инструментов в браузерах (например, Chrome DevTools), используемых для разработки, отладки и анализа веб-приложений.',
 'api': 'Интерфейс для взаимодействия между различными программами, определяющий способы их взаимодействия.',
 'postman': 'Инструмент для тестирования API, позволяющий отправлять HTTP-запросы, проверять ответы и автоматизировать тестирование.',
 'виды тестирования': 'Различные виды тестирования, такие как функциональное, регрессионное, нагрузочное, стресс-тестирование и другие.',
 'техники тест-дизайна': 'Методы создания тест-кейсов, включая эквивалентное разбиение, анализ граничных значений, причинно-следственный граф и т.д.',
 'тест-кейс': 'Набор условий или действий, разработанных для проверки конкретной функциональности программного обеспечения.',
 'багрепорт': 'Документ, описывающий обнаруженный дефект или баг в программном обеспечении, включающий шаги для его воспроизведения, ожидаемый и фактический результаты.',
 'tms': 'Система управления тестированием, используемая для планирования, выполнения и отслеживания тестирования и тест-кейсов.',
 'чек-лист': 'Список проверок или задач, используемый для выполнения тестирования.',
 'html': ' HyperText Markup Language Язык разметки для создания веб-страниц.',
 'css': 'Язык стилей, используемый для описания внешнего вида веб-страниц.',
 'javascript': 'Язык программирования, используемый для создания динамичного и интерактивного контента на веб-страницах.',
 'charles': 'Проксирование HTTP/HTTPS-трафика, инструмент для перехвата и анализа сетевых запросов и ответов.',
 'терминал': 'Интерфейс командной строки, используемый для выполнения текстовых команд в операционной системе.',
 'git': 'Система контроля версий, используемая для отслеживания изменений в исходном коде и управления разработкой программного обеспечения.',
 'sql': 'Язык программирования для управления и запросов к базам данных.',
 'agile': 'Методология разработки программного обеспечения, основанная на итеративном подходе, тесном взаимодействии с пользователями и гибком реагировании на изменения.',
 'цикл разработки': 'Полный процесс создания программного обеспечения, от анализа требований и проектирования до реализации, тестирования, развертывания и сопровождения.',
}
@bot.message_handler(commands=['start'])
def start_command_handler(message: types.Message):
	bot.send_message(
		chat_id=message.chat.id,
		text='Привет! Это краткий словарь терминов для тестировщика 😎\nВведи термин и узнай его значение'
	)
@bot.message_handler()
def message_handler(message: types.Message):
	definition = DEFINITOINS.get(
		message.text.lower()
		)
	if definition is None:
		bot.send_message(
			chat_id=message.chat.id,
			text='🤔 хз'
	)
		return
	bot.send_message(
		chat_id=message.chat.id,
		text=f'Определение:\n<code>{definition}</code>',
	)
def main():
	bot.infinity_polling()

if __name__ == '__main__':
	main()
