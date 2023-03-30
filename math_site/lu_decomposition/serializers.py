from typing import Any, List

import numpy as np
from rest_framework.serializers import (CharField, IntegerField, ListField,
                                        Serializer, FloatField)


class MatrixSerializer(Serializer):
    matrix = ListField(child=ListField(child=FloatField()))

    class Meta:
        fields = "matrix"
