from email import message
import email
from unicodedata import name
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns=[
    
    path('home/',views.homePage,name='home'),
    path('books/',views.bookPage,name='book'),
    path('register_book/',views.register_bookPage,name='register_book'),
    path('update_book/<str:pk>/',views.updateBook,name='update_book'),
    path('delete_book/<str:pk>/',views.deleteBook,name='delete_book'),
    path('customer/<str:pk>/',views.customerPage,name='customer'),
    path('register/',views.registerPage,name='register'),
    path('',views.loginPage,name='login'),
    path('logout/',views.logoutuser,name='logout'),
    path('user/',views.userPage,name='user-page'),
    path('account/',views.account_setting,name='account'),
    path('create_order/<str:pk>/',views.createOrder,name='create_order'),
    path('create_order_customer/',views.createOrderCustomer,name='create_order_customer'),
    path('update_order/<str:pk>/',views.updateOrder,name='update_order'),
    path('delete_order/<str:pk>/',views.deleteOrder,name='delete_order'),
    path('reset_password/',auth_views.PasswordResetView.as_view(template_name="password_reset.html"), name="password_reset"),
    path('reset_password_sent/',auth_views.PasswordResetDoneView.as_view(template_name="password_reset_sent.html"), name="password_reset_done"),
    path('reset/<uidb64>/<token>',auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_form.html"), name="password_reset_confirm"),
    path('reset_password_complete/',auth_views.PasswordResetCompleteView.as_view(template_name="password_reset_done.html"), name="password_reset_complete"),




# note that:
# PasswordResetView.as_view() is submit email form
# PasswordResetDoneView.as_view() is email sent success message
# PasswordResetConfirmView.as_view() is link for password reset form in email
# PasswordResetCompleteView.as_view() is password successfuly changed message 

    


]