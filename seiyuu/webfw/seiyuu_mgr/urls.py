from django.conf.urls import patterns, include, url

from webfw.seiyuu_mgr import views

urlpatterns = patterns('webfw.seiyuu_mgr.views',
    # Examples:
    # url(r'^$', 'webfw.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^(?P<season>\w+)?$', "seiyuu.seiyuu_list", name="seiyuu_list"),
)
