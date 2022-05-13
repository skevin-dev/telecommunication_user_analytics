from sklearn.decomposition import PCA
def dim_reduction(X):
    i = 1
    cum_sum = 0
    while cum_sum<=0.99:
        pca_stocks = PCA(n_components=i)
        principalComponents_stocks = pca_stocks.fit_transform(X.values)
        cum_sum = sum(pca_stocks.explained_variance_ratio_)
        print('Number of principal components:',i,'Proportion of Variance Explained:',cum_sum)
        i+=1