from django.shortcuts import render_to_response
from django.template import RequestContext
from forms import NewCaseForm
from models import SuccessCase


def all_cases(request):
    all_success_cases = SuccessCase.objects.all()
    return render_to_response(
        'success_cases/all_cases.html',
        {'all_success_cases': all_success_cases},
        context_instance=RequestContext(request),
    )

    
def new_case(request):
    form = NewCaseForm()
    if request.method == 'POST':
        form = NewCaseForm(request.POST)
        if form.is_valid():
            success_case = form.save()
            return render_to_response(
                'success_cases/case_submited.html',
                context_instance = RequestContext(request)
            )
            
    return render_to_response(
        'success_cases/new_case.html',
        {'form': form},
        context_instance=RequestContext(request),
    )
