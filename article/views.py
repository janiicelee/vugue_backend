import json

from django.views  import View
from django.http   import JsonResponse

from .models     import Categories, Video
from user.models import User
from user.utils  import login_decorator

class VideoView(View):
    def get(self, request):
        videos = Video.objects.select_related('category')
        result = [{
                'id': video.id,
                'title':video.title,
                'background_image':video.background_image,
                'content':video.content,
                'video_url':video.video_url,
                'category':video.category.name
                } for video in videos]
        return JsonResponse({'result':result}, status = 200)




