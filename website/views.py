from django.shortcuts import render
from django.contrib import messages
from .models import ContactMessage
from pathlib import Path
from django.shortcuts import render
from django.contrib.staticfiles import finders


def home(request):
    return render(request, 'website/index.html')

def about(request):
    return render(request, 'website/about-us.html')

# def authdistributor(request):
#     return render(request, 'website/authorised-distributor.html')

def partnerclients(request):
    return render(request, 'website/partner-clients.html')

# def products(request):
#     return render(request, 'website/products.html')




def products(request):
    categories = [
        {
            "name": "Mechanical & Automation",
            "slug": "mechanical",
            "folder": "mechanical",
        },
        {
            "name": "Pressure Measurement",
            "slug": "pressure",
            "folder": "pressure",
        },
        {
            "name": "Temperature Measurement",
            "slug": "temperature",
            "folder": "temperature",
        },
        {
            "name": "Flow Measurement",
            "slug": "flow",
            "folder": "flow",
        },
        {
            "name": "Level Measurement",
            "slug": "level",
            "folder": "level",
        },
        
        
    ]

    products = []
    
    allowed_extensions = [".webp"]

    base_static_path = finders.find("website/images/products")

    if base_static_path:
        base_path = Path(base_static_path)

        for category in categories:
            folder_path = base_path / category["folder"]

            if folder_path.exists():
                for image_file in sorted(folder_path.iterdir()):
                    if image_file.suffix.lower() in allowed_extensions:
                        product_title = image_file.stem.replace("-", " ").replace("_", " ").title()

                        products.append({
                            "title": product_title,
                            "category": category["slug"],
                            "category_name": category["name"],
                            "image": f"website/images/products/{category['folder']}/{image_file.name}",
                            "alt": f"{product_title} - {category['name']}",
                        })

    return render(request, "website/products.html", {
        "categories": categories,
        "products": products,
    })





def contactus(request):
    if request.method == "POST":
        name = request.POST.get("your_name")
        phone_number = request.POST.get("phone_number")
        email = request.POST.get("your_email")
        message = request.POST.get("your_message")

        ContactMessage.objects.create(
            name=name,
            phone_number=phone_number,
            email=email,
            message=message
        )

        messages.success(request, "Thank you! Your message has been sent successfully.")
        return render(request, "website/contact-us.html")

    return render(request, "website/contact-us.html")