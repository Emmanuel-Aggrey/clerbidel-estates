from django.shortcuts import render,get_object_or_404

from  django.views.generic import  TemplateView,DetailView,ListView
from  django.views.generic.edit import  CreateView
from .models import Propertytype,Property,Agent
from  django.db.models import  Q
# Create your views here.


def homeview(request):
    property_ = Property.objects.filter(available=True)
    agents = Agent.objects.filter(available=True)
    p_type = property_.values_list('property_type__name',flat=True).distinct()
    # sale_type = property_.values('sale_type',flat=True).distinct()
    location = property_.values_list('location',flat=True).distinct().exclude(property_type__name='BUILDING')


    query = request.GET.get('p_type')
    query1 = request.GET.get('sale_type')
    query2 = request.GET.get('location')

    if query and query1 or query2:
        property_ = property_.filter(Q(property_type__name__icontains=query)|Q(sale_type__icontains=query1)|Q(location__icontains=query2))
       
    context = {
        'properties':property_,
        # 'backgroud_image':property_.all()[5],
        'agents':agents,
        'p_type':p_type,
        # 'sale_type':sale_type,
        'location':location,


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
    property_ = get_object_or_404(Property,id=id)
    related_properties = Property.objects.filter(available=True,price__lte=property_.price)
    context = {
        'object':property_,
        'related':related_properties,

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






