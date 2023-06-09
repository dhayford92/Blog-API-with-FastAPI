from tortoise import models, fields
from aerich.models import Aerich





class Category(models.Model):
    image = fields.TextField()
    name = fields.CharField(max_length=255)
    
    def __str__(self) -> str:
        return self.name
    class Meta:
        table = 'category'
        
        



class Blog(models.Model):
    image = fields.TextField()
    author = fields.ForeignKeyField('models.User', related_name='users')
    title = fields.CharField(max_length=255)
    body = fields.TextField(null=True)
    categories = fields.ManyToManyField('models.Category', related_name='category')
    is_published = fields.BooleanField(default=False, null=True)
    created_at = fields.DatetimeField(auto_now_add=True)
    modified_at = fields.DatetimeField(auto_now=True, null=True)
    
    def __str__(self):
        return f'{self.author.email} - {self.title}'
    
    class Meta:
        table = 'blogs'
        ordering = ['-created_at', '-modified_at']
        
        
        
        

class Comment(models.Model):
    user = fields.ForeignKeyField('models.User', related_name='comments')
    blog = fields.ForeignKeyField('models.Blog', related_name='blog_comments')
    message = fields.TextField()
    created_at = fields.DatetimeField(auto_now_add=True)   
    
    class Meta:
        table = 'comments'
        ordering = ['-created_at'] 
        
        
        