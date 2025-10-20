from django.http import JsonResponse
def identification(request):
    accepted_types = ("xlsx","json","csv","xls")
    name = request.FILES.get('name')
    if name.endswith(accepted_types):
        file=request.FILES["file"]
        return JsonResponse({"success":True,
                             "name":name,
                             "file":file})
    else:
        return JsonResponse({"success":False,
                             "name":name,
                             "file":None})