import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import classification_report, confusion_matrix

# Carregar os dados do arquivo local
data = pd.read_csv('wine_dataset.csv')

# Preparar os dados
X = data.drop('style', axis=1)  # Ajuste aqui para usar a coluna correta
y = data['style']  # Ajuste aqui para usar a coluna correta

# Dividir os dados
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Normalizar os dados
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Treinar o modelo
gnb = GaussianNB()
gnb.fit(X_train, y_train)

# Fazer predições
predictions = gnb.predict(X_test)

# Avaliar o modelo
print("Matriz de Confusão:")
print(confusion_matrix(y_test, predictions))
print("\nRelatório de Classificação:")
print(classification_report(y_test, predictions))

