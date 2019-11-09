document.addEventListener('DOMContentLoaded', function() {

    function fill_semicircles(){
        $('.semicircle').removeClass('init')
    }

    $('.semicircle').addClass('init')
    setTimeout(fill_semicircles, 300)


    // toggle
    $(".vote").on( "click", function(e) {
        e.preventDefault()
        var btn = $(this)
        var pk = btn.data('pk')

        $.ajax({
            type: 'POST',
            async: true,
            url: '/',
            data: {
            	pk: pk, 
            },
            success: function(data) {
                var status = data['status']
                var new_amount = data['amount']
                if (status == 'success'){
                    btn.addClass('voted')
                }
                else if (status == 'removed'){
                    btn.removeClass('voted')
                }
                btn.find('span').text(new_amount)
            },
            error: function(){
            	alert("Не робе");
            },
            dataType: 'json',
        });
    });
})