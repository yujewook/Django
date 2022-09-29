from django.contrib import admin
from reviewboard.models import Reviewboard

# Register your models here.
class ReviewboardAdmin( admin.ModelAdmin ) :
    list_display = ( "reviewnum", "prodnum", "reviewdate", "userid",
                     "reviewtitle", "reviewcontent", "reviewip" )
admin.site.register( Reviewboard, ReviewboardAdmin )