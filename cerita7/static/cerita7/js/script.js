$(document).ready(function () {
    // hide all panel at beginning
    $(".inner-accordion").hide();

    // show/hide clicked panel
    $(".accordion").click(function () {
        $(this.parentNode.parentNode).next().toggle(500);
    });
});

//set activeRow/clicked index
var activeRow = 0;

function setActiveRow(el) {
    var rows = document.getElementById('movingTable').rows;
    for (var i = 0; i < rows.length; i++) {
        if (rows[i] == el) activeRow = i;
    }
}

// move actived row up or down
function moveActiveRow(move) {
    var rows = document.getElementById('movingTable').rows;

    var oldRow = rows[activeRow];
    var oldContentRow = rows[activeRow + 1];

    // move down
    if (move == 1) {
        var newRow = rows[activeRow + 2];
        var newContentRow = rows[activeRow + 3];

        if (newRow != null) {
            oldRow.parentNode.insertBefore(newContentRow, oldRow);
            newContentRow.parentNode.insertBefore(newRow, newContentRow);
        }
        // move up
    } else {
        var newRow = rows[activeRow - 2];
        var newContentRow = rows[activeRow - 1];

        if (newRow != null) {
            newRow.parentNode.insertBefore(oldContentRow, newRow);
            oldContentRow.parentNode.insertBefore(oldRow, oldContentRow);
        }
    }
}

//moving function helper
function moveRow(cell, move) {
    setActiveRow(cell.parentNode);
    moveActiveRow(move);
}

