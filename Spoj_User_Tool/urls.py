from django.conf.urls import patterns, url, include
from Spoj_User_Tool.views import home, single_user, submit
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
	url(r'^$', home),
	url(r'^user/([a-z]{1}[a-z0-9_]{2,})$', single_user),
        url(r'^user/(\w+)$', single_user),
        url(r'^user/chetan_shukla$', single_user),
        url(r'^submit$', submit),
    # Examples:
    # url(r'^$', 'Spoj_User_Tool.views.home', name='home'),
    # url(r'^Spoj_User_Tool/', include('Spoj_User_Tool.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
