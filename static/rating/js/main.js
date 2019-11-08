document.addEventListener('DOMContentLoaded', function() {

    function fill_semicircles(){
        $('.semicircle').removeClass('init')
    }

    $('.semicircle').addClass('init')
    setTimeout(fill_semicircles, 300)


    // toggle
    $(".vote").on( "click", function(e) {
        e.preventDefault()
        // $(this).toggleClass('voted')
        var pk = $(this).data('pk')

        $.ajax({
            type: 'POST',
            async: true,
            url: '/',
            data: {
            	pk: pk, 
            },
            success: function(data) {
                var status = data['status']
                if (status == 'success'){
                    $(this).toggleClass('voted')
                }
                else{
                    alert('You already voted!')
                }
            },
            error: function(){
            	alert("Не робе");
            },
            dataType: 'json',
        });
    });
})