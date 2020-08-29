from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from tweets.models import Tweet


def home_page(request):
    return render(request, "pages/home.html")


def tweet_list_view(request, *args, **kwargs):
    qs = Tweet.objects.all()

    tweet_list = [{"id": x.id, "content":x.content} for x in qs]

    data = {
    'response': tweet_list
    }
    return JsonResponse(data)

def tweet_detail_view(request,tweet_id):
    data = {
        "id": tweet_id
    }
    status = 200

    try:
        obj = Tweet.objects.get(id=tweet_id)
        data["content"] = obj.content

    except:

        data["message"] = "Page does not exist"

        status = 404

    return JsonResponse(data, status=status)
