$(document).ready(() => {
    $("#talkbubble").hide();
    $(document).on("click", "#phone", () => {
        $("#talkbubble").toggle("slow");
    })
});