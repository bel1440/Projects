from django.shortcuts import render

def resume(request):
    data = {
        'discord': 'Nikita Zoxan#keks1440',
        'mail': 'nik.belyaev2015@gmail.com',
        'adress': 'Gomel, Belarus',
        'education1': {
            'year': '2019-2023',
            'place': 'Belorusian State Polytechnical College'
        },
        'education2': {
            'year': '2025',
            'place': 'IT step school'
        },
        'name': 'Nikita Belyaev',
        'job_title': 'Student',
        'about': {
            'first': 'My name is Nikita, I was born in the city of Gomel, Belarus. I am 21 years old, I studied at school' 
                     '№ 53 until the 7th grade, in the 8th grade I moved to school № 1 due to a move. After 9th grade, '
                     'I entered the Gomel State Polytechnic College and studied there for 4 years, specializing in '
                     '“Equipment Maintenance and Repair.” After college, he served in the army for a year and a half.',
            'second': 'After service, i am got a job at a Gomel chemical plant as a repairman and began training in it step on python-developer'
        },
        'skills': {
            'first': 'Python',
            'second': 'HTML5, CSS3',
            'third': 'English - Elementary (A1+,A2)'
        },
        'strenghts': {
            'first': 'Hardworking',
            'second': 'Responsible',
            'third': 'Sociable',
            'fourth': 'Quick learner',
            'fifth': 'Goal-oriented',
            'sixth': 'Conscientious'
        }
    }
    return render(request, 'main/resume.html', data)
