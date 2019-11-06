document.addEventListener('DOMContentLoaded', function() {

    function fill_semicircles(){
        $('.semicircle').removeClass('init')
    }

    $('.semicircle').addClass('init')
    

    setTimeout(fill_semicircles, 300)
})