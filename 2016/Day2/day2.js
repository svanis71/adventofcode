function part1() {
    var hidden = document.getElementById('data1');
    var data = hidden.value.split(/\s/);
    var out  = document.getElementById('console1');

    var action = {
        'U': function(currentButton) {
            return currentButton > 3 ? currentButton - 3 : currentButton;
        },
        'D': function(currentButton) {
            return currentButton < 7 ? currentButton + 3 : currentButton;
        },
        'L': function(currentButton) {
            if(currentButton % 3 !== 1) {
                return currentButton - 1;
            }
            return currentButton;
        },
        'R': function(currentButton) {
            if(currentButton % 3 !== 0) {
                return currentButton + 1;
            }
            return currentButton;
        },
    };

    var code = '';
    var last = 5;
    data.forEach(function(row) {
        var path = row.split('');
        last = path.reduce(function(ch, curr) {
            return action[curr](ch);
        }, last);
        code = code + last;

    });

    var p = document.createElement('p');
    p.innerText = code;
    out.appendChild(p);
}

function part2() {
    var panel = [
        ['','','1','',''],
        ['','2','3','4',''],
        ['5','6','7','8','9'],
        ['','A','B','C',''],
        ['','','D','',''],
    ];
    var hidden = document.getElementById('data2');
    var data = hidden.value.split(/\s/);
    var out  = document.getElementById('console2');
    var pos = {row: 3, col: 0};
    var action = {
        'U': function(pos) {
            var newpos = {row: pos.row, col: pos.col};
            if(panel[newpos.row - 1] && panel[newpos.row - 1][newpos.col] !== '') {
                newpos.row--;
            }
            return newpos;
        },
        'D': function(pos) {
            var newpos = {row: pos.row, col: pos.col};
            if(panel[newpos.row + 1] && panel[newpos.row + 1][newpos.col] !== '') {
                newpos.row++;
            }
            return newpos;
        },
        'L': function(pos) {
            var newpos = {row: pos.row, col: pos.col};
            if(panel[newpos.row][newpos.col - 1] && panel[newpos.row][newpos.col - 1] !== '') {
                newpos.col--;
            }
            return newpos;
        },
        'R': function(pos) {
            var newpos = {row: pos.row, col: pos.col};
            if(panel[newpos.row][newpos.col + 1] && panel[newpos.row][newpos.col + 1] !== '') {
                newpos.col++;
            }
            return newpos;
        },
    };
    var code = '';
    data.forEach(function(row) {
        var path = row.split('');
        pos = path.reduce(function(ch, pos) {
            return action[pos](ch);
        }, pos);
        code = code + panel[pos.row][pos.col];
    });

    var p = document.createElement('p');
    p.innerText = code;
    out.appendChild(p);
}

(function() {
    part1();
    part2();
})();