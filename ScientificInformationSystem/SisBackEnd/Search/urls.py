from django.urls import path
from . import views
urlpatterns = [
    path('get_authors_by_name', views.get_authors_by_name,),
    path('get_personalinfo_by_uniid', views.get_personalinfo_by_uniid,),
    path('get_paper_title_by_uniid', views.get_paper_title_by_uniid,),
    path('get_paper_detail_by_title', views.get_paper_detail_by_title,),
    path('get_interpersonal_relationship_network_by_uniid', views.get_interpersonal_relationship_network_by_uniid,),
    path('get_journal_by_name', views.get_journal_by_name, ),
    path('get_paper_by_journal_name', views.get_paper_by_journal_name, ),
    path('get_journal_publish_every_year_by_journal_name', views.get_journal_publish_every_year_by_journal_name, ),
    path('get_journal_keyword_by_journal_name', views.get_journal_keyword_by_journal_name, ),
    path('get_journal_author_rank_by_journal_name', views.get_journal_author_rank_by_journal_name, ),
    path('get_organization_by_name', views.get_organization_by_name, ),
    path('get_paper_by_organization_name', views.get_paper_by_organization_name, ),
    path('get_organization_publish_every_year_by_organization_name', views.get_organization_publish_every_year_by_organization_name, ),
    path('get_organization_keyword_by_organization_name', views.get_organization_keyword_by_organization_name, ),
    path('get_organization_author_rank_by_organization_name', views.get_organization_author_rank_by_organization_name, ),
    path('user_login', views.user_login, ),
    path('add_authors', views.add_authors, ),
]