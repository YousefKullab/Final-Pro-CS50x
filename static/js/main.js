// Make A Photo Gallery In Product Page

var mainImage = document.getElementById('main-image');
var smallImages = document.getElementsByClassName('small-img');

for (let i= 0 ; i < smallImages.length; i++){
    smallImages[i].onclick = function(){
        mainImage.src = smallImages[i].src;
    }
}


// Get the button Top:

let mybutton = document.getElementById("myBtn");

window.onscroll = function() {scrollFunction()};

function scrollFunction() {
  if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
    mybutton.style.display = "block";
  } else {
    mybutton.style.display = "none";
  }
}

function topFunction() {
  document.body.scrollTop = 0; 
  document.documentElement.scrollTop = 0; 
}

// Note Hover Navbar >>> Highlight
