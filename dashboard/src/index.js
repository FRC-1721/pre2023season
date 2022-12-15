"use strict";
import * as $ from "jquery";
import * as d3 from "d3";

const WHEEL_PORT_X = 52 + 50 / 2;
const WHEEL_STARBOARD_X = 296 + 50 / 2;
const WHEEL_FORE_Y = 25 + 75 / 2;
const WHEEL_AFT_Y = 230 + 75 / 2;

// make these packages visible to the networktables helpers, too
window.$ = $;
window.d3 = d3;
var canvas;
var drawingContext;

$(document).ready(function () {

    // sets a function that will be called when the websocket connects/disconnects
    NetworkTables.addWsConnectionListener(onNetworkTablesConnection, true);

    // sets a function that will be called when the robot connects/disconnects
    NetworkTables.addRobotConnectionListener(onRobotConnection, true);
});

function onRobotConnection(connected) {
    $('#robotstate').text(connected ? "Connected!" : "Disconnected");
    $('#robotAddress').text(connected ? NetworkTables.getRobotAddress() : "disconnected");
}

function onNetworkTablesConnection(connected) {

    if (connected) {
        $("#connectstate").text("Connected!");

        // clear the table
        $("#nt tbody > tr").remove();

        console.log(NetworkTables.getKeys())

    } else {
        $("#connectstate").text("Disconnected!");
    }
}
