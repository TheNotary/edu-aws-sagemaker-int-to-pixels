import tensorflow as tf
import numpy as np
print("TensorFlow version:", tf.__version__)


def train_model():
    data = {
        0: [[1, 1, 1], [1, 0, 1], [1, 0, 1], [1, 0, 1], [1, 1, 1]],
        1: [[0, 0, 1], [0, 0, 1], [0, 0, 1], [0, 0, 1], [0, 0, 1]],
        2: [[1, 1, 1], [0, 0, 1], [1, 1, 1], [1, 0, 0], [1, 1, 1]],
        3: [[1, 1, 1], [0, 0, 1], [1, 1, 1], [0, 0, 1], [1, 1, 1]],
        4: [[1, 0, 1], [1, 0, 1], [1, 1, 1], [0, 0, 1], [0, 0, 1]],
        5: [[1, 1, 1], [1, 0, 0], [1, 1, 1], [0, 0, 1], [1, 1, 1]],
        6: [[1, 1, 1], [1, 0, 0], [1, 1, 1], [1, 0, 1], [1, 1, 1]],
        7: [[1, 1, 1], [0, 0, 1], [0, 0, 1], [0, 0, 1], [0, 0, 1]],
        8: [[1, 1, 1], [1, 0, 1], [1, 1, 1], [1, 0, 1], [1, 1, 1]],
        9: [[1, 1, 1], [1, 0, 1], [1, 1, 1], [0, 0, 1], [1, 1, 1]]
    }

    X = np.array(list(data.keys()))
    Y = np.array([np.array(data[key]).flatten() for key in data.keys()])


    from keras.models import Sequential
    from keras.layers import Dense, Embedding, Flatten

    model = Sequential([
        Embedding(10, 64, input_length=1), # Embed the integers to a higher-dimensional space
        Flatten(), # Flatten the embedding
        Dense(32, activation='relu'),
        Dense(15, activation='sigmoid')  # 15 output units for the 3x5 grid
    ])

    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    model.fit(X, Y, epochs=200)
    model.save('model.keras')
    print("Training done, now loading and using the model")


def load_and_use_model():
    # now we load the model and use it
    from keras.models import load_model
    model = load_model('model.keras')

    while True:
        print("Enter a number between 0 and 9 (q to quit):)")
        response = input()
        if response == 'q':
            break
        number = int(response)
        prediction = model.predict(np.array([number]))
        grid_prediction = (prediction > 0.5).astype(int).reshape(5, 3)
        print(grid_prediction)

if __name__ == '__main__':
    print("Choose mode: 1 for training, 2 for loading and using the model")
    mode = int(input())
    if mode == 1:
        train_model()
    elif mode == 2:
        load_and_use_model()
    else:
        print("Invalid mode, exiting")
