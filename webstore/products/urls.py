from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.pag_main, name='pag_main'),
    path('prods/list/', views.prod_list, name='prod_list'),
    path('prods/<int:pk>/', views.prod_detail, name='prod_detail'),
    path('prods/new/', views.prod_new, name='prod_new'),
    path('prods/<int:pk>/edit/', views.prod_edit, name='prod_edit'),
    path('prods/<int:pk>/delete/', views.prod_delete, name='prod_delete'),
    
    path('sells/list/', views.sell_list, name='sell_list'),
    path('sells/new/', views.sell_new, name='sell_new'),
    path('sells/<int:pk>/', views.sell_detail, name='sell_detail'),
    path('sells/<int:pk>/edit/', views.sell_edit, name='sell_edit'),
    path('sells/<int:pk>/delete/', views.sell_delete, name='sell_delete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)