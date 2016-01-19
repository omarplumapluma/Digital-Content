from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from .models import Company, Contact

@login_required
def company_listing(request):
    """ All companies. """
    companies = Company.objects.all()
    var_get_search = request.GET.get('search_box')
    if var_get_search is not None:
        companies = companies.filter(name__icontains=var_get_search)
    return render(request, 'company_listing.html', {'companies': companies})


@login_required
def company_detail(request, pk):
    """ A view. """
    company = Company.objects.get(pk=pk)
    print(company.rfc)
    contacts = Contact.objects.all().filter(company=company)
    context = {'company': company}
    return render(request, 'company_detail.html', context)


class CompanyUpdate(UpdateView):
    model = Company
    template_name = 'company_update_form.html'
    fields = ['name', 'rfc', 'street', 'colony', 'city', 'state', 'user', 'password']
    success_url = reverse_lazy('companies_list')


class CompanyDelete(DeleteView):
    model = Company
    template_name = 'company_delete_form.html'
    fields = ['name', 'rfc', 'street', 'colony', 'city', 'state', 'user', 'password']
    success_url = reverse_lazy('companies_list')


class CompanyForm(CreateView):
    template_name = 'company_form.html'
    model = Company
    fields = ['name', 'rfc', 'street', 'colony', 'city', 'state', 'user', 'password']
    success_url = reverse_lazy('companies_list')


class ContactForm(CreateView):
    template_name = 'contact_form.html'
    model = Contact
    success_url = reverse_lazy('companies_list')


@login_required(login_url='/accounts/login/')
def protected_view(request):
    """ A view that can only be accessed by logged-in users """
    return render(request, 'companies/protected.html', {'current_user': request.user})


def message(request):
    """ Message if is not authenticated. Simple view! """
    return HttpResponse('Access denied!')
