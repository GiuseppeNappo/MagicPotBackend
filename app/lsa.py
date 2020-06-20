import numpy as np
from scipy.sparse import csr_matrix
from sklearn.metrics.pairwise import cosine_similarity
import pickle
from sklearn.decomposition import TruncatedSVD
class LSA:
    def createQuery(userTerms, terms):
        query = [0] * len(terms)
        for x in userTerms:
            i = 0
            for y in terms:
                if x == y:
                    query[i] = 1
                i = i + 1

        return query

    def lsa(self):
        #Prende il vettore dei termini  salvato (il vettore dei termini comprende tutti gli ingredienti delle ricette
        with open("termsFile.txt", "rb") as fp:
            terms = pickle.load(fp)
        dtMatrixFile = np.load('dtMatrixFile2.npy')

        #effettutiamo la truncSVD sulla matrice composta da Ricette/ingredienti
        #trunc_SVD_model = TruncatedSVD(n_components=4)
        #dtMatrix = trunc_SVD_model.fit_transform(dtMatrixFile)
        {
        # Questo è il codice che data una lista di stringhe ritorna la matrice sparsa e i termini
        '''
                vectorizer = CountVectorizer(min_df=1)
                dtm = vectorizer.fit_transform(example)
                trunc_SVD_model = TruncatedSVD(n_components=5)
                dtMatrix = trunc_SVD_model.fit_transform(dtm.toarray())
                terms = vectorizer.get_feature_names()
        '''
        }
        # Query Creation , Creiamo una Query ossia un vettore query (un vettore formato di 0 e 1 )
        userQuery = LSA.createQuery(self, terms)
        #transformedQuery = trunc_SVD_model.transform(csr_matrix(userQuery))

        # LSA
        similarities = cosine_similarity(dtMatrixFile, csr_matrix(userQuery))

        n = 5
        indexes = np.argsort(similarities.flat)[-n:]

        cnt = 0
        #Prendiamo i coseni maggiori di 0.5 per il best-matching
        for x in similarities.flat[indexes]:
            if x > 0.5:
                cnt = cnt+1

        #Riordino gli indici
        finalBestRecipes = np.argsort(similarities.flat)[-cnt:]

        return list(finalBestRecipes[::-1])