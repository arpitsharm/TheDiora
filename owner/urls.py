from django.urls import path
from . import views

urlpatterns = [
    # Authentication
    path('login/', views.owner_login_view, name='owner_login'),
    path('logout/', views.owner_logout_view, name='owner_logout'),
    
    # Dashboard
    path('dashboard/', views.owner_dashboard_view, name='owner_dashboard'),
    
    # Product Management
    path('products/', views.owner_product_list_view, name='owner_products'),
    path('products/add/', views.owner_product_add_view, name='owner_product_add'),
    path('products/<int:pk>/edit/', views.owner_product_edit_view, name='owner_product_edit'),
    path('products/<int:pk>/delete/', views.owner_product_delete_view, name='owner_product_delete'),
    
    # Order Management
    path('orders/', views.owner_order_list_view, name='owner_orders'),
    path('orders/<int:pk>/', views.owner_order_detail_view, name='owner_order_detail'),
    
    # Customer Management
    path('customers/', views.owner_customer_list_view, name='owner_customers'),
    path('customers/<int:pk>/', views.owner_customer_detail_view, name='owner_customer_detail'),
    
    # Analytics
    path('analytics/', views.owner_analytics_view, name='owner_analytics'),
    
    # Coupon Management
    path('coupons/', views.owner_coupon_list_view, name='owner_coupons'),
    path('coupons/add/', views.owner_coupon_add_view, name='owner_coupon_add'),
    path('coupons/<int:pk>/edit/', views.owner_coupon_edit_view, name='owner_coupon_edit'),
    path('coupons/<int:pk>/delete/', views.owner_coupon_delete_view, name='owner_coupon_delete'),
    
    # Review Management
    path('reviews/', views.owner_review_list_view, name='owner_reviews'),
    path('reviews/<int:pk>/toggle/', views.owner_toggle_review_view, name='owner_toggle_review'),
    path('reviews/<int:review_id>/approve/', views.approve_review_view, name='approve_review'),
    
    # Complaint Management
    path('complaints/<int:complaint_id>/resolve/', views.resolve_complaint_view, name='resolve_complaint'),
    
    # Category Management
    path('categories/', views.owner_category_list_view, name='owner_categories'),
    path('categories/add/', views.owner_category_add_view, name='owner_category_add'),
    path('categories/<int:pk>/edit/', views.owner_category_edit_view, name='owner_category_edit'),
    path('categories/<int:pk>/delete/', views.owner_category_delete_view, name='owner_category_delete'),
    
    # Product Promotion
    path('products/<int:product_id>/promote/', views.owner_promote_product_view, name='owner_promote_product'),
]
