# **Resume Processor API**

This project is a Django-based REST API designed to extract basic information such as the candidate's first name, email, and mobile number from a resume file (PDF or Word). The API endpoint accepts a resume file and returns the extracted information in a structured format.

---

## **Project Setup**

To set up this project locally, follow these steps:

### **1. Clone the Repository**
```bash
git clone https://github.com/prakharrrt/Resume-Processor.git
```
### **2. Set up virtual Environment**
```bash
python -m venv env
.\env\Scripts\activate
```

### **3. Install Dependencies**
```bash
pip install -r requirements.txt
```

### **4. Database Configuration**
PostgreSQL Setup
You need to set up a PostgreSQL database. Create a new database and user for this project.

Update .env File In the root directory of the project, create a .env file and add your database credentials:
```bash
DB_NAME=your_database_name
DB_USER=your_database_user
DB_PASSWORD=your_database_password
DB_HOST=localhost
DB_PORT=5432
```

Run Migrations
Apply the migrations to create the necessary database tables:
```bash
python manage.py migrate
```

### **5. Running the application locally**
Start the Django Development Server:
```bash
python manage.py runserver
```

### **6. Testing the API Endpoint**
API Endpoint:
``` bash
POST http://127.0.0.1:8000/api/extract_resume/
```

Request Body:
Set the request type to POST. In the "Body" tab, choose form-data. Add a key file (make sure the type is set to "File"). Upload a .pdf or .docx file containing the candidate's resume.

Expected Response:
Upon successful extraction, you will receive a JSON response with the candidate’s information:

```bash
{
    "first_name": "John",
    "email": "john.doe@example.com",
    "mobile_number": "123-456-7890"
}
```


![image](https://github.com/user-attachments/assets/5917700c-d211-4a4d-8df0-651c352b2812)


