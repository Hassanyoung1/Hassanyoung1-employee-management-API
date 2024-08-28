from django.db import models

class Employee(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    contact_number = models.CharField(max_length=100)
    contact_info = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    birth_date = models.DateField()
    hire_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Review(models.Model):
    """
    Represents a review of an employee's performance.

    Attributes:
        employee (ForeignKey): The employee being reviewed.
        rating (int): The rating given to the employee (1 to 5).
        comments (str): Optional comments or feedback for the employee.
        created_at (datetime): The date and time when the review was created.
        updated_at (datetime): The date and time when the review was last updated.
    """

    RATING_CHOICES = [
        (1, 'Very Poor'),
        (2, 'Poor'),
        (3, 'Average'),
        (4, 'Good'),
        (5, 'Excellent'),
    ]

    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='reviews')
    rating = models.IntegerField(choices=RATING_CHOICES)
    comments = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        """
        Returns a string representation of the review object.
        
        The string representation consists of the employee's name and the review rating.
        
        Returns:
            str: The string representation of the review object.
        """
        return f"Review for {self.employee} - Rating: {self.rating}"
