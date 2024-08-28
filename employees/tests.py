
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Employee
from .models import Review

class EmployeeAPITestCase(APITestCase):
    def setUp(self):
        """
        Set up initial data for Employee tests.
        """
        self.employee_data = {
            "first_name": "John",
            "last_name": "Doe",
            "email": "john.doe@example.com",
            "contact_number": "1234567890",
            "contact_info": "123 Main St",
            "department": "Engineering",
            "birth_date": "1990-01-01",
            "hire_date": "2020-01-01"
        }
        self.employee = Employee.objects.create(**self.employee_data)
        self.create_url = reverse('employee-create')
        self.list_url = reverse('employee-list')
        self.detail_url = reverse('employee-retrieve', kwargs={'identifier': self.employee.id})
        self.update_url = reverse('employee-update', kwargs={'identifier': self.employee.id})
        self.delete_url = reverse('employee-delete', kwargs={'identifier': self.employee.id})

    def test_create_employee(self):
        """
        Ensure we can create a new Employee object.
        """
        new_employee_data = self.employee_data.copy()
        new_employee_data['email'] = 'jane.doe@example.com'  # Change the email
        response = self.client.post(self.create_url, new_employee_data, format='json')
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Employee.objects.count(), 2)

    def test_retrieve_employee(self):
       """ Ensure we can retrieve an employee by ID."""
       response = self.client.get(self.detail_url)
       self.assertEqual(response.status_code, status.HTTP_200_OK)
       self.assertEqual(response.data['first_name'], 'John')

    def test_list_employees(self):
        
        """ Ensure we can list all employees. """
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_update_employee(self):
        
       """Ensure we can update an existing employee."""
       updated_data = self.employee_data.copy()
       updated_data['first_name'] = 'Jane'
       response = self.client.put(self.update_url, updated_data, format='json')
       self.assertEqual(response.status_code, status.HTTP_200_OK)
       self.employee.refresh_from_db()
       self.assertEqual(self.employee.first_name, 'Jane')

    def test_delete_employee(self):
        
        """Ensure we can delete an employee."""
        
        response = self.client.delete(self.delete_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Employee.objects.count(), 0)


class PerformanceReviewAPITestCase(APITestCase):
    def setUp(self):
        # Initial setup remains the same...
        self.employee = Employee.objects.create(
            first_name="Jane",
            last_name="Doe",
            email="jane.doe@example.com",
            contact_number="0987654321",
            contact_info="456 Elm St",
            department="Sales",
            birth_date="1992-02-02",
            hire_date="2021-02-01"
        )
        self.review_data = {
            "employee": self.employee.id,
            "rating": 4,
            "comments": "Good performance"
        }
        self.review = Review.objects.create(employee=self.employee, rating=4, comments="Good performance")
        self.list_reviews_url = reverse('review-list')
        self.detail_review_url = reverse('review-detail', kwargs={'pk': self.review.id})

    def test_create_review(self):
        """
        Ensure we can create a new Review object.
        """
        response = self.client.post(self.list_reviews_url, self.review_data, format='json')
        print(response.status_code)  # Debugging: print the status code
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Review.objects.count(), 2)


"""   def test_retrieve_review(self):
  
        Ensure we can retrieve a review by ID.
    
        response = self.client.get(self.detail_review_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['rating'], 4)

    def test_list_reviews(self):
      
        Ensure we can list all reviews.
       
        response = self.client.get(self.list_reviews_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_update_review(self):
 
       Ensure we can update an existing review.
  
        updated_data = self.review_data.copy()
        updated_data['rating'] = 5
        response = self.client.put(self.detail_review_url, updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.review.refresh_from_db()
        self.assertEqual(self.review.rating, 5)

    def test_delete_review(self):
        
        Ensure we can delete a review.

        response = self.client.delete(self.detail_review_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Review.objects.count(), 0) """
