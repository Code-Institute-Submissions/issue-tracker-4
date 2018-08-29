from django.db import models
from django.contrib.auth.models import User

# Product
class Issue(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=200)
    date_created = models.DateField(auto_now=True)
    user = models.ForeignKey(User,related_name='user_issue', on_delete=models.CASCADE)
    upvotes = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    
    def __str__(self):
        return self.title

# Gives the user the ability to comment on issues
class Comment(models.Model):
    comment = models.CharField(max_length=200)
    date_created = models.DateField(auto_now=True)
    # ForeignKey links to User and Issues models
    user = models.ForeignKey(User, related_name='user_comment')
    issue = models.ForeignKey(Issue, related_name='issue_comment')

    def __str__(self):
        return self.comment