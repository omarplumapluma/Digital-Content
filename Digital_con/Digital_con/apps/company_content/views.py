from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from .models import Company_content, Company_media
from Digital_con.apps.company.models import Company

@login_required
def company_content_listing(request):
    """ All companies. """
    contents = Company_content.objects.all()
    var_get_search = request.GET.get('search_box')
    if var_get_search is not None:
        contents = contents.filter(campaign__icontains=var_get_search)
    return render(request, 'company_content_listing.html', {'contents': contents})


@login_required
def company_content_detail(request, pk):
    """ A view. """
    content = Company_content.objects.get(pk=pk)
    context = {'contents': content}
    return render(request, 'company_content_detail.html', context)


@login_required
def company_media_listing(request):
    """ All companies. """
    contents = Company_media.objects.all()
    var_get_search = request.GET.get('search_box')
    if var_get_search is not None:
        contents = contents.filter(name__icontains=var_get_search)
    return render(request, 'company_media_listing.html', {'contents': contents})


class CompanyContentUpdate(UpdateView):
    model = Company_content
    template_name = 'company_content_update_form.html'
    fields = ['company', 'campaign', 'description', 'start_date', 'end_date', 'marquee', 'status']
    success_url = reverse_lazy('companies_content_list')


class CompanyContentDelete(DeleteView):
    model = Company_content
    template_name = 'company_content_delete_form.html'
    fields = ['company', 'campaign', 'description', 'start_date', 'end_date', 'marquee', 'status']
    success_url = reverse_lazy('companies_content_list')


class CompanyContentForm(CreateView):
    template_name = 'company_content_form.html'
    model = Company_content
    fields = ['company', 'campaign', 'description', 'start_date', 'end_date', 'marquee', 'status']
    success_url = reverse_lazy('companies_content_list')

    def get_initial(self):
        user = self.request.user
        company = Company.objects.filter(user_id=user.id)
        return {
            'company': company[0],
        }

class CompanyMediaForm(CreateView):
    template_name = 'company_media_form.html'
    model = Company_media
    fields = ['company', 'files']
    success_url = reverse_lazy('companies_media_list')

    def get_initial(self):
        user = self.request.user
        company = Company.objects.filter(user_id=user.id)
        return {
            'company': company[0],
        }

