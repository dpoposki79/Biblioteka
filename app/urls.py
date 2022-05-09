from django.urls import path
from .views import get_all_books, get_all_members, create_book, create_member, get_del_book, get_del_member, pozajmi, vrati

#from .views import create_country, 

urlpatterns=[
    path("books/", get_all_books),
    path("members/", get_all_members),
    path("new-book/", create_book),
    path("new-member/", create_member),
 #   path("book-qty/", book_qty),
    path("book-get-del/", get_del_book),
    path("member-get-del/", get_del_member),
    path("pozajmi/", pozajmi),
    path("vrati/", vrati)


]