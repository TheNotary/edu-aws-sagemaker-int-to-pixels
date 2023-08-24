/*
 * We'll use HTML to draw our pixels, setting div elements to be 
 * either active or not.  
 * We'll start out with pre-defined values for our numbers.
 * It's a silly problem to solve with a NN, but we'll then use this
 * predefined data to train a NN to generate numbers based on text input.
 */
function drawNumber() {
    const num = parseInt(document.getElementById('numberInput').value);

    // Reset the grid
    for (let i = 0; i < 5; i++) {
        for (let j = 0; j < 3; j++) {
            document.getElementById(`cell${i}${j}`).classList.remove('active');
        }
    }

    const numbers = {
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
    };

    const currentNumber = numbers[num];

    for (let i = 0; i < 5; i++) {
        for (let j = 0; j < 3; j++) {
            if (currentNumber[i][j]) {
                document.getElementById(`cell${i}${j}`).classList.add('active');
            }
        }
    }
}

