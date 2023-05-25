import numpy as np
from sklearn.mixture import GaussianMixture

# Veri noktaları
veriler = np.array([[1.2], [1.4], [1.6], [9.5], [9.8], [9.9]])

# Gauss karışım modeli oluşturma
gmm = GaussianMixture(n_components=3, random_state=42)

# Verileri modele uydurma (kümeleme yapma)
gmm.fit(veriler)

# Elde edilen Gauss bileşenlerini ve ağırlıklarını yazdırma
for j in range(gmm.n_components):
    print(f"Bileşen {j+1}: ortalama={gmm.means_[j][0]:.2f}, varyans={np.diag(gmm.covariances_[j])[0]:.2f}, ağırlık={gmm.weights_[j]:.2f}")