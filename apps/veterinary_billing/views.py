from django.shortcuts import render, get_object_or_404
from .models import Invoice    

def billing_home(request):
    return render (request,'veterinary_billing/home_billing.html')

def invoice_detail(request, invoice_id):
    invoice = get_object_or_404 (Invoice, id=invoice_id)
    
    context = {
        'invoice': invoice,
        'owner': invoice.client.full_name,  
        'pet_name': invoice.pet.name,  
        'date': invoice.date, 
        'total': invoice.total,  
    }
        
    return render(request, 'veterinary_billing/invoice_detail.html', context)