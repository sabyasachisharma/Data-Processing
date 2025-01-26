# File Management Django App

This Django application is designed for efficient file management, including features like file upload, download, data preview, search, and pagination. It supports multiple file formats and ensures a user-friendly experience with robust validation mechanisms.

## Project Overview

### Features

- **File Upload**: Upload multiple files simultaneously with validation for file type and size.
- **File Download**: Securely download uploaded files.
- **Data Preview**: Preview the first 10 rows of CSV files in a structured table.
- **Search**: Search for specific content in the uploaded CSV files.
- **Pagination**: Navigate through large datasets using pagination.
- **Validation**:
  - Supported file types: CSV, Excel, and PDF.
  - File size restriction (default: 5 MB).
- **Responsive Dashboard**: View uploaded files and manage data efficiently.

---

## Requirements

- Python 3.8+
- Django 4.0+
- pandas library

---

## Installation and Setup

### Step 1: Clone the Repository

```bash
git clone https://github.com/sabyasachisharma/Data-Processing.git
cd Data-Processing
```

### Step 2: Create a Virtual Environment

```bash
python -m venv venv
```

### Step 3: Activate the Virtual Environment

- **Windows**:
  ```bash
  venv\Scripts\activate
  ```
- **macOS/Linux**:
  ```bash
  source venv/bin/activate
  ```

### Step 4: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 5: Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### Step 6: Run the Development Server

```bash
python manage.py runserver
```

---

## Usage

### File Upload
1. Navigate to `/file/upload/`.
2. Select one or more files and click "Upload".

### Dashboard
1. Navigate to `/file/dashboard/`.
2. View uploaded files along with metadata.
3. Preview the first 10 rows of the most recent CSV file.
4. Use the search bar to filter data.
5. Navigate through paginated rows using "Previous" and "Next" links.

### File Download
1. Navigate to `/file/dashboard/`.
2. Click the "Download" button next to the desired file.

---

## Directory Structure

The project follows a modular structure for maintainability and scalability:

```
file_app/
├── templates/
│   ├── file_manager/
│   │   ├── upload.html
│   │   └── dashboard.html
├── static/
├── media/
├── views/
│   ├── upload_views.py
│   └── dashboard_views.py
├── urls/
│   └── file_urls.py
├── tests/
│   └── test_file_app.py
```

---

## Key Changes

### 1. Validation Enhancements
- File type validation: Only CSV, Excel, and PDF are allowed.
- File size validation: Restricted to files below 5 MB.

### 2. Dashboard Features
- Added pagination for CSV previews.
- Implemented a search bar to filter rows dynamically.

### 3. Multiple File Upload
- Support for uploading multiple files simultaneously.

### 4. Improved Structure
- Modularized views and URLs for better organization.

---

## Testing

Run the following command to ensure the application works as expected:

```bash
python manage.py test
```
