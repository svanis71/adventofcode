(function () {
    var data = 'L1, L5, R1, R3, L4, L5, R5, R1, L2, L2, L3, R4, L2, R3, R1, L2, R5, R3, L4, R4, L3, R3, R3, L2, R1, L3, R2, L1, R4, L2, R4, L4, R5, L3, R1, R1, L1, L3, L2, R1, R3, R2, L1, R4, L4, R2, L189, L4, R5, R3, L1, R47, R4, R1, R3, L3, L3, L2, R70, L1, R4, R185, R5, L4, L5, R4, L1, L4, R5, L3, R2, R3, L5, L3, R5, L1, R5, L4, R1, R2, L2, L5, L2, R4, L3, R5, R1, L5, L4, L3, R4, L3, L4, L1, L5, L5, R5, L5, L2, L1, L2, L4, L1, L2, R3, R1, R1, L2, L5, R2, L3, L5, L4, L2, L1, L2, R3, L1, L4, R3, R3, L2, R5, L1, L3, L3, L3, L5, R5, R1, R2, L3, L2, R4, R1, R1, R3, R4, R3, L3, R3, L5, R2, L2, R4, R5, L4, L3, L1, L5, L1, R1, R2, L1, R3, R4, R5, R2, R3, L2, L1, L5'.replace(/[^LR,\d]/g, '');
    var moves = data.split(',');

    var canvas = document.getElementById('canvas');
    var ctx = canvas.getContext('2d');
    var out = document.getElementById('console');
    var coords = [];
    var ox = canvas.width / 2;
    var oy = canvas.height / 2;

    var x = 0;
    var y = 0;
    var xdir = -1;
    var ydir = 0;


    ctx.beginPath();
    ctx.moveTo(ox, oy);
    var stop = false
    for (var i = 0; i < moves.length && !stop; i++) {
        var dir = moves[i].charAt(0);
        var blocks = Number(moves[i].substring(1));
        if (xdir < 0) {
            ydir = dir === 'R' ? 1 : -1
            xdir = 0;
        } else if (ydir < 0) {
            xdir = dir === 'R' ? -1 : 1;
            ydir = 0;
        } else if (xdir > 0) {
            ydir = dir === 'R' ? -1 : 1;
            xdir = 0;
        } else if (ydir > 0) {
            xdir = dir === 'R' ? 1 : -1;
            ydir = 0;
        }
        for (var b = 0; b < blocks; b++) {
            var tx = x + (b * xdir);
            var ty = y + (b * ydir);
            var coord = tx + "_" + ty;
            if (coords.indexOf(coord) >= 0) {
                stop = true;
                var sp = document.createElement('p');
                sp.innerText = 'Cross first at ' + tx + ', ' + ty;
                out.appendChild(sp);
            }
            coords.push(coord);
        }
        y = y + (blocks * ydir);
        x = x + (blocks * xdir);
        ctx.lineTo(ox + x, oy + y);
    }

    var p = document.createElement('p');
    p.innerText = 'Target at ' + x + ', ' + y;
    out.appendChild(p);

    ctx.strokeStyle = "#0f0";
    ctx.stroke();

})();
