(function () {
    var cmp = function(a, b) { return a - b; }
    function part1() {
        var hidden = document.getElementById('data1');
        var data = hidden.value.split(/\n/);
        var out = document.getElementById('console1');

        var possibleTriangles = data.reduce(function (count, row) {
            var fixed = row.replace(/^\s*/, '').split(/\s+/);
            var sorted = fixed.map(function (itm) { return Number(itm) }).sort(cmp);
            if (sorted[0] + sorted[1] > sorted[2])
                return count + 1;
            return count;
        }, 0);

        var p = document.createElement('p');
        p.innerText = 'Answer is: ' + possibleTriangles;
        out.appendChild(p);
    }

    function part2() {
        var hidden = document.getElementById('data1');
        var data = hidden.value.split(/\n/);
        var out = document.getElementById('console2');
        var tmpArr = [[],[],[]];

        data.forEach(function(row) {
            var sp = row.replace(/^\s*/, '').split(/\s+/);
            sp.forEach(function(val, idx) {
                tmpArr[idx].push(val);
            })
        });
        var numbers = [].concat(tmpArr[0], tmpArr[1], tmpArr[2]);
        var count = 0;
        for(var i = 0; i < numbers.length; i += 3) {
            var t = [Number(numbers[i]), Number(numbers[i + 1]), Number(numbers[i + 2])].sort(cmp);
             if(t[0] + t[1] > t[2]) {
                count++;
            }
        }
        var p = document.createElement('p');
        p.innerText = 'Answer is: ' + count;
        out.appendChild(p);
    }

    part1();
    part2();

})();