from django.contrib import admin
from .models import Project, Contact, Testimonial, Consult, Question

# Register your models here.
admin.site.register(Project)
admin.site.register(Contact)
admin.site.register(Testimonial)
admin.site.register(Consult)
admin.site.register(Question)
