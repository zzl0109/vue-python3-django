from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from common.models import Customer

# 先定义好HTML模板
html_template = '''
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<style>
table {
    border-collapse: collapse;
}
th, td {
    padding: 8px;
    text-align: left;
    border-bottom: 1px solid #ddd;
}
</style>
</head>
    <body>
        <table>
        <tr>
        <th>id</th>
        <th>姓名</th>
        <th>电话号码</th>
        <th>地址</th>
        <th>qq</th>
        </tr>

        %s


        </table>
    </body>
</html>
'''


def listcustomers(request):

    qs = Customer.objects.values()

    ph = request.GET.get('phone_number', None)

    if ph:
        qs = qs.filter(phone_number=ph)

    res = ''
    for customer in qs:
        res += '<tr>'

        for name,value in customer.items():
            res += f'<td>{value}</td>'
        res += '</tr>'

    return HttpResponse(html_template % res)



