from django.shortcuts import render

class AccountApi(generics.GenericAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        user_data = UserSerializer(user, context=self.get_serializer_context())
        user = user_data.data
        return response.Response(
            {
                "user": user,
                "message": "User Created Successfully.  Now perform Login to get your token",
            }
        )

    def get(self, request: request.Request, *args, **kwargs):
        users = User.objects.all()
        user_data = UserSerializer(users, many=True)
        return response.Response(user_data.data)


class AccountDetailApi(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
