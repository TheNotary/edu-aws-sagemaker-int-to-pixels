import sys
import tensorflow as tf
from keras.models import Sequential, load_model
from keras.layers import Dense, Embedding, Flatten, Reshape, Lambda, Input
import numpy as np
from training_data import TrainingData
# print("TensorFlow version:", tf.__version__)


def main():
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
    print("4 for model summary")
    print("5 for targetted training_charge")
    print("6 for complete training_charge")
    mode = int(input())
    if mode == 1:
        train_model()
    elif mode == 2:
        repl_with_model()
    elif mode == 3:
        run_tests()
    elif mode == 4:
        summary()
    elif mode == 5:
        training_charge()
    elif mode == 6:
        training_charge_all()
    else:
        print("Invalid mode, exiting")



def train_model():
    model = build_original_model()
    # model = build_uint8_model()
    # model = build_one_hot_encoding_model()
    
    # Ok, show me the code for a network that uses one hot encoding to convert the input integer into a sparse representation then has a hidden layer before finally  having a 15 parameter output layer.
    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    
    # while True:
    #     print("Enter for train, s for stop")
    #     if input() == "s":
    #         break
    #     model.fit(X, Y, epochs=1000)
        
    X, Y = TrainingData().get_training_inputs_outputs()
    
    model.fit(X, Y, epochs=1000)
        
    model.save('model.keras')
    print("Training done, now loading and using the model")
    model.summary()


def build_uint8_model():
    ######################
    # Use uint8 as Input #
    ######################
    
    # 1. Input layer for a single byte
    input_layer = Input(shape=(1,), dtype=tf.uint8)
    # 2. Normalize the byte to [0, 1]
    normalized_input = Lambda(lambda x: tf.cast(x, tf.float32) / 255.0)(input_layer)
    # 3. Hidden layer (let's say with 32 units and ReLU activation)
    hidden_layer = Dense(15, activation='relu')(normalized_input)
    hidden_layer = Dense(15, activation='relu')(hidden_layer)
    hidden_layer = Dense(15, activation='relu')(hidden_layer)
    hidden_layer = Dense(15, activation='relu')(hidden_layer)
    hidden_layer = Dense(20, activation='relu')(hidden_layer)
    # 4. Output layer with 15 parameters (let's assume a linear activation for simplicity)
    output_layer = Dense(15, activation='sigmoid')(hidden_layer)
    model = tf.keras.Model(inputs=input_layer, outputs=output_layer)
    return model

def build_original_model():
    model = Sequential([
        # Reshape(target_shape=(1,), input_shape=(1, 1)),
        # Dense(1, input_shape=(1,)), # 1 input unit for the integer
        Embedding(10, 10, input_length=1), # Embed the integers to a higher-dimensional space
        Flatten(), # Flatten the embedding
        # Dense(32, activation='relu'),
        Dense(15, activation='sigmoid')  # 15 output units for the 3x5 grid
    ])
    return model

def build_one_hot_encoding_model():
    pass


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
        if grid == TrainingData.training_data[i]:
            passing_tests += 1
        else:
            failing_tests.append(i)
    
    assert passing_tests == 10, f"Failed {10 - passing_tests} tests: {failing_tests}"
        # assert grid == TrainingData.training_data[i], f"Failed to predict {i} correctly\nExpected: \n{training_data[i]}\nGot: \n{grid}"
    print("All tests passed!")
    sys.exit(0)

def summary():
    model = load_model('model.keras', safe_mode=False)
    model.summary()

def training_charge():
    model = load_model('model.keras', safe_mode=False)
    # X = np.array(list(training_data.keys()))
    # Y = np.array([np.array(training_data[key]).flatten() for key in training_data.keys()])

    X = np.array([8])
    Y = np.array([np.array(TrainingData.training_data[8]).flatten()])
    model.fit(X, Y, epochs=1)
    model.save('model.keras')
    
def training_charge_all():
    model = load_model('model.keras', safe_mode=False)
    X = np.array(list(TrainingData.training_data.keys()))
    Y = np.array([np.array(TrainingData.training_data[key]).flatten() for key in TrainingData.training_data.keys()])

    # X = np.array([8])
    # Y = np.array([np.array(TrainingData.training_data[8]).flatten()])
    model.fit(X, Y, epochs=9)
    model.save('model.keras')
    model


if __name__ == '__main__':
    main()
