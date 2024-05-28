from django.urls import path
from . import views
from django.views.generic import TemplateView

urlpatterns = [
<<<<<<< HEAD
    # path('', views.index, name='index'),
    # Navigation bar routing 
    path('', TemplateView.as_view(template_name='nav/index.html'), name="index" ),
    path('Shop/', TemplateView.as_view(template_name='nav/shop-grid.html'), name="shop" ),
    path('Blogs/', TemplateView.as_view(template_name="nav/blog.html"), name="blog" ),
    path('Contact/', TemplateView.as_view(template_name="nav/contact.html"), name="contact" ),

        # pages-dropdown 
    path('Shop-Details/', TemplateView.as_view(template_name='nav/pages/shop-details.html'), name="shop-details" ),
    path('Shoping-Cart/', TemplateView.as_view(template_name='nav/pages/shoping-cart.html'), name="shoping-cart" ),
    path('Checkout/', TemplateView.as_view(template_name='nav/pages/checkout.html'), name="checkout" ),
    path('Blog-Details/', TemplateView.as_view(template_name="nav/pages/blog-details.html"), name="blog-details" ),

=======
    path('', views.index, name='index')
>>>>>>> 381dff768dfadfd0dde741af1c94f794c1adbda6
]