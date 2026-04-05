from django.shortcuts import render, redirect, get_object_or_404
from .models import Word
from .forms import WordForm
from django.contrib import messages

def home(request):
    total_words = Word.objects.count()
    return render(request, 'home.html', {'total': total_words})

def word_list(request):
    all_words = Word.objects.all().order_by('word')  # сортировка по алфавиту
    return render(request, 'list.html', {'words': all_words, 'total': all_words.count()})

def add_word(request):
    if request.method == 'POST':
        form = WordForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Слово добавлено!')
            return redirect('list')
    else:
        form = WordForm()
    return render(request, 'form.html', {'form': form, 'title': 'Добавить слово'})

def edit_word(request, pk):
    word = get_object_or_404(Word, id=pk)
    if request.method == 'POST':
        form = WordForm(request.POST, request.FILES, instance=word)
        if form.is_valid():
            form.save()
            messages.success(request, 'Слово обновлено!')
            return redirect('list')
    else:
        form = WordForm(instance=word)
    return render(request, 'form.html', {'form': form, 'title': 'Редактировать слово'})

def quiz(request):
    words = Word.objects.all()
    result = None
    if request.method == 'POST':
        score = 0
        total = len(words)
        for word in words:
            user_answer = request.POST.get(f'answer_{word.id}')
            if user_answer and user_answer.lower().strip() == word.translation.lower():
                score += 1
        result = f'Правильно: {score} из {total}'
    return render(request, 'quiz.html', {'words': words, 'result': result})