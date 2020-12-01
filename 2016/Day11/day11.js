/*
CG = cobalt generator
CC = cobalt-compatible microchip

UG = curium generator
UC = curium-compatible microchip

PG = plutonium generator
PC = plutonium-compatible microchip

OG = promethium generator
OC = promethium-compatible microchip

RG = ruthenium generator
RC = ruthenium-compatible microchip

The first floor contains a promethium generator and a promethium-compatible microchip.
The second floor contains a cobalt generator, a curium generator, a ruthenium generator, and a plutonium generator.
The third floor contains a cobalt-compatible microchip, a curium-compatible microchip, a ruthenium-compatible microchip, and a plutonium-compatible microchip.
The fourth floor contains nothing relevant


Test:

The first floor contains a hydrogen-compatible microchip and a lithium-compatible microchip.
The second floor contains a hydrogen generator.
The third floor contains a lithium generator.
The fourth floor contains nothing relevant.

HG = hydrogen generator
HC = hydrogen-compatible microchip

LG = lithium generator
LC = lithium-compatible microchip

*/

var currFloor = 0;
var moves = [];
var floors = [
    ['HC','LC'],
    ['HG'],
    ['LG'],
    [],
];

var press = false;
while(currFloor != 3 && floors[3].length < 4) {
    press = false;
    for(var i = 0; !press && i < floors[currFloor].length; i++) {
        var generators = floors[currFloor].filter(function(s) { return s.endsWith('G')});
        var chips = floors[currFloor].filter(function(s) { return s.endsWith('C')});
        var payload = [];
        // Kolla nästa våning

    }
}