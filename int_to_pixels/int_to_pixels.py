import sys
import tensorflow as tf
from keras.models import Sequential, load_model
from keras.layers import Dense, Embedding, Flatten, Reshape
import numpy as np
print("TensorFlow version:", tf.__version__)

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

def train_model():
    X = np.array(list(data.keys()))
    Y = np.array([np.array(data[key]).flatten() for key in data.keys()])

    # 1. Input layer for a single byte
    input_layer = tf.keras.layers.Input(shape=(1,), dtype=tf.uint8)
    # 2. Normalize the byte to [0, 1]
    normalized_input = tf.keras.layers.Lambda(lambda x: tf.cast(x, tf.float32) / 255.0)(input_layer)
    # 3. Hidden layer (let's say with 32 units and ReLU activation)
    hidden_layer = tf.keras.layers.Dense(32, activation='relu')(normalized_input)
    hidden_layer = tf.keras.layers.Dense(32, activation='relu')(hidden_layer)
    hidden_layer = tf.keras.layers.Dense(32, activation='relu')(hidden_layer)
    # 4. Output layer with 15 parameters (let's assume a linear activation for simplicity)
    output_layer = tf.keras.layers.Dense(15, activation='sigmoid')(hidden_layer)
    # Construct the model
    # model = Sequential([
    #     input_layer,
    #     normalized_input,
    #     hidden_layer,
    #     output_layer
    # ])
    model = tf.keras.Model(inputs=input_layer, outputs=output_layer)

    # model = Sequential([
    #     # Reshape(target_shape=(1,), input_shape=(1, 1)),
    #     # Dense(1, input_shape=(1,)), # 1 input unit for the integer
    #     Embedding(10, 10, input_length=1), # Embed the integers to a higher-dimensional space
    #     Flatten(), # Flatten the embedding
    #     # Dense(32, activation='relu'),
    #     Dense(15, activation='sigmoid')  # 15 output units for the 3x5 grid
    # ])
    # model.add(tf.keras.layers.Dense(8, input_shape=(16,)))

    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    model.fit(X, Y, epochs=20000)
    model.save('model.keras')
    print("Training done, now loading and using the model")


def repl_with_model():
    while True:
        print("Enter a number between 0 and 9 (q to quit):)")
        response = input()
        if response == 'q':
            break
        number = int(response)
        grid_prediction = predict_pixels(number)
        my_map = []
        for row in grid_prediction:
            for i in row:
                if i == 0:
                    print(" ", end="")
                else:
                    print("*", end="")
            print("")
        # print(my_map)


def predict_pixels(number):
    model = load_model('model.keras', safe_mode=False)
    prediction = model.predict(np.array([number]))
    grid_prediction = (prediction > 0.5).astype(int).reshape(5, 3)
    return grid_prediction.tolist()


def run_tests():
    model = load_model('model.keras', safe_mode=False)
    passing_tests = 0
    failing_tests = []
    for i in range(10):
        grid = predict_pixels(i)
        if grid == data[i]:
            passing_tests += 1
        else:
            failing_tests.append(i)
    
    assert passing_tests == 10, f"Failed {10 - passing_tests} tests: {failing_tests}"
        # assert grid == data[i], f"Failed to predict {i} correctly\nExpected: \n{data[i]}\nGot: \n{grid}"
    print("All tests passed!")
    sys.exit(0)

if __name__ == '__main__':
    # check the cmd line args to see if they want to just train the model non-interactively
    if len(sys.argv) > 1:
        if sys.argv[1] == '--train':
            train_model()
            sys.exit(0)
        elif sys.argv[1] == '--test':
            run_tests()
    
    print("Choose mode:")
    print("1 for training the model")
    print("2 REPLing with the model")
    print("3 for testing the model")
    mode = int(input())
    if mode == 1:
        train_model()
    elif mode == 2:
        repl_with_model()
    elif mode == 3:
        run_tests()
    else:
        print("Invalid mode, exiting")
