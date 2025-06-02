from django.shortcuts import render
from .forms import SubmissionForm


def submit_request(request):
    print(request)
    if request.method == 'POST':
        form = SubmissionForm(request.POST)
        if form.is_valid():
            submission = form.save()
            return render(request, 'submission_result.html', {'submission': submission})
    else:
        form = SubmissionForm()
    return render(request, 'submission_form.html', {'form': form})

