/* jshint esversion: 6 */

// validates correct role/department combination selected
$(document).ready(() => {
    $("#role").change(() => {
        if ($("#role").val() == "Commercial") {
            $("#department").prop('disabled', false);
            $("#department option[value='All']").prop('disabled', true);
            $("#department option[value='Fruit']").prop('selected', true);
        } else {
            $("#department").prop('disabled', true);
            $("#department option[value='All']").prop('selected', true);
        }
        $("#department").formSelect();
    });
});