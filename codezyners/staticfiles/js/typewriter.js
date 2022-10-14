const TypeWriter = function ( txtElement, words, wait = 3000 ) {
    this.txtElement = txtElement;
    this.words = words;
    this.txt = "";
    this.wordIndex = 0;
    this.wait = parseInt( wait, 8 );
    this.type();
    this.isDeleting = false;
}

// Type Method
TypeWriter.prototype.type = function () {
    // Current index of word
    const current = this.wordIndex % this.words.length

    // Get full text of current word
    const fullTxt = this.words[ current ];

    // Check if deleting
    if ( this.isDeleting ) {
        // Remove Character
        this.txt = fullTxt.substring( 0, this.txt.length - 1 );
    } else {
        // Add Character
        this.txt = fullTxt.substring( 0, this.txt.length + 1 );
    }
    // Insert txt into Element
    this.txtElement.innerHTML = `<span class="txt">${ this.txt }</span>`;

    // Initial Type Speed
    let typeSpeed = 300;
    if ( this.isDeleting ) {
        //It will divide typeSpeed by 2.
        typeSpeed = typeSpeed / 2;
    }

    // If word is complete
    if ( !this.isDeletinge && this.txt === fullTxt ) {
        // Make pause at end
        typeSpeed = this.wait;
        // set is deleting to True
        this.isDeleting = true;
    } else if ( this.isDeleting && this.txt === '' ) {
        this.isDeleting = false;
        // Move to next word
        this.wordIndex++;
        // Pause before start typing
        typeSpeed = 500;
    }
    setTimeout( () => this.type(), typeSpeed );
}


// Init on DOM Load
document.addEventListener( 'DOMContentLoaded', init );

// Init App
function init() {
    const txtElement = document.querySelector( ".txt-type" );
    const words = JSON.parse( txtElement.getAttribute( 'data-words' ) );
    const wait = txtElement.getAttribute( 'data-wait' )

    // Init TypeWriter
    new TypeWriter( txtElement, words, wait );
}