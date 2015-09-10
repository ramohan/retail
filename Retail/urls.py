from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'Store.views.home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^get_info/', 'Store.views.getinfo'),
    url(r'^save/', 'Store.views.save'),
    url(r'^add/', 'Store.views.add_info'),
    url(r'^add_through_script/', 'Store.demo_data.new_data'),
    url(r'^add_demo_data/', 'Store.views.add_first_time'),
    url(r'^add_stock/', 'Store.views.add_stock'),
    url(r'^add_item_wise/', 'Store.views.add_stock_item_wise'),
    url(r'^add_stock_one_shot/', 'Store.views.add_stock_one_shot'),
    #url(r'^home_page/', 'Store.views.home_page'),
)