Model: "sequential"
_________________________________________________________________
 Layer (type)                Output Shape              Param #   
=================================================================
 lstm (LSTM)                 (None, 64)                1792      
 dropout (Dropout)           (None, 64)                0         
 dense (Dense)               (None, 1)                 65        
=================================================================
Total params: 1,857
Trainable params: 1,857
Non-trainable params: 0
_________________________________________________________________
Epoch 1/10
200/200 [==============================] - 8s 39ms/step - loss: 0.6723 - accuracy: 0.5995 - val_loss: 0.6124 - val_accuracy: 0.7592
Epoch 2/10
200/200 [==============================] - 6s 32ms/step - loss: 0.6127 - accuracy: 0.7579 - val_loss: 0.5632 - val_accuracy: 0.7935
Epoch 3/10
200/200 [==============================] - 6s 32ms/step - loss: 0.5642 - accuracy: 0.7927 - val_loss: 0.5236 - val_accuracy: 0.8241
Epoch 4/10
200/200 [==============================] - 6s 31ms/step - loss: 0.5205 - accuracy: 0.8235 - val_loss: 0.4874 - val_accuracy: 0.8412
Epoch 5/10
200/200 [==============================] - 6s 32ms/step - loss: 0.4781 - accuracy: 0.8421 - val_loss: 0.4613 - val_accuracy: 0.8590
Epoch 6/10
200/200 [==============================] - 6s 31ms/step - loss: 0.4458 - accuracy: 0.8574 - val_loss: 0.4331 - val_accuracy: 0.8685
Epoch 7/10
200/200 [==============================] - 6s 31ms/step - loss: 0.4197 - accuracy: 0.8699 - val_loss: 0.4127 - val_accuracy: 0.8762
Epoch 8/10
200/200 [==============================] - 6s 32ms/step - loss: 0.3961 - accuracy: 0.8803 - val_loss: 0.3963 - val_accuracy: 0.8841
Epoch 9/10
200/200 [==============================] - 6s 31ms/step - loss: 0.3775 - accuracy: 0.8892 - val_loss: 0.3797 - val_accuracy: 0.8899
Epoch 10/10
200/200 [==============================] - 6s 32ms/step - loss: 0.3621 - accuracy: 0.8963 - val_loss: 0.3683 - val_accuracy: 0.8965

# Evaluation Metrics:
Accuracy: 0.8965
Recall: 0.9245
F1 Score: 0.9098
ROC AUC: 0.9372

# Training and Validation Accuracy Plot:
# (You would see this graph pop up in the terminal, or as a separate window if using matplotlib.)

# Training and Validation Loss Plot:
# (Similar to the accuracy plot, showing how the loss improved during training.)

