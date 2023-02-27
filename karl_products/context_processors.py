
from .models import Cart

def cart_count(request):
    cart = Cart.objects.filter(user=request.user.id, active=True).first()
    count = cart.products.count() if cart else 0
    return {'cart_count': count}
