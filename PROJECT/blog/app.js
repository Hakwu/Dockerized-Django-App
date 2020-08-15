$(document).ready(function() {
    $('.updateButton').on('click', function() {
        var email = $('#form.email').val();
        req = $.ajax({
            url : '/profile',
            type : 'POST',
            data : { email : email }
        });
    });
});
