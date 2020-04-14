// Smooth Scrolling
$('#menu-container a, .btn').on('click', function(event) {
  if (this.hash !== '') {
    event.preventDefault();

    const hash = this.hash;

    $('html, body').animate(
      {
        scrollTop: $(hash).offset().top - 300 //'-100' allows the titles to be see since the navbar is sticky
      },
      800
    );
  }
});

// sticky menu background
window.addEventListener('scroll', function() {
  if (window.scrollY > 75) {
    document.querySelector('#menu-container').style.opacity = 0.8;
  } else {
    document.querySelector('#menu-container').style.opacity = 1;
  }
});



// Initialise and add the map
function initMap(){
  // your location
  const loc = { lat: 51.520050, lng: -0.087390 };
  // Centered map on location
  const map = new google.maps.Map(document.querySelector('.google')
  , {
    zoom: 14,
    center: loc
  });
  // the marker, positioned at location
  const marker = new google.maps.Marker({ position: loc, map:map});
}


