from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .serializers import McfCarBrandCreateSerializer
from avto_cc.models import mcfcarbrand

class McfCarBrandCreateView(generics.CreateAPIView):
    queryset = mcfcarbrand.objects.all()
    serializer_class = McfCarBrandCreateSerializer
    # permission_classes = [IsAuthenticated]


from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from avto_bs.models import z_avtobrand
from .serializers import ZAvtobrandCreateSerializer, AvtobrandSerializer

class ZAvtobrandCreateView(generics.CreateAPIView):
    queryset = z_avtobrand.objects.all()
    serializer_class = ZAvtobrandCreateSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


from rest_framework import generics
from avto_bs.models import z_avtobrand
from .serializers import AvtobrandSerializer

class AvtobrandDetailAPIView(generics.RetrieveUpdateAPIView):
    queryset = z_avtobrand.objects.all()
    serializer_class = AvtobrandSerializer
    lookup_field = 'BrandID'

class ZAvtobrandDeleteView(generics.DestroyAPIView):
    queryset = z_avtobrand.objects.all()
    lookup_field = 'BrandID'