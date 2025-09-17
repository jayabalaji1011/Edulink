import os
import sys

# Add the project directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Set up Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Assignment.settings")
import django
django.setup()

from django.contrib.auth.models import User
from Edulink.models import Assignment  # Ensure this is correct

admin_user = User.objects.filter(username='edulink').first()  # Update to the correct username
actual_user = User.objects.filter(username='balaji').first()  # Update to the correct username


if not admin_user or not actual_user:
    print('One or both users do not exist.')
else:
    updated_count = Assignment.objects.filter(created_by=admin_user).update(created_by=actual_user)
    print(f'{updated_count} assignments updated successfully!')
