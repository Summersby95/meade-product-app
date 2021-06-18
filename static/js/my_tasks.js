/* jshint esversion: 6 */

// quotable api call to display inspiration quote
$(document).ready(() => {
    $.getJSON("https://api.quotable.io/random?maxLength=100", (data) => {
        quote = data;
        M.toast({
            html: `<i class="material-icons left">chat_bubble</i> ${quote.author} - <i>${quote.content}</i>`,
            displayLength: 10000
        });
    });
});
