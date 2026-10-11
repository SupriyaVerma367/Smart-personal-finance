from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import RegisterSerializer

@api_view(['GET'])
def test_api(request):
    return Response({
        'message':"Smart Personal Finance API is working!",
        'status':'success'
    })
@api_view(['POST'])
def register_user(request):
    serializer = RegisterSerializer(data=request.data)

    if serializer.is_valid():
        user=serializer.save()
        return Response(
            {
                'message':'Registration succesful',
                'user_id':user.id,
                'username':user.username
            },
            status=status.HTTP_201_CREATED

        )
    return Response(
        serializer.errors,
        status=status.HTTP_400_BAD_REQUEST
    )
