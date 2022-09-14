// --------------------- Color Change on Scroll ----------------- //
// //Nav-Item Active
// $( document ).on( "click", "li", function () {
// 	$( this ).addClass( "active" ).siblings().removeClass( "active" )
// } )

// // Change Color on Scroll *WORKING*

// $( window ).scroll( function () {
// 	$( 'header' ).toggleClass( 'scrolling', $( this ).scrollTop() > 800 );
// } );

// ----------------------------- Responsive Navbar --------------------------------- //
const primaryHeader = document.querySelector( ".primary-header" );
const navToggle = document.querySelector( ".mobile-nav-toggle" );
const primaryNav = document.querySelector( ".primary-navigation" );

navToggle.addEventListener( 'click', () => {
	primaryNav.hasAttribute( 'data-visible' ) ?
		navToggle.setAttribute( 'aria-expanded', false ) :
		navToggle.setAttribute( 'aria-expanded', true );
	primaryNav.toggleAttribute( 'data-visible' );
	primaryHeader.toggleAttribute( 'data-overlay' );
} );