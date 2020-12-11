
(function () {
    var input = '11100010111110100';
    var dest = input;
    var diskSize = 35651584;

    String.prototype.reverse = function () {
        var s = this;
        return s.split('').reverse().join('');
    }

    while (dest.length < diskSize) {
        var tmp = dest.reverse().replace(/[0-1]/g, function (c) {
            return c == '0' ? 1 : '0';
        });
        dest = dest + '0' + tmp;
    }
    var s = dest.substr(0, diskSize);
    var pairs = s.match(/\d\d/g);
    var s1 = "";
    while(s1.length % 2 == 0) {
        s1 = "";
        for(var i = 0; i < pairs.length; i++) {
            s1 += (pairs[i].charAt(0) == pairs[i].charAt(1) ? '1' : '0');
        }
        pairs = s1.match(/\d\d/g);
    }
    console.log(s1);

})();