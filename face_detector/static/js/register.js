$(document).ready(() => {
    $("form input").on("input", e => {
        if(e.target.value === ''){
            $(`#${e.target.getAttribute('name')}`).transition({
                'font-size': '1.75vh',
                'margin-bottom': '-7.5vh',
            }, 500);
        }
        else{
            $(`#${e.target.getAttribute('name')}`).transition({
                'font-size': '1vh',
                'margin-bottom': '-6vh',
            }, 500);
        }        
    });
    $("#fileUpload").on("input", () => {
        $("#uploadText") !== undefined ? $("#uploadText").remove() : '';
        $("#post_image").after(`<span id='uploadText'>${$("#fileUpload").val()}</span>`)
    });
    $(document).on("click", "#submit", () => {
        setTimeout(() => {
            $(".popup").remove();
        }, 2000);
    });
});