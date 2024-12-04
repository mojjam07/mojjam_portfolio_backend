from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import Project, Contact, Testimonial, Consult, Question

class ProjectSerializer(ModelSerializer):
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = Project
        fields = ['title', 'description', 'technologies', 'github_link', 'image', 'image_url' ]
        read_only_field = ['created_at']
        
    def get_image_url(self, obj):
        request = self.context.get("request", None)
        if request and obj.image:
            return request.build_absolute_uri(obj.image.url)
        return None

class ContactSerializer(ModelSerializer):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']
        read_only_field = ['sent_at']

class TestimonialSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField() # Just added

    class Meta:
        model = Testimonial
        fields = ['id', 'name', 'testimonial', 'image', 'image_url', 'approved']
        read_only_fields = ['approved']  # Prevent approval field modification by users

    def get_image_url(self, obj):
        request = self.context.get("request", None)
        if request and obj.image:
            return request.build_absolute_uri(obj.image.url)
        return None
    
class ConsultSerializer(ModelSerializer):
    class Meta:
        model = Consult
        fields = '__all__'

class QuestionSerializer(ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'