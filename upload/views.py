# upload/views.py
import xml.etree.ElementTree as Et
from django.shortcuts import render
from django.http import JsonResponse
from .forms import UploadFileForm
from .models import Ad

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            xml_file = request.FILES['xml_file']
            try:
                tree = Et.parse(xml_file)
                root = tree.getroot()
                for ad_elem in root.findall('ad'):
                    title = ad_elem.find('title').text
                    price = ad_elem.find('price').text
                    address = ad_elem.find('address').text
                    area = ad_elem.find('area').text
                    link = ad_elem.find('link').text
                    date = ad_elem.find('date').text

                    # Проверка на дубликаты
                    if not Ad.objects.filter(link=link).exists():
                        Ad.objects.create(
                            title=title,
                            price=price,
                            address=address,
                            area=area,
                            link=link,
                            date=date
                        )
                return JsonResponse({'status': 'success'})
            except Exception as e:
                return JsonResponse({'status': 'error', 'message': str(e)})
        else:
            return JsonResponse({'status': 'error', 'message': 'Invalid form data'})
    else:
        form = UploadFileForm()
    return render(request, 'upload/upload.html', {'form': form})