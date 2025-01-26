from django.db import models

class UploadedFile(models.Model):
    file = models.FileField(upload_to='uploaded_files/')  # File upload path
    uploaded_at = models.DateTimeField(auto_now_add=True)  # Timestamp of upload

    def __str__(self):
        return self.file.name  # Return the file name as a string representation
