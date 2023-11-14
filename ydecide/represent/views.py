from django.shortcuts import render


def page_not_found_view(request, exception):
    return render(request, 'represent/404.html', status=404)


def main(request):
    # include news and teachers
    template_name = 'main.html'
    context = {

    }
    return render(request, 'represent/main.html', context=context)


def news(request):
    # include news and teachers
    template_name = 'news.html'
    context = {

    }
    return render(request, 'represent/news.html', context=context)


def lesson_schedule(request):
    # include news and teachers
    template_name = 'lesson_schedule.html'
    context = {

    }
    return render(request, 'represent/lesson_schedule.html', context=context)
