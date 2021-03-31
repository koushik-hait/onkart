from rest_framework import viewsets
from django.http import JsonResponse
from django.contrib.auth import get_user_model
from .serializers import OrderSerializer
from .models import Order
from django.views.decorators.csrf import csrf_exempt


# Create your views here.

def validate_user_session(id, token):
    UserModel = get_user_model()
    try:
        user = UserModel.objects.get(pk=id)
        if user.session_token == token:
            return True
        else:
            return False
    except UserModel.DoesNotExist:
        return False


@csrf_exempt
def add(request, id, token):
    if not validate_user_session(id, token):
        return JsonResponse({'error': 'Please login', 'code': '1'})
    if request.method == 'POST':
        user_id = id
        transaction_id = request.POST['transaction_id']
        total_amount = request.POST['total_amount']
        products = request.POST['products']

        total_products = len(products.split(',')[:-1])
        UserModel = get_user_model()
        try:
            user = UserModel.objects.get(pk=id)
        except UserModel.DoesNotExist:
            return JsonResponse({'error': 'User Does not exists!'})
        ordr = Order(user=user, transaction_id=transaction_id, total_amount=total_amount, product_names=products,
                     total_products=total_products, )
        ordr.save()
        return JsonResponse({'success': True, 'error': False, 'msg': 'Order Placed successfully'})


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all().order_by('id')
    serializer_class = OrderSerializer
