/* jshint esversion: 6 */

$(document).ready(function() {
    let canvas = document.getElementById("signature-pad");

    canvas.height = 200;
    canvas.width = canvas.offsetWidth;

    let signaturePad = new SignaturePad(canvas);


});