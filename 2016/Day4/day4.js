(function () {
    var hidden = document.getElementById('data1');
    var data = hidden.value.split(/\n/);

    function part1() {
        var out = document.getElementById('console1');
        var tmpObj = {};

        var cmp = function (k1, k2) {
            var res = tmpObj[k2] - tmpObj[k1];
            if (res === 0) {
                res = k1.charCodeAt(0) - k2.charCodeAt(0);
            }
            return res;
        };

        var code = data.reduce(function (sum, line) {
            var parts = line.replace(/-/g, '').match(/^([a-z]*)(\d+)\[(.*)\]$/);
            parts.shift();
            var letters = parts[0].split('');
            tmpObj = {};
            letters.forEach(function (ch) {
                tmpObj[ch] = tmpObj[ch] + 1 || 1;
            })
            var sorted = Object.keys(tmpObj).sort(cmp).join('');
            if (sorted.startsWith(parts[2])) {
                return sum + Number(parts[1]);
            }
            return sum;
        }, 0);

        var p = document.createElement('p');
        p.innerText = code;
        out.appendChild(p);
    }

    function rotate(ch, steps) {
        var aCode = 'a'.charCodeAt(0);
        var code = ch.charCodeAt(0) - aCode;
        var code = (code  + (steps % 26)) % 26;
        return String.fromCharCode(aCode + code);
    }

    function part2() {
        var out = document.getElementById('console2');

        data.forEach(function (line, idx) {
            var parts = line.match(/^([a-z-]*)(\d+)\[(.*)\]$/);
            parts.shift();
            var letters = parts[0].split('');
            var decrypted = letters.map(function (l) {
                return l === '-' ? ' ' : rotate(l, parts[1]);
            });
            decrypted = decrypted.join().replace(/,/g, '');
            if(decrypted.indexOf('north') > -1) {
                var p = document.createElement('p');
                p.innerText = parts[1];
                out.appendChild(p);
            }
        });
    }

    part1();
    part2();

})();