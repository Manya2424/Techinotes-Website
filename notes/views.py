from django.shortcuts import render
from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from home.forms import NoteForm
from django.contrib import messages
from home.models import Note
from django.core.paginator import Paginator
# Create your views here.

@login_required
def create_note(request):

    if request.method == 'POST':
        form = NoteForm(request.POST)

        if form.is_valid():
            note = form.save(commit=False)
            note.user = request.user
            note.save()
            messages.success(request,"Note Created")
            return redirect('notes')

    else:
        form = NoteForm()

    return render(request, 'create_note.html', {'form': form})


@login_required
def notes(request):
    
    note_list = Note.objects.filter(
        user=request.user
    ).order_by('-created_at')

    paginator = Paginator(note_list, 4)

    page_number = request.GET.get('page')

    notes = paginator.get_page(page_number)

    return render(
        request,
        'notes.html',
        {'notes': notes}
    )
@login_required
def edit_note(request, note_id):
    note = get_object_or_404(Note, id=note_id)

    if request.method == "POST":
        note.title = request.POST.get("title")
        note.content = request.POST.get("content")
        note.save()
        messages.success(request,"Note Updated")
        return redirect('notes')   

    return render(request, 'edit_note.html', {'note': note})

@login_required
def delete_note(request, note_id):
    note = get_object_or_404(Note, id=note_id, user=request.user)
    note.delete()
    messages.success(request,"Note Deleted")
    return redirect('notes')



@login_required
def search_notes(request):

    query = request.GET.get('q')

    results = []

    if query:
        results = Note.objects.filter(
            title__icontains=query,
            user=request.user
        )

    return render(
        request,
        'search_results.html',
        {
            'query': query,
            'results': results
        }
    )
