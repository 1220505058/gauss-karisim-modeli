# gauss-karisim-modeli
İlk olarak, veri noktaları veriler adlı bir numpy dizisinde tanımlanır.
GaussianMixture sınıfı kullanılarak bir Gauss karışım modeli (gmm) oluşturulur. Bu model, veri noktalarını belirtilen sayıda bileşene göre kümelere ayırmak için kullanılır. n_components parametresi ile kaç bileşen kullanılacağı belirlenir.
gmm.fit(veriler) komutuyla model, veri noktalarını kullanarak öğrenme işlemini gerçekleştirir ve veri noktalarını bileşenlere atar.
Elde edilen Gauss bileşenlerinin özellikleri (mean, covariance) ve ağırlıkları (weights) gmm.means_, gmm.covariances_ ve gmm.weights_ ile erişilebilir.
Son olarak, her bir Gauss bileşeni için ortalama, varyans ve ağırlık değerleri yazdırılır.
Bu şekilde, Gauss karışım modeli kullanarak veri noktaları kümelere ayrılır ve her bir kümenin özellikleri elde edilir.
