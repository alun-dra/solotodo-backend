from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Post
from .serializers import PostSerializer
from django.shortcuts import get_object_or_404

class PostList(APIView):
    """
    Clase para listar todos los posts o crear un nuevo post.
    - GET: Devuelve todos los posts disponibles.
    - POST: Crea un nuevo post con los datos proporcionados.
    """
    def get(self, request):
        posts = Post.objects.all()  # Obtiene todos los posts
        serializer = PostSerializer(posts, many=True)  # Serializa los datos de los posts
        return Response({
            'status': 'success',
            'data': serializer.data
        })  # Envía la respuesta con los datos serializados en formato dict

    def post(self, request):
        serializer = PostSerializer(data=request.data)  # Crea un nuevo serializador con los datos proporcionados
        if serializer.is_valid():  # Verifica la validez del serializador
            serializer.save()  # Guarda el nuevo post si es válido
            return Response({
                'status': 'success',
                'data': serializer.data,
                'message': 'Post created successfully'
            }, status=status.HTTP_201_CREATED)  # Devuelve el post creado y un estado 201 con mensaje
        return Response({
            'status': 'error',
            'errors': serializer.errors,
            'message': 'Error creating the post'
        }, status=status.HTTP_400_BAD_REQUEST)  # Si no es válido, devuelve los errores en formato dict

class PostDetail(APIView):
    """
    Clase para manejar operaciones en un único post.
    - GET: Devuelve un post específico por su ID.
    """
    def get(self, request, pk):
        post = get_object_or_404(Post, pk=pk)  # Obtiene el post o devuelve un error 404 si no existe
        serializer = PostSerializer(post)  # Serializa el post obtenido
        return Response({
            'status': 'success',
            'data': serializer.data
        })  # Envía la respuesta con el post serializado en formato dict
