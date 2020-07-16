from django.http import HttpResponse
import json

from app.models import Activity


def testdb(request):
    list = Activity.objects.all()

    # list2 = {}

    list3 = []
    i = 1
    for var in list:
        data = {}
        data['id'] = i
        data['cname'] = var.cname
        data['ctime'] = var.ctime
        data['address'] = var.address
        data['price'] = var.price
        data['photo'] = var.photo
        data['urlLink'] = var.urlLink
        #
        # list2['id'] = i
        # list2['data'] = data

        list3.append(data)
        i += 1

    # a = json.dumps(data)
    # b = json.dumps(list2)

    # 将集合或字典转换成json 对象
    c = json.dumps(list3, ensure_ascii=False)
    return HttpResponse(c)
