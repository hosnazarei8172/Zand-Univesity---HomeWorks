from sklearn.preprocessing import StandardScaler

features = data[['Temperature', 'Humidity']]
target = data['Energy Consumption']

scaler = StandardScaler()
features_scaled = scaler.fit_transform(features)
