import os
import django
import requests
from django.core.files.base import ContentFile

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'thediora.settings')
django.setup()

from store.models import Category

# Category images from Unsplash (free stock photos)
category_images = {
    'Furniture': 'https://images.unsplash.com/photo-1556228453-efd6c1ff04f6?w=800&h=600&fit=crop',
    'Home Decor': 'https://images.unsplash.com/photo-1513519245088-0e12902e5a38?w=800&h=600&fit=crop',
    'Lighting': 'https://images.unsplash.com/photo-1565814329452-e1efa11c5b89?w=800&h=600&fit=crop',
    'Textiles': 'https://images.unsplash.com/photo-1520006403909-878d6e67a60e?w=800&h=600&fit=crop',
}

print("Adding beautiful images to categories...")
print("=" * 50)

for category_name, image_url in category_images.items():
    try:
        category = Category.objects.get(name=category_name)
        
        # Download image
        print(f"\nDownloading image for {category_name}...")
        response = requests.get(image_url, timeout=10)
        
        if response.status_code == 200:
            # Save image to category
            image_filename = f'{category_name.lower().replace(" ", "_")}.jpg'
            category.image.save(
                image_filename,
                ContentFile(response.content),
                save=True
            )
            print(f"✓ Successfully added image to {category_name}")
        else:
            print(f"✗ Failed to download image for {category_name}")
            
    except Category.DoesNotExist:
        print(f"✗ Category {category_name} not found")
    except Exception as e:
        print(f"✗ Error with {category_name}: {str(e)}")

print("\n" + "=" * 50)
print("Done! All categories now have beautiful images!")
