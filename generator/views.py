from django.http import JsonResponse
from django.views.decorators.http import require_GET
import secrets
import string

@require_GET
def generate_password_view(request):
	try:
		length = int(request.GET.get('length', 12))
		if length < 1 or length > 128:
			return JsonResponse({'error': 'Password length must be between 1 and 128.'}, status=400)
	except (TypeError, ValueError):
		return JsonResponse({'error': 'Invalid length parameter.'}, status=400)

	alphabet = string.ascii_letters + string.digits + string.punctuation
	password = ''.join(secrets.choice(alphabet) for _ in range(length))
	return JsonResponse({'password': password})
