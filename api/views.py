from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListAPIView
from .models import Project, Contact, Testimonial, Consult, Question
from .serializers import ProjectSerializer, ContactSerializer, TestimonialSerializer, ConsultSerializer, QuestionSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import status
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny
from django.http import JsonResponse

def home(request):
    return JsonResponse({"message": "Welcome to Mojjam Resume Backend API!"})

# class ProjectViewSet(ModelViewSet):
#     queryset = Project.objects.all()
#     serializer_class = ProjectSerializer
#     # permission_classes = [IsAuthenticatedOrReadOnly]

class ProjectListView(APIView):
    def post(self, request):
        serializer = ProjectSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()  # Save the contact message to the database
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def get(self, request):
        contacts = Project.objects.all()  # Query all contact messages
        serializer = ProjectSerializer(contacts, many=True, context={'request': request})  # Serialize the queryset
        return Response(serializer.data, status=status.HTTP_200_OK)  # Return serialized data

# class ContactViewSet(ModelViewSet):
#     queryset = Contact.objects.all()
#     serializer_class = ContactSerializer
#     permission_classes = [AllowAny]

#     def get_queryset(self):
#         # Optional: Limit query logic or provide filtered data
#         return super().get_queryset()

class ContactListView(APIView):
    def post(self, request):
        serializer = ContactSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()  # Save the contact message to the database
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def get(self, request):
        contacts = Contact.objects.all()  # Query all contact messages
        serializer = ContactSerializer(contacts, many=True)  # Serialize the queryset
        return Response(serializer.data, status=status.HTTP_200_OK)  # Return serialized data

# class ApprovedTestimonialListView(ListAPIView):
#     queryset = Testimonial.objects.filter(approved=True).only('name', 'testimonial', 'profile_picture')
#     serializer_class = TestimonialSerializer


# class SubmitTestimonialView(APIView):
#     parser_classes = (MultiPartParser, FormParser)

#     def post(self, request, *args, **kwargs):
#         try:
#             serializer = TestimonialSerializer(data=request.data)
#             if serializer.is_valid():
#                 serializer.save(approved=False)  # Default to not approved
#                 return Response(
#                     {"success": "Testimonial submitted and awaiting approval."},
#                     status=status.HTTP_201_CREATED,
#                 )
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#         except Exception as e:
#             return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class TestimonialListView(APIView):
    parser_classes = [MultiPartParser, FormParser]

    def get(self, request):
        # Filter testimonials where approved=True
        testimonials = Testimonial.objects.filter(approved=True)
        serializer = TestimonialSerializer(testimonials, many=True, context={'request': request})
        return Response(serializer.data)

    def post(self, request):
        serializer = TestimonialSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


class ConsultViewSet(ModelViewSet):
    queryset = Consult.objects.all()
    serializer_class = ConsultSerializer

class QuestionViewSet(ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer