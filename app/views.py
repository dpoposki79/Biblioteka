from django.shortcuts import render
from requests import Response
from .models import Knigi, Clenovi
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import KnigiSerilizer, ClenoviSerilizer
from django.utils.timezone import now
# Create your views here.


# GET BOOKS
@api_view(["GET"])  
def get_all_books(request):
    allBooks=Knigi.objects.all().order_by("-Naslov")
    books_serializer=KnigiSerilizer(allBooks, many=True)
    return Response(books_serializer.data)

# GET MEMBERS
@api_view(["GET"])  
def get_all_members(request):
    allMembers=Clenovi.objects.all().order_by("-Ime")
    members_serializer=ClenoviSerilizer(allMembers, many=True)
    return Response(members_serializer.data)

# GET & DELETE MEMBER
@api_view(["GET", "DELETE"])  
def get_del_member(request):
    if request.method == "GET":
        Members=Clenovi.objects.get(id=request.GET["id"])
        members_serializer=ClenoviSerilizer(Members, many=False)
        return Response(members_serializer.data)
    elif request.method == "DELETE":  
        member_for_delete = Clenovi.objects.get(id=request.data["id"])
        member_for_delete.delete()
        return Response({"Info": "Clenot e izbrisan"})

#POST, DELETE, PUT BOOKS
@api_view(["POST", "DELETE"]) #"PUT"]) 
def create_book(request):
    if request.method == "POST":
        books_serilizer = KnigiSerilizer(data=request.data, many=True) 
        if books_serilizer.is_valid():
            books_serilizer.save()
            return Response(books_serilizer.data)
#    return Response(books_serilizer.errors)
    elif request.method == "DELETE":  
        kniga_for_delete = Knigi.objects.get(id=request.data["id"])
        kniga_for_delete.delete()
        return Response({"Info": "Knigata e izbrisana"})
"""
    elif request.method =="PUT":
        kniga_for_update = Knigi.objects.get(id = request.data['id'])
        kniga_for_update.Naslov = request.data['Naslov']
        kniga_for_update.save()
        knigi_serializer = KnigiSerilizer(kniga_for_update)
        return Response(knigi_serializer.data)
"""
#GET & DELETE BOOK
@api_view(["GET", "DELETE"])  
def get_del_book(request):
    if request.method == "GET":
        books=Knigi.objects.get(id=request.GET["id"])
        books_serializer=KnigiSerilizer(books, many=False)
        return Response(books_serializer.data)

    elif request.method == "DELETE":  
        kniga_for_delete = Knigi.objects.get(id=request.data["id"])
        kniga_for_delete.delete()
        return Response({"Info": "Knigata e izbrisana"})

#PATCH BOOK QTY
"""
@api_view(["PATCH"]) 
def book_qty(request):
    kniga_qty = Knigi.objects.get(id = request.data['id'])
    kniga_qty.Kolicina = request.data['Kolicina']
    kniga_qty.save()
    knigi_serializer = KnigiSerilizer(kniga_qty)
    return Response(knigi_serializer.data)
"""
#POST, DELETE, PUT MEMBERS
@api_view(["POST", "DELETE"]) 
def create_member(request):
    members_serilizer = ClenoviSerilizer(data=request.data, many=True) 
    if request.method == "POST":
        if members_serilizer.is_valid():
            members_serilizer.save()
            return Response(members_serilizer.data)
        #return Response(members_serilizer.errors)
    elif request.method == "DELETE":   
        clen_for_delete = Clenovi.objects.get(id=request.data["id"])
        clen_for_delete.delete()
        return Response({"Info": "Clenot e izbrisan"})
"""
    elif request.method =="PUT":
        clen_for_update = Clenovi.objects.get(id = request.data['id'])
        clen_for_update.Ime = request.data['Ime']
        clen_for_update.save()
        knigi_serializer = ClenoviSerilizer(clen_for_update)
        return Response(knigi_serializer.data)
"""

@api_view(["GET", "POST"])
def pozajmi(request):
    clenId = request.data["clenId"]
    knigaId = request.data["knigaId"]
    clen = Clenovi.objects.get(id=clenId)
    kniga = Knigi.objects.get(id=knigaId)


    # promena kaj clen
    clen.Dali_ima_pozajmeno = True
    clen.Pozajmena_kniga = kniga
    clen.Data_pozajmuvanje = now()
    clen.denovi_potsetuvanje = request.data["denoviPotsetuvanje"]
    clen.save()

    #promena kaj kniga
    kniga.Kolicina = kniga.Kolicina-1
    kniga.save()  

    #vrakanje podatoci
    clen_serializer = ClenoviSerilizer(clen)
    return Response(clen_serializer.data)
    

@api_view(["GET", "POST"])
def vrati(request):
    clenId = request.data["clenId"]
    knigaId = request.data["knigaId"]
    clen = Clenovi.objects.get(id=clenId)
    kniga = Knigi.objects.get(id=knigaId)

    # promena kaj clen
    clen.Dali_ima_pozajmeno = False
    clen.Pozajmena_kniga = None
    clen.save()

    #promena kaj kniga
    kniga.Kolicina = kniga.Kolicina + 1
    kniga.save()  

    #vrakanje podatoci
    clen_serializer = ClenoviSerilizer(clen)
    return Response(clen_serializer.data)
    