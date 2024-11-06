from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# Calculate the assessment linear regression
mae_linear = mean_absolute_error(y_test, y_pred)
mse_linear = mean_squared_error(y_test, y_pred)
r2_linear = r2_score(y_test, y_pred)

# Calculate the assessment decision tree
mae_tree = mean_absolute_error(y_test, y_pred_tree)
mse_tree = mean_squared_error(y_test, y_pred_tree)
r2_tree = r2_score(y_test, y_pred_tree)

# Calculate the assessment neural network
mae_nn = mean_absolute_error(y_test, y_pred_nn)
mse_nn = mean_squared_error(y_test, y_pred_nn)
r2_nn = r2_score(y_test, y_pred_nn)

# print result
print(f"Linear Regression - MAE: {mae_linear}, MSE: {mse_linear}, R2: {r2_linear}")
print(f"Decision Tree - MAE: {mae_tree}, MSE: {mse_tree}, R2: {r2_tree}")
print(f"Neural Network - MAE: {mae_nn}, MSE: {mse_nn}, R2: {r2_nn}")
