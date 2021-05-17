from django.conf.urls import url
from.import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
url(r'^$', views.index,name="index"),

url(r'^donerReg/', views.donerReg,name="donerReg"),
url(r'^donerRegaction/', views.donerRegaction,name="donerRegaction"),
url(r'^viewDonersPending/', views.viewDonersPending,name="viewDonersPending"),
url (r'^confirmdoner/(?P<value>\d+)/$', views.confirm, name='confirmdoner'),
url(r'^confirmedDoners/', views.confirmedDoners,name="confirmedDoners"),


url(r'^accepterReg/', views.accepterReg,name="accepterReg"),
url(r'^accepterRegaction/', views.accepterRegaction,name="accepterRegaction"),
url(r'^viewAccepterPending/', views.viewAccepterPending,name="viewAccepterPending"),
url (r'^confirmAccepter/(?P<value>\d+)/$', views.confirm, name='confirmAccepter'),
url(r'^confirmedAccepters/', views.confirmedAccepters,name="confirmedAccepters"),

url(r'^loginView/', views.loginView,name="loginView"),
url(r'^loginViewAction/', views.loginViewAction,name="loginViewAction"),
url(r'^viewprofile/', views.viewprofile,name="viewprofile"),
url(r'^logout/', views.logout,name="logout"),


url(r'^addBlood/', views.addBlood,name="addBlood"),
url(r'^addBloodaction/', views.addBloodaction,name="addBloodaction"),
url(r'^viewBlood/', views.viewBlood,name="viewBlood"),

url(r'^updatestatus/', views.updatestatus,name="updatestatus"),
url(r'^donationstatusaction/', views.donationstatusaction,name="donationstatusaction"),

url(r'^search/', views.search,name="search"),
url(r'^searchaction/', views.searchaction,name="searchaction"),
url(r'^viewRequest/', views.viewRequest,name="viewRequest"),
url (r'^sendrequestaction/(?P<value>\d+)/$', views.sendrequestaction, name='sendrequestaction'),
        ]