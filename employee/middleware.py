from django.utils.deprecation import MiddlewareMixin
from django.http import HttpResponseBadRequest

class ExperienceSalaryMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if request.path == '/register/' and request.method == 'POST':
            experience = int(request.POST.get('experience'))
            if experience < 1:
                return HttpResponseBadRequest("У вас недостаточно опыта")
            elif experience >=1 and experience < 3:
                request.salary = 1000
            elif experience >=3 and experience < 7:
                request.salary = 2000
            elif experience >=7 and experience <= 10:
                request.salary = 5000
            else:
                return HttpResponseBadRequest('Вы врете')
        elif request.path == '/register/' and request.method == 'GET':
            setattr(request, 'salary', 'Зарплата не определена')