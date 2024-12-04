from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technologies = models.CharField(max_length=200)
    github_link = models.URLField(blank=True, null=True)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name}"
    
class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    testimonial = models.TextField()
    image = models.ImageField(upload_to='testimonial_pics/', blank=True, null=True)
    approved = models.BooleanField(null=True, default=False)

    def __str__(self):
        return self.name

class Consult(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    service_type = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"New consult from {self.name} on {self.date}"
    
class Question(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    question = models.TextField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"A new question from {self.name}"

class Images(models.Model):
    name = models.CharField(max_length=100)
    image_data = models.BinaryField(null=True, blank=True)

    def __str__(self):
        return f"{self.name}"

