## 这是一个用户登录和注册的项目
## 这是一个可重用的登录和注册app

## 简单使用方法

创建虚拟环节

使用pip安装第三方依赖

修改settings.example.py文件为settings.py

运行`migrate`命令，创建数据库和数据表

运行`python manage.py runserver`启动服务器

##
路由配置：

```python
# mysite/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('login.urls')),
    path('captcha/', include('captcha.urls'))
]


# login/urls.py
from django.urls import path
from login import views

urlpatterns = [
    path('index/', views.index),
    path('login/', views.login),
    path('register/', views.register),
    path('logout/', views.logout),
    path('confirm/', views.user_confirm),
]

```