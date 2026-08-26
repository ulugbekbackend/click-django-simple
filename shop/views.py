from click_up import ClickUp
from rest_framework.views import APIView
from rest_framework import response

from config import settings

from .serializers import OrderSeralizer

click_up = ClickUp(
    service_id=settings.CLICK_SERVICE_ID, 
    merchant_id=settings.CLICK_MERCHANT_ID
)


class OrderCreate(APIView):

    def post(self, request):
        serializer = OrderSeralizer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        result={
            'order':serializer.data
        }

        if serializer.data['payment_method'] == 'click':
            payment_link = click_up.initializer.generate_pay_link(
                id=serializer.data['id'],
                amount=serializer.data['total_cost'],
                return_url='https://ulugbekdev.uz/'
            )
            result['payment_link']=payment_link
        
        return response.Response(result)