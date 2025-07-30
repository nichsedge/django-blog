from django.urls import path, include
from rest_framework import renderers
from rest_framework.urlpatterns import format_suffix_patterns

from snippets.views_class_based import SnippetViewSet, UserViewSet, api_root

snippet_list = SnippetViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
snippet_detail = SnippetViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})
snippet_highlight = SnippetViewSet.as_view({
    'get': 'highlight'
}, renderer_classes=[renderers.StaticHTMLRenderer])
user_list = UserViewSet.as_view({
    'get': 'list'
})
user_detail = UserViewSet.as_view({
    'get': 'retrieve'
})

urlpatterns = format_suffix_patterns([
    path('', api_root, name="home_snippet"),
    path('snippets/', snippet_list, name='snippet-list'),
    path('snippets/<int:pk>/', snippet_detail, name='snippet-detail'),
    path('snippets/<int:pk>/highlight/', snippet_highlight, name='snippet-highlight'),
    path('users/', user_list, name='user-list'),
    path('users/<int:pk>/', user_detail, name='user-detail'),
    path('api-auth/', include('rest_framework.urls')),
])

# from django.urls import path, include
# from rest_framework.urlpatterns import format_suffix_patterns
# from snippets import views # function based
# from snippets import views_class_based # class based


# urlpatterns = [
#     # Function
#     path('snippets0/', views.snippet_list),
#     path('snippets0/<int:pk>', views.snippet_detail),

#     # Class
#     path('snippets/', views_class_based.SnippetList.as_view()),
#     path('snippets/<int:pk>/', views_class_based.SnippetDetail.as_view()),
#     path('users/', views_class_based.UserList.as_view()),
#     path('users/<int:pk>/', views_class_based.UserDetail.as_view()),

#     # auth
#     path('api-auth/', include('rest_framework.urls')),

#     # tutorial 5
#     path('', views_class_based.api_root),
#     path('snippets/', views_class_based.SnippetList.as_view(), name='snippet-list'),
#     path('snippets/<int:pk>/', views_class_based.SnippetDetail.as_view(), name='snippet-detail'),
#     path('snippets/<int:pk>/highlight/', views_class_based.SnippetHighlight.as_view(), name='snippet-highlight'),
#     path('users/', views_class_based.UserList.as_view(), name='user-list'),
#     path('users/<int:pk>/', views_class_based.UserDetail.as_view(), name='user-detail')

# ]
