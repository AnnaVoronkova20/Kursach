from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from .logic import LU_partial_decomposition, array_to_list, list_to_array
from .serializers import MatrixSerializer


def index(request):
    return render(request, 'index.html')


class LUView(APIView):
    def post(self, request):
        data = MatrixSerializer(data=request.data)
        if data.is_valid(raise_exception=True):
            matrix = data.data["matrix"]
            matrix_arr = list_to_array(matrix)
            try:
                result = LU_partial_decomposition(matrix_arr)
            except:
                return Response(data={"msg": "bad matrix"}, status=400)
            for key, value in result.items():
                tmp_matrix = array_to_list(value)
                if tmp_matrix is None:
                    return Response(data={"msg": "bad matrix"}, status=400)
                result.update({key: tmp_matrix})

            result.update({"input": matrix})
            return Response(data=result, status=200)
