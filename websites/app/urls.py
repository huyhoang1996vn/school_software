from django.conf.urls import url, include
import views
from rest_framework import routers
from django.conf.urls.static import static
from django.conf import settings
from rest_framework.authtoken import views as auth_view
from django.views.decorators.csrf import csrf_exempt

router = routers.DefaultRouter()
router.register(r'userbase', views.UserBaseViewSet)
router.register(r'product', views.ProductViewSet)
router.register(r'category', views.CategoryViewSet)
router.register(r'feedback', views.FeedbackViewSet)
router.register(r'supplier', views.SupplierViewSet)
router.register(r'order/store', views.OrderViewSet)
router.register(r'store/owner', views.StoreViewSet, base_name='store-list')
router.register(r'order', views.OrderAdminViewSet)



urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^', include(router.urls)),
    url(r'^register/$', views.UserViewSet.as_view({'post': 'create'})),
    url(r'^profile/$', views.profile_user),
    url(r'^login/$', auth_view.obtain_auth_token, name='login'),
    url(r'^cart/$', views.view_cart, name='view_cart'),
    url(r'^cart/modify/$', views.modify_cart, name='modify_cart'),
    url(r'^change/password/$', csrf_exempt(views.change_passqord), name="change-passqord"),
    url(r'^paypal/redirect', views.redirect_paypal, name="change-passqord"),
    url(r'^paypal/confirm', views.payment_confirm, name="change-passqord"),
    url(r'^paypal/payment/$', views.payment, name="change-passqord"),
    url(r'^order/create/$', views.create_order, name="change-passqord"),
    url(r'^order/list/$', views.list_order, name="change-passqord"),
    url(r'^group/user/$', views.get_group_user, name="get_group_user"),



]
    