from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.paginator import Paginator
from .models import UploadedFile
import pandas as pd

# Allowed file extensions
ALLOWED_EXTENSIONS = ['.csv', '.xlsx', '.pdf']

# Maximum file size in MB
MAX_FILE_SIZE_MB = 5


def file_upload(request):
    """
    Handle file uploads with validation for type and size.
    Supports multiple file uploads.
    """
    if request.method == 'POST':
        files = request.FILES.getlist('file')
        for uploaded_file in files:
            # File type validation
            if not any(uploaded_file.name.endswith(ext) for ext in ALLOWED_EXTENSIONS):
                return HttpResponse("Unsupported file type.", status=400)

            # File size validation
            if uploaded_file.size > MAX_FILE_SIZE_MB * 1024 * 1024:
                return HttpResponse(f"File too large. Max size is {MAX_FILE_SIZE_MB} MB.", status=400)

            # Save the file
            UploadedFile.objects.create(file=uploaded_file)

        return redirect('file_dashboard')

    return render(request, 'file_manager/upload.html')


def file_dashboard(request):
    """
    Display all uploaded files and preview the latest file's data with pagination.
    Includes search functionality for CSV files.
    """
    files = UploadedFile.objects.all()
    search_query = request.GET.get('search', '')
    data = []

    if files.exists():
        latest_file = files.last()
        file_path = latest_file.file.path

        # Preview CSV data
        if latest_file.file.name.endswith('.csv'):
            df = pd.read_csv(file_path)

            # Search functionality
            if search_query:
                df = df[df.apply(lambda row: row.astype(str).str.contains(search_query).any(), axis=1)]

            # Convert to dictionary for rendering
            data = df.to_dict(orient='records')

    # Pagination
    paginator = Paginator(data, 10)  # 10 rows per page
    page_number = request.GET.get('page')
    page_data = paginator.get_page(page_number)

    return render(request, 'file_manager/dashboard.html', {'files': files, 'data': page_data})


def file_download(request, file_id):
    """
    Handle file downloads by serving the selected file.
    """
    file_obj = UploadedFile.objects.get(id=file_id)
    response = HttpResponse(file_obj.file, content_type='application/octet-stream')
    response['Content-Disposition'] = f'attachment; filename={file_obj.file.name}'
    return response
