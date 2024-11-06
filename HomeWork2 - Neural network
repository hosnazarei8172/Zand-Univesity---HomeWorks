from sklearn.neural_network import MLPRegressor

# making Neural network
nn_model = MLPRegressor(hidden_layer_sizes=(50,), max_iter=1000, random_state=42)
nn_model.fit(X_train, y_train)

# prediction energy
y_pred_nn = nn_model.predict(X_test)
