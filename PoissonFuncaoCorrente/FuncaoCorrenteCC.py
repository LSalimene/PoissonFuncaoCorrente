import numpy as np
def funcaocorrenteCC(psi,vorticidade,dx,dy,l=2500):

    """
    Calcula a Função Corrente com a matriz contendo as condições de contorno ja montadas e uma vorticidade conhecida
    Parameters
    ----------
    psi : numpy.ndarray
        Matriz para a FC com as CC aplicadas.
    vorticidade : numpy.ndarray
        Matriz com a vorticidade conhecida.
    dx : float
        Distância entre cada ponto da grade em x.
    dy : float
        Distância entre cada ponto da grade em y.
    l : int, optional
        Número de iterações que o método irá utilizar (padrão é 2500).

    Returns
    -------
    numpy.ndarray
        Função Corrente calculada numericamente pelo método iterativo com l iterações.
    """
    k=0
    while k<l:
        for i in range(1,psi.shape[0]-1):
            for j in range (1,psi.shape[1]-1):
                    psi[i,j] = 0.25*(psi[i+1,j]+psi[i,j+1]+psi[i-1,j]+psi[i,j-1]-(dy*dx*vorticidade[i,j]))
        k = k+1
    return psi
