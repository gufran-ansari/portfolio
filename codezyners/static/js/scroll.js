// ------------------------- Scroll Tracker ------------------------- //

import 'https://flackr.github.io/scroll-timeline/dist/scroll-timeline.js';

const scrollTracker = document.querySelector( ".scroll-tracker" );

const scrollTrackingTimeline = new ScrollTimeline( {
	source: document.scrollingElement,
	orientation: "block",
	scrollOffsets: [ CSS.percent( 0 ), CSS.percent( 100 ) ],
} );

scrollTracker.animate( {
	transform: [ "scaleX(0)", "scaleX(1)" ],
}, {
	duration: 1,
	timeline: scrollTrackingTimeline,
} );

// ------------------------- Scroll Tracker ------------------------- //



// ------------------------- Scroll Animation ------------------------- //

const observer = new IntersectionObserver( ( entries ) => {
	entries.forEach( ( entry ) => {
		if ( entry.isIntersecting ) {
			entry.target.classList.add( 'show' );
		} else {
			entry.target.classList.remove( 'show' );
		}
	} );
} );

const hiddenElements = document.querySelectorAll( '.hidden' );
hiddenElements.forEach( ( el ) => observer.observe( el ) );

// ------------------------- Scroll Animation ------------------------- //