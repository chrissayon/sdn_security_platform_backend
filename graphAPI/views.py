import json
from django.http import JsonResponse

# def index(request):
#     return JsonResponse({'data':69})
http_method_names = ['get', 'post', 'put', 'delete', 'head', 'options', 'trace']

def index(request):
    # if request.status == 200:
    #     return 

    response = JsonResponse(
        {"data":69}
    ) 
    
    response["Access-Control-Allow-Origin"] = "*"
    response["Access-Control-Allow-Methods"] = "GET, OPTION"
    response["Access-Control-Max-Age"] = "1000"
    response["Access-Control-Allow-Headers"] = "X-Requested-With, Content-Type, access-control-allow-origin"
    return response