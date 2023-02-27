from django.shortcuts import render,redirect,get_object_or_404

# Create your views here.
from django.http import HttpResponse
from django.template import loader
from .models import product,User
from .models import category
from django.core.mail import send_mail
from django.conf import settings
from .models import Review
from .forms import ReviewForm,CreateUserform
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login , logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import product, Cart
from django.http import JsonResponse


@login_required
def cart_count(request):
    cart = Cart.objects.filter(user=request.user.id, active=True).first()
    if cart:
        count = cart.products.count()
    else:
        count = 0
    return {'cart_count': count}

@login_required
def add_to_cart(request, slug):
    # Retrieve the product using its slug
    product_instance = get_object_or_404(product, slug=slug)

    # Retrieve the cart associated with the logged-in user
    cart_instance, created = Cart.objects.get_or_create(user=request.user, active=True)

    # Add the product to the cart
    cart_instance.products.add(product_instance)
    messages.success(request, f"{product_instance.name} was added to your cart.")


    # Redirect the user to the cart page
    return redirect('cart')

@login_required
def cart_view(request):
    cart = Cart.objects.filter(user=request.user, active=True).first()
    cart_count = cart.products.count() if cart else 0
    context = {'cart': cart, 'cart_count': cart_count}
    return render(request, 'cart.html', context)



@login_required
def remove_from_cart(request, product_slug):
    cart = Cart.objects.filter(user=request.user, active=True).first()
    product_obj = get_object_or_404(product, slug=product_slug)
    cart.products.remove(product_obj)
    messages.success(request, f"{product_obj.name} was removed from your cart.")
    return redirect('cart')



def home(request):
    featured_products = product.objects.filter(featured=True)
    reviews = Review.objects.all()
    data = category.objects.all()
    product_data = product.objects.all()
    return render(request, 'index.html', {'category': data , 'product' : product_data , 'featured': featured_products, 'reviews': reviews })

def product_category(request, cats):
    # product_cats = category.objects.get(name=cats).product.all()
    data = category.objects.all()
    product_cats = product.objects.filter(category_id__name=cats)
    return render(request , 'category.html' , {'product_cats': product_cats , 'category': data})

def register(request):
    form = CreateUserform()
    context = {'form' : form}
    if request.method == 'POST':
        form = CreateUserform(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'your account has been created successfully')
            return redirect('../login')
    return render(request , 'register.html' , context)

def loginPage(request):
    context = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username = username , password = password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request ,'Username or Password is incorrect')
    return render(request , 'login.html' , context)

def logoutUser(request):
    logout(request)
    return redirect('../login')




def shop(request):
    data = category.objects.all()
    product_data = product.objects.all()
    return render(request, 'shop.html', {'category': data , 'product' : product_data})

def checkout(request):
    template = loader.get_template('checkout.html')
    return HttpResponse(template.render())

def single(request,slug):
    data = category.objects.all()
    product_data = get_object_or_404(product, slug=slug)
    return render(request, 'single.html', {'category': data , 'product' : product_data})

def succes(request):
        return render(request, 'succes.html')

def contact(request):
    data = category.objects.all()
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        description = request.POST['description']

        send_mail(
            'New Contact Form Submission',
            'Name: ' + name + '\nEmail: ' + email + '\nPhone: ' + phone + '\nDescription: ' + description,
            email,
            ['fever8292@gmail.com'],
            fail_silently=False,
        )

        return redirect('successfully')

    return render(request, 'contact.html' , { 'category': data })

def review(request):
    data = category.objects.all()
    if request.method == 'POST':
        form = ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ReviewForm()
    return render(request, 'review.html', {'form': form , 'category': data})

# def add_to_cart(request,id):
#     user = request.user.id
#     product_cart = product.objects.filter(id=id)
#     cart_items = cart.objects.create(user_id=user,product_id=product_cart)
#     cart_items.save()
#     return HttpResponseRedirect(request.path_info)


