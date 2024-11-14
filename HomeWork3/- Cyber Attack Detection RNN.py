import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout
from sklearn.metrics import accuracy_score, recall_score, f1_score, roc_auc_score
import matplotlib.pyplot as plt

# Step 1: Data Collection
# Load the dataset (assumed to be in CSV format)
data = pd.read_csv('CICIDS_2017.csv')

# Step 2: Data Preprocessing
# Clean the data (drop rows with missing values)
data = data.dropna()

# Select necessary features (e.g., Time, SourceIP, DestinationIP, Protocol, etc.)
features = data[['Time', 'SourceIP', 'DestinationIP', 'Protocol', 'Feature1', 'Feature2', 'FeatureN']]
labels = data['Label']  # Label indicates attack or no attack

# Normalize the feature data
scaler = StandardScaler()
features_scaled = scaler.fit_transform(features)

# Split the data into training and test sets (80% training, 20% testing)
X_train, X_test, y_train, y_test = train_test_split(features_scaled, labels, test_size=0.2, random_state=42)

# Reshape data for RNN input (we are assuming a sequence length of 100)
# This means we take 100 samples as a single sequence for each input
X_train_rnn = X_train.reshape(X_train.shape[0], 100, -1)  # Reshaping to [samples, time_steps, features]
X_test_rnn = X_test.reshape(X_test.shape[0], 100, -1)

# Step 3: Model Design
# Initialize a Sequential model
model = Sequential()

# Add an LSTM layer (64 units, 'relu' activation function)
model.add(LSTM(units=64, activation='relu', input_shape=(X_train_rnn.shape[1], X_train_rnn.shape[2])))

# Add Dropout layer to prevent overfitting
model.add(Dropout(0.5))

# Add a Dense output layer with sigmoid activation (binary classification: attack or no attack)
model.add(Dense(1, activation='sigmoid'))

# Compile the model with Adam optimizer and binary cross-entropy loss function
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Print the model summary to inspect the architecture
model.summary()

# Step 4: Model Training
# Train the model on the training data (with validation on test data)
history = model.fit(X_train_rnn, y_train, epochs=10, batch_size=32, validation_data=(X_test_rnn, y_test))

# Step 5: Model Evaluation
# Use the trained model to make predictions on the test set
y_pred = model.predict(X_test_rnn)
y_pred = (y_pred > 0.5).astype(int)  # Convert probabilities to 0 or 1 (attack or no attack)

# Evaluate the model using various metrics
accuracy = accuracy_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)
roc_auc = roc_auc_score(y_test, y_pred)

# Print the evaluation results
print(f'Accuracy: {accuracy}')
print(f'Recall: {recall}')
print(f'F1 Score: {f1}')
print(f'ROC AUC: {roc_auc}')

# Step 6: Results Analysis
# Plot the training and validation accuracy over epochs
plt.plot(history.history['accuracy'], label='Train Accuracy')
plt.plot(history.history['val_accuracy'], label='Test Accuracy')
plt.title('Model Accuracy')
plt.legend()
plt.show()

# Plot the training and validation loss over epochs
plt.plot(history.history['loss'], label='Train Loss')
plt.plot(history.history['val_loss'], label='Test Loss')
plt.title('Model Loss')
plt.legend()
plt.show()
