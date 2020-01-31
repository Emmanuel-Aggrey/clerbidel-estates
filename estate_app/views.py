
from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from  django.views.generic import  TemplateView,DetailView,ListView
from django.urls import reverse_lazy
from  rest_framework import generics
from .serializers import Phoneserializer
from  django.views.generic.edit import  CreateView,DeleteView,UpdateView
from .models import Propertytype,Property,Agent,Gallary,Phone
from .forms import AddlandForm,AddhouseForm,PhoneForm
from  django.db.models import  Q

# Create your views here.


def homeview(request):
    form = PhoneForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('estate_app:home')
    # request.session['user'] = request.user
    gallary = Gallary.objects.all()
    property_ = Property.objects.filter(available=True)
    agents = Agent.objects.filter(available=True)
    p_type = property_.values_list('property_type__name',flat=True).distinct()
    # sale_type = property_.values('sale_type',flat=True).distinct()
    location = property_.values_list('location',flat=True).distinct()#.exclude(property_type__name='BUILDING')


    query = request.GET.get('p_type')
    query1 = request.GET.get('sale_type')
    query2 = request.GET.get('location')

    if query and query1 or query2:
        property_ = property_.filter(Q(property_type__name__icontains=query)|Q(sale_type__icontains=query1)|Q(location__icontains=query2))
       
    context = {
        'gallary':gallary,
        'properties':property_,
        # 'backgroud_image':property_.all()[5],
        'agents':agents,
        'p_type':p_type,
        # 'sale_type':sale_type,
        'location':location,
        'form':form,


    }
    return render(request, 'estate_app/index.html',context)



class Hometlistview(ListView):
    template_name = 'estate_app/index.html'
    # queryset = Property.objects.filter(available=True)
    context_object_name = 'objects'
    def get_queryset(self,request):
        queryset = {'properties':Property.objects.filter(available=True),
        'agents':Agent.objects.filter(available=True)
        }
        return queryset
    
    
def propertydetalview(request,id):
    # related_properties = None
    property_ = get_object_or_404(Property,id=id)
    # if property_.price:
    related_properties = Property.objects.filter(available=True)
    context = {
        'object':property_,
        'related':related_properties,
        # 'userphone':Phone.objects.filter(user=property_.created_by)

    }
    return render(request,'estate_app/property-details.html',context)

# not using this using above ie method
class Propertiesdetailview(DetailView):
    template_name = 'estate_app/property-details.html'
    context_object_name ='property'
    model =Property
    # def get_queryset(self):
    #     queryset = {'property':Property.objects.filter(available=True),
    #     'properties':Agent.objects.filter(available=True)
    #     }
    #     return queryset
    

class Contactview(ListView):
    template_name = 'estate_app/contact.html'
    queryset = Agent.objects.filter(available=True)


class AboutView(ListView):
    template_name = 'estate_app/about.html'
    queryset = Agent.objects.filter(available=True)

class Addlandview(LoginRequiredMixin,CreateView,ListView):
   
    # model = Property
    paginate_by = '5'
    form_class = AddlandForm
    success_url = reverse_lazy('estate_app:addland')

    def form_valid(self, form):
        form.instance.created_by = self.request.user   
        form.instance.user_phone = self.request.user.userphone.phonenumber   
 
        return super().form_valid(form)
    
    def get_queryset(self):
        queryset = Property.objects.filter(available=True,property_type__name__iexact='land',\
        created_by=self.request.user).order_by('-date_updated')
        return queryset 
    
class Updatelandview(LoginRequiredMixin,UpdateView):
    model = Property
    template_name = 'estate_app/property_form.html'
    success_url = reverse_lazy('estate_app:addland')
    form_class = AddlandForm




 
class Addhomeview(LoginRequiredMixin,CreateView,ListView):
    paginate_by = '5'
    model = Property
    form_class =AddhouseForm
    success_url = reverse_lazy('estate_app:addhome')
   
    def form_valid(self, form):
        form.instance.created_by = self.request.user        
        return super().form_valid(form)
    def get_queryset(self):
        queryset = Property.objects.filter(available=True,property_type__name__iexact='building',\
        created_by=self.request.user).order_by('-date_updated')
        return queryset 
    
class Updatehomeview(LoginRequiredMixin,UpdateView):
    model = Property
    template_name = 'estate_app/property_form.html'
    form_class =AddhouseForm
    success_url = reverse_lazy('estate_app:addhome')




  
   
def deleteland(request,id):
    if request.method == 'POST':
        property_ = Property.objects.get(id=id)
        property_.delete()
        
        return redirect('estate_app:addland')


def deletehome(request,id):
    if request.method == 'POST':
        property_ = Property.objects.get(id=id)
        property_.delete()
        
        return redirect('estate_app:addhome')


class Addphoneview(generics.CreateAPIView):
    serializer_class = Phoneserializer
    def post(self,request):
        return self.create(request)
    
    def perform_create(self,serializer):
        serializer.save(user=self.request.user)

class UserphoneExistview(generics.ListAPIView):
    pass