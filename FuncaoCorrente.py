import numpy as np
def funcaocorrente(u,v,dx,dy,l=2500):
    """
    Calcula a Função Corrente a partir de um campo de velocidade conhecido.

    Parameters
    ----------
    u : numpy.ndarray
        Matriz com a componente u da velocidade.
    v : numpy.ndarray
        Matriz com a componente v da velocidade.
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
    psi = np.zeros_like(v)
    dudy, dudx = np.gradient(u, dx, dy)
    dvdy, dvdx = np.gradient(v, dx, dy)
    omega = dvdx - dudy
    psi = np.zeros_like(omega) 
    k = 0
    while k<l:
        for i in range(1,v.shape[0]-1):
            for j in range (1,v.shape[1]-1):
                    psi[i,j] = 0.25*(psi[i+1,j]+psi[i,j+1]+psi[i-1,j]+psi[i,j-1]-(dy*dx*omega[i,j]))
        k = k+1
    return psi
