from django.shortcuts import render

def index(request):
    return render(request, 'scanner/index.html')

import base64
from io import BytesIO
from PIL import Image
from django.http import JsonResponse

# Placeholder function for ML model
def identify_fruit(image):
    # Replace this function with actual ML model integration
    return {
        "name": "Apple",
        "health_benefits": "Rich in fiber and vitamins.",
        "common_location": "Found globally in temperate climates.",
    }

def camera_scan(request):
    if request.method == 'POST':
        # Get the image data from the POST request
        image_data = request.POST.get('image')
        
        if image_data:
            try:
                # Decode the Base64 image
                format, imgstr = image_data.split(';base64,')  # Ensure correct format splitting
                image = Image.open(BytesIO(base64.b64decode(imgstr)))

                # Use the placeholder ML function to identify the fruit
                result = identify_fruit(image)

                # Render the results
                return render(request, 'scanner/result.html', {'result': result})

            except Exception as e:
                # Handle any errors with image decoding
                return JsonResponse({'error': str(e)}, status=400)

    return render(request, 'scanner/camera.html')


