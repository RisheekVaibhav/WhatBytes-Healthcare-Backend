from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from .models import Mapping
from .serializers import MappingSerializer
from doctors.serializers import DoctorSerializer


class MappingViewSet(viewsets.ModelViewSet):
    queryset = Mapping.objects.all()
    serializer_class = MappingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def retrieve(self, request, pk=None):
        # spec treats this id as patient_id, returns all doctors assigned to that patient
        mappings = Mapping.objects.filter(patient_id=pk)
        doctors = [m.doctor for m in mappings]
        serializer = DoctorSerializer(doctors, many=True)
        return Response(serializer.data)