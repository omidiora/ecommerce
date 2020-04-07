from django.db import models

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

class Product(models.Model):
    title=models.CharField(max_length=120)
    description=models.TextField()
    price=models.DecimalField(decimal_places=2,max_digits=20,default=39.99)
    image=models.FileField(upload_to='products/',null=True,blank=True)



    def __str__(self):
        return self.title

