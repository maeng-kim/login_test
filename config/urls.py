from django.contrib import admin
from django.urls import include, path
from django.conf import settings

from accounts.views import lotto_index, lotto_result


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('lotto/', lotto_index, name='lotto_index'),
    path('lotto/result/', lotto_result, name='lotto_result'),

]
