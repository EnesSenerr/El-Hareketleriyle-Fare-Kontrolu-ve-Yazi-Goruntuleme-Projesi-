import pandas as pd
import glob

csv_files = glob.glob('*.csv')  # Tüm CSV dosyalarını al

all_data = []


for file in csv_files:
    df = pd.read_csv(file)
         # Etiketleme
    label = file.split('.')[0]  # Dosya adını al ve etiket olarak kullan
    df['Label'] = label
    
  
    all_data.append(df)


final_data = pd.concat(all_data, ignore_index=True)


print(final_data.head())

final_data.to_csv('all_data2.csv', index=False)

data = pd.read_csv('all_data2.csv')

features = data.drop(columns=['Label'])

labels = data['Label']

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.2, random_state=42)

print(f"Eğitim verisi: {X_train.shape}")
print(f"Test verisi: {X_test.shape}")

from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

model = KNeighborsClassifier(n_neighbors=3)

model.fit(X_train, y_train)


y_pred = model.predict(X_test)


accuracy = accuracy_score(y_test, y_pred)
print(f"Model doğruluğu: {accuracy * 100:.2f}%")


from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)
print("Karmaşıklık Matrisi:")
print(cm)

import joblib
joblib.dump(model, 'knn_model3.pkl')  # Modeli kaydet

