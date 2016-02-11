from django.conf.urls import patterns, include, url

from django.contrib import admin
from mysite.views import hello
from mysite.views import current_datetime
from mysite.views import hours_ahead
from mysite.books import views
from mysite.contact.views import contact
from mysite.contact.views import thanks
from mysite.log_and_reg.views import login_view,reg_view
from mysite.log_and_reg.testcsrf import add
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    #url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    ('^hello/$',hello),
    ('^time/$',current_datetime),
    (r'^time/plus/(\d{1,2})/$', hours_ahead),
#    (r'^search-form/$',views.search_form),
    (r'^search/$',views.search),
    (r'^contact/$',contact),
    (r'^contact/thanks/$',thanks),
    (r'^register/$',reg_view),
    (r'^account/login/$',login_view),
    (r'^account/loggedin/$',thanks),
    (r'^add/$',add),
    url(r'^admin/', include(admin.site.urls)),
)
