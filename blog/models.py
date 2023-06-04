from tortoise import models, fields
from tortoise.contrib.pydantic import pydantic_model_creator as serializer



class Category(models.Model):
    name = fields.CharField(max_length=255)
    class Meta:
        table = 'category'
        
        



class Blog(models.Model):
    author = fields.ForeignKeyField('models.User', related_name='blog')
    title = fields.CharField(max_length=255)
    body = fields.TextField(null=True)
    categories = fields.ManyToManyField('models.Category')
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
        
        
        
        


# --- serialization with pydantic ---
CategorySerializer = serializer(Category, name="Category")
CategoryInSerializer = serializer(Category, name="CategoryIn", exclude_readonly=True)

