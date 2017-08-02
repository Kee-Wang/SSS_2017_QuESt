import numpy as np


def make_f_mo(g, kappa, F, nocc, nbas):
    """
    Make F_ia^kappa in MO basis

    Parameters
    ----------
    g: Numpy 4-tensor
    kappa : 1D array
    F : 2-tensor
    nocc: integer number of occupied orbitals
    nbas: number of basis functions

    Returns
    -------
    F : 1D array
    """

    # Slices - with RHF reference, nelec = 2 * nocc
    occ = slice(0, nocc)
    vir = slice(nocc, nbas)

    kappa.reshape((nocc, nvirt))

    # Einsum pieces of Eqn 14 in response handout
    one = np.einsum('ab,jb->ja', F[occ, occ], kappa)
    two = np.einsum('ij,jb->ib', F[vir, vir], kappa)
    thr = np.einsum('jb,iajb->ia', kappa, g[occ, vir, occ, vir]) 
    fou = np.einsum('jb,ijab->ia', kappa, g[occ, vir, occ, vir])
    fiv = np.einsum('jb,bjai->ia', kappa, g[occ, vir, occ, vir])
    
    Fiakappa = - one + two + 4 * thr - fou - fiv

    Fiakappa.ravel()

    return Fiakappa




