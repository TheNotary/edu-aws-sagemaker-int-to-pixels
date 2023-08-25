/*
 * We'll use HTML to draw our pixels, setting div elements to be 
 * either active or not.  
 * We'll start out with pre-defined values for our numbers.
 */
function drawNumberViaLookup(displayIndex) {
    const num = parseInt(document.getElementById('numberInput' + displayIndex).value);
    
    const grid = document.getElementById('grid' + displayIndex);
    clearGrid(grid);
    
    const pixelGridConfig = pullPixelGridConfigFromTable(num);
    setGrid(grid, pixelGridConfig);
}

/*
 * It's a silly problem to solve with a NN, but we'll then use this
 * predefined data to train a NN to generate numbers based on text input.
 */ 
function drawNumberViaNN(displayIndex) {
    const num = parseInt(document.getElementById('numberInput' + displayIndex).value);
    
    fetch('/pixels?number=' + num)
        .then(response => response.json())
        .then(data => {
            const grid = document.getElementById('grid' + displayIndex);
            clearGrid(grid);
            setGrid(grid, data['pixels']);
        });
}

function clearGrid(grid) {
    for (let i = 0; i < 5; i++) {
        for (let j = 0; j < 3; j++) {
            const elem = grid.getElementsByClassName(`cell${i}${j}`);
            elem[0].classList.remove('active');
        }
    }
}

function setGrid(grid, pixelGridConfig) {
    for (let i = 0; i < 5; i++) {
        for (let j = 0; j < 3; j++) {
            if (pixelGridConfig[i][j]) {
                const elem = grid.getElementsByClassName(`cell${i}${j}`);
                elem[0].classList.add('active');
            }
        }
    }
}

function pullPixelGridConfigFromTable(num) {
    const pixelGridConfigs = {
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

    return pixelGridConfigs[num];
}
