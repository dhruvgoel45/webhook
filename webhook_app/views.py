from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .models import Webhook
import json
from django.shortcuts import get_object_or_404

@csrf_exempt
def webhook_view(request, unique_id):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))

        name = data.get('name')
        email = data.get('email')
        phone = data.get('phone')

        if name and email and phone:
            webhook, created = Webhook.objects.get_or_create(unique_id=unique_id, defaults={
                'name': name,
                'email': email,
                'phone': phone,
                'job_title': data.get('job_title'),
                'address': data.get('address'),
                'best_time_to_connect': data.get('best_time_to_connect'),
                'project_interest': data.get('project_interest'),
                'alternative_number': data.get('alternative_number'),
                'project': data.get('project'),
            })

            return JsonResponse({'message': 'Webhook created/updated successfully.'})
        else:
            return JsonResponse({'message': 'Name, email, and phone are required.'}, status=400)

    elif request.method == 'GET':
        webhook = get_object_or_404(Webhook, unique_id=unique_id)
        data = {
            'name': webhook.name,
            'email': webhook.email,
            'phone': webhook.phone,
            'job_title': webhook.job_title,
            'address': webhook.address,
            'best_time_to_connect': webhook.best_time_to_connect,
            'project_interest': webhook.project_interest,
            'alternative_number': webhook.alternative_number,
            'project': webhook.project,
        }
        return JsonResponse(data)


    return JsonResponse({'message': 'Invalid request method.'}, status=405)
