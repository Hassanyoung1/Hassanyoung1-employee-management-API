import os
import django

# Set up Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "employee_management.settings")
django.setup()

from employees.models import Employee
from django.db.models import Count

# Find all email addresses that are duplicated
duplicates = Employee.objects.values('email').annotate(email_count=Count('email')).filter(email_count__gt=1)

for duplicate in duplicates:
    email = duplicate['email']
    employees = Employee.objects.filter(email=email)
    # Delete all but the first entry
    employees.exclude(id=employees.first().id).delete()

print("Successfully removed duplicate emails")
