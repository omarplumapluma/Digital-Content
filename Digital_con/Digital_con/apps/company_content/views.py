from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from .models import Company_content

@login_required
def company_content_listing(request):
    """ All companies. """
    contents = Company_content.objects.all()
    var_get_search = request.GET.get('search_box')
    if var_get_search is not None:
        contents = contents.filter(name__icontains=var_get_search)
    return render(request, 'company_content_listing.html', {'contents': contents})


@login_required
def company_content_detail(request, pk):
    """ A view. """
    content = Company_content.objects.get(pk=pk)
    context = {'contents': content}
    return render(request, 'company_content_detail.html', context)

class CompanyContentUpdate(UpdateView):
    model = Company_content
    template_name = 'company_content_update_form.html'
    fields = ['company', 'image', 'text', 'status']
    success_url = reverse_lazy('companies_contect_list')


class CompanyContentDelete(DeleteView):
    model = Company_content
    template_name = 'company_content_delete_form.html'
    fields = ['company', 'image', 'text', 'status']
    success_url = reverse_lazy('companies_content_list')


class CompanyContentForm(CreateView):
    template_name = 'company_content_form.html'
    model = Company_content
    fields = ['company', 'campaign', 'description', 'start_date', 'end_date', 'content', 'marquee', 'status']
    success_url = reverse_lazy('companies_content_list')
