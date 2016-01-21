from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from .models import Company, Contact

@login_required
def company_listing(request):
    """ All companies. """
    user = request.user
    company = Company.objects.filter(user_id=user.id)
    result = len(company)
    if result != 0:
        return render(request, 'company_listing.html', {'companies': company, 'user': user})
    else:
        return render(request, 'create_perfil.html', {'user': user})


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
    fields = ['name', 'rfc', 'street', 'colony', 'city', 'state']
    success_url = reverse_lazy('companies_list')


class CompanyDelete(DeleteView):
    model = Company
    template_name = 'company_delete_form.html'
    fields = ['name', 'rfc', 'street', 'colony', 'city', 'state']
    success_url = reverse_lazy('companies_list')


class CompanyForm(CreateView):
    template_name = 'company_form.html'
    model = Company
    fields = ['name', 'rfc', 'street', 'colony', 'city', 'state']
    success_url = reverse_lazy('companies_list')

    def get_initial(self):
        return {
            'status': 'a',
            'user': self.request.user,
        }


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
