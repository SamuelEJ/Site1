from django.contrib import admin

# Register your models here.
from .models import Post
from .models import Tags
from .models import Author1
from .models import Author2


#class Author2Inline(Tags.TabularInline):
 #    model = Author2


class PostAdmin(admin.ModelAdmin):
   # fields = ['question_text']
    list_display = ['Title', 'Opening_Para', 'Author1', 'Actual_Author1', 'get_tags', 'image_tag']
    #inline = [Author2Inline]
    def Actual_Author1(self, obj):
     return obj.Author1.Author1_name
    Actual_Author1.short_description = 'Primary Author'
    readonly_fields = ('image_tag',)
   # readonly_fields = ('image_preview',)
   ## def image_preview(self, obj):
   #  Image = getattr(obj, 'image', '')
   #  return format_html(u'<img src="{}" />', Image)




class Author1Admin(admin.ModelAdmin):
    # fields = ['question_text']
    list_display = ['Author1_name']



admin.site.register(Post, PostAdmin)
admin.site.register(Tags)
admin.site.register(Author1, Author1Admin)
admin.site.register(Author2)
