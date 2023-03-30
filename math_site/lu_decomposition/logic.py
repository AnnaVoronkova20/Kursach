from typing import Any, Dict, List

import numpy as np


def LU_partial_decomposition(
    matrix: np.ndarray,
) -> Dict[str, np.ndarray]:
    n, m = matrix.shape
    P = np.identity(n)
    L = np.identity(n)
    U = matrix.copy()
    PF = np.identity(n)
    LF = np.zeros((n, n))
    for k in range(0, n - 1):
        index = np.argmax(abs(U[k:, k]))
        index = index + k
        if index != k:
            P = np.identity(n)
            P[[index, k], k:n] = P[[k, index], k:n]
            U[[index, k], k:n] = U[[k, index], k:n]
            PF = np.dot(P, PF)
            LF = np.dot(P, LF)
        L = np.identity(n)
        for j in range(k + 1, n):
            L[j, k] = -(U[j, k] / U[k, k])
            LF[j, k] = U[j, k] / U[k, k]
        U = np.dot(L, U)
    np.fill_diagonal(LF, 1)
    return {"P": PF, "L": LF, "U": U}


def list_to_array(matrix: List[Any]) -> np.ndarray:
    return np.array(matrix)


def array_to_list(matrix: np.ndarray) -> List[Any]:
    
    result = matrix.tolist()
    
    for i in range(len(result)):
        for j in range(len(result[i])):
            if np.isnan(result[i][j]):
                return

    return result
