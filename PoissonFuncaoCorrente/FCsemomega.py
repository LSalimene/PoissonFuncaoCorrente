import numpy as np
def fcnOmega(vorticidade,dx,dy,l=2500):
    """
    Calcula a Função Corrente a partir de uma vorticidade conhecida

    Parameters
    ----------
    vorticidade : numpy.ndarray
        Matriz com a vorticidade.
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

    psi = np.zeros_like(vorticidade) 
    k = 0
    while k<l:
        for i in range(1,vorticidade.shape[0]-1):
            for j in range (1,vorticidade.shape[1]-1):
                    psi[i,j] = 0.25*(psi[i+1,j]+psi[i,j+1]+psi[i-1,j]+psi[i,j-1]-(dy*dx*vorticidade[i,j]))
        k = k+1
    return psi
