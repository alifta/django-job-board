from django.db import models


# Create your models here.
class JobPosting(models.Model):
    # id comes default starting at 1 and autoincrement
    title = models.CharField(max_length=100)
    description = models.TextField()
    company = models.CharField(max_length=100)
    salary = models.IntegerField()
    is_active = models.BooleanField(default=False)

    # run the following commands in terminal
    # (1)
    # python manage.py makemigrations
    # (2)
    # python manage.py migrate
    # (3) CRUD operations using
    # python manage.py shell
    # (4) add data to table
    # from job_board.models import JobPosting
    # JobPosting.objects.create(title="job posting 1", description="this is a great job", company="abc tech", salary=80000)
    # JobPosting.objects.create(title="software engineer", description="write great code", company="tech solution", salary=100000, is_active=True)
    # JobPosting.objects.create(title="marketing manager", description="create marketing campaigns", company="sunny tech", salary=90000, is_active=True)
