from django.shortcuts import render,redirect
from django.views.generic import ListView,DetailView
from .models import Product


class ProductFeaturedListView(ListView):
    template_name="products/list.html"
    def get_queryset(self,*args,**kwargs):
          request=self.request
          return Product.objects.all()
           
       


# class ProductManager(models.Manager):
#     def get_by_id(self,id):
#         qs=self.get_queryset.filter(id=id)
#         if qs.count()==1 :
#             return qs.first()
#         return None
   
   
   

class ProductFeaturedDetailView(DetailView):
  
    template_name="products/featured-detail.html"

    def get_queryset(self,*args,**kwargs):
        request=self.request
        return Product.objects.all()
        #   qs=Product.objects.get(pk=id)
        #   js=qs.filter(featured=True)
          
    # def get_context_data(self,*args,**kwargs):
    #     context=super(ProductFeaturedDetailView,self).get_context_data(*args,**kwargs)   
    #     context['heloo']=js   
    #     return context






class ProductListView(ListView):
    queryset=Product.objects.all()
    template_name="products/list.html"

    
  

    

    # def get_object(self,*args,**kwargs):
    #     request=self.request
    #     pk=self.kwargs.get("pk")
    #     instance=Product.objects.get_by_id(pk)
    #     if instance is None:
    #         raise Http404("product does not eist")
    #     raise instance

    



class ProductDetailView(DetailView,):
     model=Product
     template_name="products/detail.html"






# # Create your views here.
# def homepage(request):
#     context={
#         'content':'welcome to the homepage',
      
        
#     }
#     context['premiun_content']='yeahdjiklkondko'
#     return render(request,'homepage.html',context)


# def aboutpage(request):
#     context={}
#     return render(request,'about.html',context)


# def contactpage(request):
#     contact_form=ContactForm(request.POST or None)
#     context={'form':contact_form}
#     if contact_form.is_valid():
#         print(contact_form.cleaned_data)
   
#     return render(request,'contact.html',context)


# def login_page(request):
#     form=LoginForm(request.POST or None)
#     context={'form':form}
#     if form.is_valid():
#         username=form.cleaned_data.get("username")
#         password=form.cleaned_data.get("password")
#         user=authenticate(request,username=username,password=password)
#         if user is not None:
#             login(request,user)
#             print(form.cleaned_data)
#             context['form']=LoginForm()
#             return redirect("/login")
#         else:
#             print("Error")
        
#     return render(request,"auth/login.html",context)

# User=get_user_model()
# def register_page(request):
#     form=RegisterForm(request.POST or None)
#     context={
#         'form':form
#     }
#     if form.is_valid():
#         username=form.cleaned_data.get("username")
#         password=form.cleaned_data.get("password")
#         email=form.cleaned_data.get("email")
#         print(form.cleaned_data )
#         ppp= User.objects.create_user(username,password,email)
#         print(ppp)
#     return render(request,"auth/register.html",context)

