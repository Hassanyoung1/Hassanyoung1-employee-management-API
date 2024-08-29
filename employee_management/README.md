Here's an API documentation for the provided code, which includes endpoints for managing employees and performance reviews. The documentation details the HTTP methods, URLs, request parameters, and response formats.

---

## Employee Management API

### 1. Create an Employee

**Endpoint**: `/api/v1/employees/create/`  
**Method**: `POST`  
**Description**: Creates a new employee record in the database.

**Request Body**:
```json
{
  "first_name": "John",
  "last_name": "Doe",
  "email": "john.doe@example.com",
  "contact_number": "123-456-7890",
  "contact_info": "123 Street, City",
  "department": "Engineering",
  "birth_date": "1990-01-01",
  "hire_date": "2020-01-01"
}
```

**Response**:
- **201 Created**: Returns the created employee object.
  ```json
  {
    "id": 1,
    "first_name": "John",
    "last_name": "Doe",
    "email": "john.doe@example.com",
    "contact_number": "123-456-7890",
    "contact_info": "123 Street, City",
    "department": "Engineering",
    "birth_date": "1990-01-01",
    "hire_date": "2020-01-01",
    "created_at": "2024-08-27T10:00:00Z",
    "updated_at": "2024-08-27T10:00:00Z",
    "reviews": []
  }
  ```
- **400 Bad Request**: If the input data is invalid.

---

### 2. Retrieve an Employee

**Endpoint**: `/api/v1/employees/{identifier}/`  
**Method**: `GET`  
**Description**: Retrieves an employee by ID, first name, or last name.

**Path Parameter**:
- `identifier`: Can be the employee's ID (integer), first name, or last name (string).

**Response**:
- **200 OK**: Returns the employee object.
  ```json
  {
    "id": 1,
    "first_name": "John",
    "last_name": "Doe",
    "email": "john.doe@example.com",
    "contact_number": "123-456-7890",
    "contact_info": "123 Street, City",
    "department": "Engineering",
    "birth_date": "1990-01-01",
    "hire_date": "2020-01-01",
    "created_at": "2024-08-27T10:00:00Z",
    "updated_at": "2024-08-27T10:00:00Z",
    "reviews": []
  }
  ```
- **404 Not Found**: If no employee matches the given identifier.

---

### 3. List All Employees

**Endpoint**: `/api/v1/employees/`  
**Method**: `GET`  
**Description**: Retrieves a list of all employees.

**Response**:
- **200 OK**: Returns a list of all employee objects.
  ```json
  [
    {
      "id": 1,
      "first_name": "John",
      "last_name": "Doe",
      "email": "john.doe@example.com",
      "contact_number": "123-456-7890",
      "contact_info": "123 Street, City",
      "department": "Engineering",
      "birth_date": "1990-01-01",
      "hire_date": "2020-01-01",
      "created_at": "2024-08-27T10:00:00Z",
      "updated_at": "2024-08-27T10:00:00Z",
      "reviews": []
    },
    {
      "id": 2,
      "first_name": "Jane",
      "last_name": "Smith",
      "email": "jane.smith@example.com",
      "contact_number": "123-456-7890",
      "contact_info": "123 Street, City",
      "department": "HR",
      "birth_date": "1985-05-15",
      "hire_date": "2018-06-01",
      "created_at": "2024-08-27T10:00:00Z",
      "updated_at": "2024-08-27T10:00:00Z",
      "reviews": []
    }
  ]
  ```

---

### 4. Update an Employee

**Endpoint**: `/api/v1/employees/{identifier}/update/`  
**Method**: `PUT`, `PATCH`  
**Description**: Updates an employee's details by ID, first name, or last name.

**Path Parameter**:
- `identifier`: Can be the employee's ID (integer), first name, or last name (string).

**Request Body** (example):
```json
{
  "department": "Marketing"
}
```

**Response**:
- **200 OK**: Returns the updated employee object.
- **400 Bad Request**: If the input data is invalid.
- **404 Not Found**: If no employee matches the given identifier.

---

### 5. Delete an Employee

**Endpoint**: `/api/v1/employees/delete/{identifier}/`  
**Method**: `DELETE`  
**Description**: Deletes an employee by ID, first name, or last name.

**Path Parameter**:
- `identifier`: Can be the employee's ID (integer), first name, or last name (string).

**Response**:
- **204 No Content**: Successfully deleted the employee.
- **404 Not Found**: If no employee matches the given identifier.

---

## Performance Review Management API

### 1. List All Performance Reviews

**Endpoint**: `/api/v1/employees/reviews/`  
**Method**: `GET`  
**Description**: Retrieves a list of all performance reviews.

**Response**:
- **200 OK**: Returns a list of all review objects.
  ```json
  [
    {
      "id": 1,
      "employee": 1,
      "rating": 5,
      "comments": "Excellent performance!",
      "created_at": "2024-08-27T10:00:00Z",
      "updated_at": "2024-08-27T10:00:00Z"
    },
    {
      "id": 2,
      "employee": 2,
      "rating": 3,
      "comments": "Average performance.",
      "created_at": "2024-08-27T10:00:00Z",
      "updated_at": "2024-08-27T10:00:00Z"
    }
  ]
  ```

---

### 2. Retrieve a Performance Review

**Endpoint**: `/api/v1/employees/reviews/{pk}/`  
**Method**: `GET`  
**Description**: Retrieves a performance review by its primary key (ID).

**Path Parameter**:
- `pk`: The primary key (ID) of the review.

**Response**:
- **200 OK**: Returns the review object.
  ```json
  {
    "id": 1,
    "employee": 1,
    "rating": 5,
    "comments": "Excellent performance!",
    "created_at": "2024-08-27T10:00:00Z",
    "updated_at": "2024-08-27T10:00:00Z"
  }
  ```
- **404 Not Found**: If no review matches the given ID.

---

### 3. Create a Performance Review

**Endpoint**: `/api/v1/employees/reviews/`  
**Method**: `POST`  
**Description**: Creates a new performance review for an employee.

**Request Body**:
```json
{
  "employee": 1,
  "rating": 4,
  "comments": "Good performance."
}
```

**Response**:
- **201 Created**: Returns the created review object.
- **400 Bad Request**: If the input data is invalid.

---

### 4. Update a Performance Review

**Endpoint**: `/api/v1/employees/reviews/{pk}/`  
**Method**: `PUT`, `PATCH`  
**Description**: Updates a specific performance review by its primary key (ID).

**Path Parameter**:
- `pk`: The primary key (ID) of the review.

**Request Body** (example):
```json
{
  "rating": 4
}
```

**Response**:
- **200 OK**: Returns the updated review object.
- **400 Bad Request**: If the input data is invalid.
- **404 Not Found**: If no review matches the given ID.

---

### 5. Delete a Performance Review

**Endpoint**: `/api/v1/employees/reviews/{pk}/`  
**Method**: `DELETE`  
**Description**: Deletes a specific performance review by its primary key (ID).

**Path Parameter**:
- `pk`: The primary key (ID) of the review.

**Response**:
- **204 No Content**: Successfully deleted the review.
- **404 Not Found**: If no review matches the given ID.

---

### Notes
- **Error Handling**: All endpoints will return appropriate HTTP status codes and messages in the event of an error, such as `400 Bad Request` for invalid input, `404 Not Found` for non-existent resources, and `204 No Content` for successful deletions.
- **Authentication and Authorization**: Depending on your application's settings, authentication and authorization may be