from django import template
#from relevant_app import ItemToDisplay

from django.shortcuts import get_object_or_404, render
from .. import functionss
from django import template
from .. import functionss
#Make a model available to the views
from ..models import Post, PostView

from django import template
register = template.Library()

#@register.inclusion_tag('relevant_app/menu_items.html', takes_context=True)
#def menu_items(context):
 #   return {'items': ItemsToDisplay.objects.all()}




@register.inclusion_tag('sub_archive_pane_test.html', takes_context=True)
def Archives(context):
    blog_posts = Post.objects.all()
    return {'blog_posts': blog_posts}

@register.inclusion_tag('sub_archive_pane.html', takes_context=True)
def ArchiveView(context):
    from django.db import connection, transaction
    cursor = connection.cursor()
# Data retrieval operation

    #cursor.execute("SELECT * FROM mysite_blog_app_db.post_archive_view")
    cursor.execute("SELECT * FROM mysite_blog_app_db.post_archive_view;")
    archives = functionss.dictfetchall(cursor)

    return {"archives":archives}