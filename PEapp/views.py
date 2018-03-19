from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect
from django.urls import reverse
from django.views.generic.detail import DetailView
from django.utils import timezone

from PEapp.models import Prescription, MedicalRecord, MyUser
from PEapp.admin import UserCreationForm
from django.contrib.auth import login, authenticate

# Create your views here.

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('user_name')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

@login_required(login_url="login/")
def home(request):
    context = {}
    # if request.user.user_type == "PA":
    #     context["pending_approvals"] = Approval.objects.filter(status="PE", prescription__user=request.user)
    # else:
    #     context["approved_prescriptions"] = Prescription.objects.filter(approval__user=request.user,
    #                                                                     approval__status="AP")
    #     context["pending_prescriptions"] = Prescription.objects.filter(approval__user=request.user,
    #                                                                    approval__status="PE")
    #     context["rejected_prescriptions"] = Prescription.objects.filter(approval__user=request.user,
    #                                                                     approval__status="RE")
    #     context["available_prescriptions"] = Prescription.objects.filter(
    #         Q(approval__isnull=True)) | Prescription.objects.filter(~Q(approval__user=request.user))
    return render(request, context=context, template_name="index.html")


class PrescriptionDetailView(DetailView):
    model = Prescription
    template_name = 'prescription_detail.html'

    def get_context_data(self, **kwargs):
        context = super(PrescriptionDetailView, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


class MedicalRecordDetailView(DetailView):
    model = MedicalRecord
    template_name = 'medicalrecord_detail.html'

    def get_context_data(self, **kwargs):
        context = super(MedicalRecordDetailView, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context
