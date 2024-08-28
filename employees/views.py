from rest_framework.response import Response
from rest_framework import status, viewsets
from rest_framework.decorators import action
from .models import Employee, Review
from .serializers import EmployeeSerializer, ReviewSerializer
from django.shortcuts import get_object_or_404

class EmployeeViewSet(viewsets.GenericViewSet, viewsets.mixins.ListModelMixin, viewsets.mixins.CreateModelMixin, viewsets.mixins.UpdateModelMixin):
    serializer_class = EmployeeSerializer

    @action(detail=False, methods=['get'], url_path='(?P<identifier>[^/.]+)')
    def retrieve_employee(self, request, identifier=None, *args, **kwargs):
        """
        Retrieve an employee by ID, first name, or last name.
        """
        # Check if the identifier is numeric (i.e., an ID)
        if identifier.isdigit():
            employee = get_object_or_404(Employee, id=identifier)
        else:
            # Try to find an employee by first name or last name (case-insensitive)
            employee = Employee.objects.filter(first_name__iexact=identifier).first()
            if not employee:
                employee = Employee.objects.filter(last_name__iexact=identifier).first()

        serializer = self.get_serializer(employee)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=False, methods=['post'], url_path='create')
    def create_employee(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['put', 'patch'], url_path='update/(?P<identifier>\w+)')
    def update_employee(self, request, identifier=None, *args, **kwargs):
        if identifier.isdigit():
            # If identifier is a digit, filter by id
            employee = get_object_or_404(Employee, id=identifier)
        else:
            # If identifier is a string, filter by name (assuming unique name for simplicity)
            employee = get_object_or_404(Employee, first_name__iexact=identifier)

        partial = request.method == 'PATCH'
        serializer = self.get_serializer(employee, data=request.data, partial=partial)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @action(detail=False, methods=['delete'], url_path='delete/(?P<identifier>\w+)')
    def delete_employee(self, request, identifier=None, *args, **kwargs):
        if identifier.isdigit():
            # If the identifier is a digit, assume it's an ID
            employee = get_object_or_404(Employee, id=identifier)
        else:
            # If the identifier is a string, assume it's a name (unique name for simplicity)
            employee = get_object_or_404(Employee, first_name__iexact=identifier)

        employee.delete()
        return Response({'detail': 'Employee deleted successfully.'}, status=status.HTTP_204_NO_CONTENT)
    

class PerformanceReviewViewSet(viewsets.ModelViewSet):
    """
    A viewset for handling PerformanceReview models.

    Inherits from:
        - viewsets.ModelViewSet
    """
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def get_queryset(self):
        return Review.objects.all()
    
    def get_serializer(self, *args, **kwargs):
        return super().get_serializer(*args, **kwargs)
    
    def retrieve(self, request, pk=None, *args, **kwargs):
        """
        Retrieve a specific employee by ID.

        Args:
            request (Request): The HTTP request object.
            pk (str): The primary key of the employee.

        Returns:
            response (Response): The HTTP response object.
        """
        employee = get_object_or_404(Employee, id=pk)
        serializer = self.get_serializer(employee)
        return Response(serializer.data)
    
    def list(self, request, *args, **kwargs):
        """
        Retrieve all performance reviews.

        Args:
            request (Request): The HTTP request object.

        Returns:
            response (Response): The HTTP response object.
        """
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None, *args, **kwargs):
        """
        Retrieve a specific performance review by ID.

        Args:
            request (Request): The HTTP request object.
            pk (str): The primary key of the review.

        Returns:
            response (Response): The HTTP response object.
        """
    
        review = get_object_or_404(self.get_queryset(), pk=pk)
        serializer = self.get_serializer(review)
        return Response(serializer.data)

    def update(self, request, pk=None, *args, **kwargs):
        """
        Update a specific performance rev   iew by ID.

        Args:
            request (Request): The HTTP request object.
            pk (str): The primary key of the review.

        Returns:
            response (Response): The HTTP response object.
        """
        partial = kwargs.pop('partial', False)
        review = get_object_or_404(self.get_queryset(), pk=pk)
        serializer = self.get_serializer(review, data=request.data, partial=partial)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None, *args, **kwargs):
        """
        Delete a specific performance review by ID.

        Args:
            request (Request): The HTTP request object.
            pk (str): The primary key of the review.

        Returns:
            response (Response): The HTTP response object.
        """
        review = get_object_or_404(self.get_queryset(), pk=pk)
        review.delete()
        return Response({'detail': 'Review deleted successfully.'}, status=status.HTTP_204_NO_CONTENT)

    
