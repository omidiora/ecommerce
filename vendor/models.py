from django.db import models
from .utils import unique_slug_generator
from django.db.models.signals import pre_save,post_save

# Create your models here.
def get_filename_ext(filepath):
    base_name=os.path.bsenme(filepath)
    name,ext-os.path.splitext(base_name)
    return name,ext

def upload_image_path(instance,filenme):
    new_filenme=random.randinit(1,3910209312)
    name,et=get_filename_ext(filenme)
    final_filename='{new_filename}{ext}'.format(new_filename=new_filenme,ext=ext)
    return "product/{new_filename}/{final_filename}".format(
        new_filename=new_filename,
        filename_filename=final_filename,
    )

class ProductManager(models.Manager):
     def featured(self):
        return self.get_queryset().filter(featured=True)
     def get_by_id(self,id):
         qs=self.get_queryset().filter(id=id)
         if qs.count()==1 :
             return qs.first()
         return None

class Product(models.Model):
    title=models.CharField(max_length=120)
    slug=models.SlugField(default='abc')
    description=models.TextField()
    price=models.DecimalField(decimal_places=2,max_digits=20,default=39.99)
    image=models.ImageField(upload_to='products/',null=True,blank=True)
    featured=models.BooleanField(default=False)



    def __str__(self):
        return self.title

    def product_pre_save_receiver(sender,instance,*args,**kwargs):
        if not instance.slug:
            instance.slug='abc'
pre_save.connect(product_pre_save_receiver,sender=Product)

