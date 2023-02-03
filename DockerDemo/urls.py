"""DockerDemo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.static import serve

from demoApp.views import index_view

urlpatterns = (
    [
        path("admin/", admin.site.urls),
        path("demo/", include("demoApp.urls")),
        path("", index_view),
    ]
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
)

re_path(r"^media/(?P<path>.*)$", serve, {"document_root": settings.MEDIA_ROOT}),
re_path(r"^static/(?P<path>.*)$", serve, {"document_root": settings.STATIC_ROOT}),

handler404 = "demoApp.views.error_404"
handler500 = "demoApp.views.error_500"

# handler500 = "utils.exceptionHandler.server_error"

# handler403 = 'demoApp.views.error_403'
# handler400 = 'demoApp.views.error_400'

urlpatterns += [
    path("api-auth/", include("rest_framework.urls")),
    path("api/", include("demoApp.api.urls")),
]
