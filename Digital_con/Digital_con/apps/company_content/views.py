from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.views.generic import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from .models import Company_content, Company_media, Campaing_media
from .forms import CampaingForm, CompanyContentForm
from Digital_con.apps.company.models import Company
from django.shortcuts import render_to_response, redirect
from django.template.context import RequestContext


@login_required
def company_content_listing(request):
    """ All companies. """
    user = request.user
    company = Company.objects.filter(user_id=user.id)
    contents = Company_content.objects.filter(company=company[0].pk)
    var_get_search = request.GET.get('search_box')
    if var_get_search is not None:
        contents = contents.filter(campaign__icontains=var_get_search)
    return render(request, 'company_content_listing.html', {'contents': contents})


@login_required
def company_media_listing(request):
    """ All files. """
    user = request.user
    company = Company.objects.filter(user_id=user.id)
    contents = Company_media.objects.filter(company=company[0].pk)
    return render(request, 'company_media_listing.html', {'contents': contents})


@login_required
def company_campaing_listing(request):
    """ All files. """
    user = request.user
    company = Company.objects.filter(user_id=user.id)
    contents = Campaing_media.objects.filter(company=company[0].pk)
    return render(request, 'company_campaing_listing.html', {'contents': contents})


@login_required
def company_media_options(request):
    """ All files. """
    user = request.user
    company = Company.objects.filter(user_id=user.id)
    contents = Company_media.objects.filter(company=company[0].pk)
    return render(request, 'company_media_content.html', {'contents': contents})

@login_required
def company_content_detail(request, pk):
    """ A view. """
    content = Company_content.objects.get(pk=pk)
    context = {'contents': content}
    return render(request, 'company_content_detail.html', context)


@login_required
def company_campaing_detail(request, pk):
    """ A view. """
    content = Campaing_media.objects.get(pk=pk)
    ids = content.content
    dic_con = ids.split(',')
    dic = []
    for pk in dic_con:
        media_con = Company_media.objects.filter(id=pk)
        dic.append(media_con[0])
    context = {'campaing': content, 'contents': dic}
    return render(request, 'company_campaing_detail.html', context)


class CompanyContentUpdate(UpdateView):
    model = Company_content
    template_name = 'company_content_update_form.html'
    form_class = CompanyContentForm
    success_url = reverse_lazy('companies_content_list')


class CompanyContentDelete(DeleteView):
    model = Company_content
    template_name = 'company_content_delete_form.html'
    fields = ['company', 'campaign', 'description', 'start_date', 'end_date', 'marquee', 'status']
    success_url = reverse_lazy('companies_content_list')

class CompanyMediaDelete(DeleteView):
    model = Company_media
    template_name = 'company_media_delete_form.html'
    fields = ['company', 'files']
    success_url = reverse_lazy('companies_media_list')

class CompanyCampaingDelete(DeleteView):
    model = Campaing_media
    template_name = 'company_campaing_delete_form.html'
    fields = ['company', 'content', 'campaign']
    success_url = reverse_lazy('company_campaing_list')


class CompanyContentForm(CreateView):
    template_name = 'company_content_form.html'
    model = Company_content
    form_class = CompanyContentForm
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

class CompanyCampaingForm(CreateView):
    template_name = 'company_campaing_form.html'
    model = Campaing_media
    fields = ['company', 'content', 'campaing', 'status']
    success_url = reverse_lazy('company_campaing_list')

    def get_initial(self):
        user = self.request.user
        company = Company.objects.filter(user_id=user.id)
        return {
            'company': company[0],
        }

@login_required
def Create_campaing_content(request):
    if request.method == 'POST':  # If the form has been submitted...
        form = CampaingForm(request.POST)  # A form bound to the POST data
        if form.is_valid():  # All validation rules pass
            campaing=form.save(commit=False)
            campaing.save()
            return redirect('company_campaing_list')
    else:
        initial_data = {}
        user = request.user
        company = Company.objects.filter(user_id=user.id)
        contents = Company_media.objects.filter(company=company[0].pk)
        capaings = Company_content.objects.filter(company=company[0].pk)

        if company:
            initial_data = {'company': company[0],}
        form = CampaingForm(initial=initial_data)
        form.fields["campaing"].queryset = Company_content.objects.filter(company=company[0].pk)
    data = {
        'form': form,
        'contents': contents,
    }
    return render_to_response('company_campaing_form.html', data,\
    context_instance=RequestContext(request))

@login_required
def Update_campaing_content(request, campaing_id):
    campaing = get_object_or_404(Campaing_media, pk=campaing_id)
    if request.method == 'POST':  # If the form has been submitted...
        form1 = CampaingForm(request.POST, instance=campaing)  # A form bound to the POST data
        if form1.is_valid():  # All validation rules pass
            form1.save()
            return redirect('company_campaing_detail',campaing.pk)
    else:
        form1 = CampaingForm(instance=campaing)
        contents = Company_media.objects.filter(company=campaing.company)
    data = {
        'form': form1,
        'contents': contents,
    }
    return render_to_response('company_campaing_update_form.html', data,\
    context_instance=RequestContext(request))