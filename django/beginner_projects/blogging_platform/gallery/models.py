from django.db import models

# Create your models here.
class Product(models.Model):
    name=models.CharField(max_length=255)
    desc=models.TextField()
    image=models.ImageField(upload_to='products/')
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    def edit(self,name,description,image):
        self.name=name
        self.desc=description
        self.image=image
        self.save()

    def short_desc(self):
        #Split the description into words
        words=self.desc.split()
        if len(words)>50:
            #Join the first 50 words and add "..." at the end
            return ' '.join(words[:30])+'...'
        else:
            #If description is already less than 50 words, return it as is
            return self.desc
