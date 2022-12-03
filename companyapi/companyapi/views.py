from django.http import JsonResponse


def home_page(request):
    print('Home Page Requested')
    friends = ['Ankit', 'Ravi', 'Uttam']
    return JsonResponse(friends, safe=False)
