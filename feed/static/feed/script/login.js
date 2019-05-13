var wasSignIn = true;

$(document).ready(() => {

    // Exchange the form for registered and non-registered users.
    $('#form-signup').hide();
    $('#radio-yes').change(e => {
        if ($('#radio-yes').is(':checked') && !wasSignIn) {
            $('#form-signup').fadeOut(300, () => {
                $('#form-signin').fadeIn(300);
            });
            wasSignIn = true;
        }
    });
    $('#radio-no').change(e => {
        if ($('#radio-no').is(':checked') && wasSignIn) {
            $('#form-signin').fadeOut(300, () => {
                $('#form-signup').fadeIn(300);
            });
            wasSignIn = false;
        }
    });

    $('#form-signup').submit(e => {
        if ($('#signupInputPassword').val() !== $('#signupInputRepassword').val()) {
            $('#signupInputRepassword')[0].setCustomValidity('The passwords do not match.');
            e.preventDefault();
        }
    });
});
