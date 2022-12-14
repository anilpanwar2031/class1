from django.urls import path
from app import views


urlpatterns = \
    [
        path('', views.index, name='index'),
        path('dashboard/', views.dashboard, name='dashboard'),
        path('quotations/', views.quotation, name='quotations'),
        path('products/', views.products, name='products'),
        path('qsearch/', views.qsearch, name='qsearch'),
        path('psearch/', views.psearch, name='psearch'),
        path('quotation/<int:pk>', views.quotdetail, name='quotdetail'),
        path('newquote', views.newquote, name='newquote'),
        path('delete/<int:qid>/<int:sid>/<int:pid>', views.deletesp, name='deletesp'),
        path('deletesub/<int:qid>/<int:subid>/<int:pid>', views.deletesubp, name='deletesubp'),
        path('export/', views.export_data, name='export'),
        path('savequote/', views.savequote, name='savequote'),

        # path('delete/<int:pk>', views.deletesubp, name='deletesubp')
    ]