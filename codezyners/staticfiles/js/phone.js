var input = document.querySelector( "#phone" );
var validMsg = document.querySelector( "#valid-msg" );
var errorMsg = document.querySelector( "#error-msg" );
var errorMap = [ "Invalid Number", "Invalid Country Code", "Too Short", "Too Long", "Invalid Number" ]

// Country Flags
var iti = intlTelInput( input, {
	initialCountry: 'in',
	nationalMode: true,
	hiddenInput: "phone",
	utilsScript: "https://cdnjs.cloudflare.com/ajax/libs/intl-tel-input/8.4.6/js/utils.js"
} );

var reset = function () {
	input.classList.remove( "error" );
	errorMsg.innerHTML = "";
	errorMsg.classList.add( "hide" );
	validMsg.classList.add( "hide" );
}

input.addEventListener( 'blur', function () {
	if ( input.value.trim() ) {
		if ( iti.isValidNumber() ) {
			validMsg.classList.remove( 'hide' );
		} else {
			input.classList.add( 'error' );
			var errorCode = iti.getValidationError();
			errorMsg.innerHTML = errorMap[ errorCode ];
			errorMsg.classList.remove( 'hide' );
		}
	}
} );

input.addEventListener( 'change', reset );
input.addEventListener( 'keyup', reset );