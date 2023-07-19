from djongo import models

class Webhook(models.Model):
    unique_id = models.CharField(max_length=255, primary_key=True)  # Make unique_id the primary key
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    job_title = models.CharField(max_length=255, blank=True)
    address = models.TextField(blank=True)
    best_time_to_connect = models.CharField(max_length=255, blank=True)
    project_interest = models.TextField(blank=True)
    alternative_number = models.CharField(max_length=20, blank=True)
    project = models.TextField(blank=True)

    def __str__(self):
        return self.name
