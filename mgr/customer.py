import json
from django.http import JsonResponse
from common.models import Customer


def dispatcher(request):
    # 将请求的参数统一放进request.params属性中，方便以后处理

    # GET请求：参数在GET属性中
    if request.method == 'GET':
        request.params = request.GET

    # 其他请求参数在body中
    if request.method in ['POST', 'PUT', 'DELETE']:
        # 此请求类型body是json字符串
        request.params = json.loads(request.body)

    # 拿到参数的类型
    action = request.params['action']

    # 不同类型交给不同的处理函数
    if action == 'list_customer':
        return list_customer(request)
    elif action == 'add_customer':
        return add_customer(request)
    elif action == 'modify_customer':
        return modify_customer(request)
    elif action == 'del_customer':
        return delete_customer(request)
    else:
        return JsonResponse({'ret': 1, 'message': '参数错误'})


def list_customer(requset):
    # 返回的是QuerySet对象，里面保护所以的表记录
    qs = Customer.objects.values()
    retlist = list(qs)
    return JsonResponse({'ret': 0, 'retlist': retlist})


def add_customer(requset):
    info = requset.params['data']
    record = Customer.objects.create(name=info['name'],
                            phone_number=info['phone_number'],
                            address=info['address'])

    return JsonResponse({'ret': 0, 'id': record.id})


def modify_customer(requset):
    modify_id = requset.params['id']
    try:
        modify_record = Customer.objects.get(id=modify_id)
    except Customer.DoesNotExist:
        return JsonResponse(
            {
                'ret': 1,
                'message': f'id为{modify_id}的客户不存在'
            }
        )
    new_data = requset.params['newData']
    if 'name' in new_data:
        modify_record['name'] = new_data['name']
    if 'phone_number' in new_data:
        modify_record['phone_number'] = new_data['phone_number']
    if 'address' in new_data:
        modify_record['address'] = new_data['address']
    # 修改过后调用save方法，将改动映射到数据库
    modify_record.save()

    return JsonResponse({'ret': 0})


def delete_customer(requset):
    delete_id = requset.params['id']
    try:
        delete_record = Customer.objects.get(id=delete_id)
    except Customer.DoesNotExist:
        return JsonResponse(
            {
                'ret': 1,
                'message': f'id为{delete_id}的客户不存在'
            }
        )
    delete_record.delete()

    return JsonResponse({'ret': 0})
