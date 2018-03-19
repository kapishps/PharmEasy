from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect
from django.urls import reverse
from django.views.generic.detail import DetailView
from django.utils import timezone

from PEapp.models import Prescription, MedicalRecord, MyUser,Approval
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
    if request.user.user_type == "P":
        context["pending_approvals"] = Approval.objects.filter(status="PE", prescription_no__user=request.user)
    else:
        context["approved_prescriptions"] = Prescription.objects.filter(approval__requester=request.user,approval__status="AP")
        context["pending_prescriptions"] = Prescription.objects.filter(approval__requester=request.user,approval__status="PE")
        context["available_prescriptions"] = Prescription.objects.filter(Q(approval__isnull=True)) | Prescription.objects.filter(~Q(approval__requester=request.user))
    return render(request, context=context, template_name="index.html")


# @login_required(login_url="login/")
class PrescriptionDetailView(DetailView):
    model = Prescription
    template_name = 'prescription.html'

    def get_context_data(self, **kwargs):
        context = super(PrescriptionDetailView, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


class MedicalRecordDetailView(DetailView):
    model = MedicalRecord
    template_name = 'medical_rec.html'

    def get_context_data(self, **kwargs):
        context = super(MedicalRecordDetailView, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


@login_required(login_url="login/")
def create_approval(request):
    user_id = request.POST['user']
    requester = MyUser.objects.get(id=user_id)
    prescription_id = request.POST['prescription']
    prescription = Prescription.objects.get(id=prescription_id)
    Approval.objects.create(requester=requester, prescription_no=prescription)
    return HttpResponseRedirect(reverse('home'))


@login_required(login_url="login/")
def approve_approval(request):
    approval_id = request.POST['approval_id']
    approval = Approval.objects.get(id = approval_id)
    user_id = request.POST['user']
    user = MyUser.objects.get(id=user_id)
    if approval.prescription_no.user.user_name == user.user_name:
        approval.status = 'AP'
        approval.save()
    return HttpResponseRedirect(reverse('home'))

