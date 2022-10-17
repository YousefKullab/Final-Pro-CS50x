// Make A Photo Gallery In Product Page

var mainImage = document.getElementById('main-image');
var smallImages = document.getElementsByClassName('small-img');

for (let i= 0 ; i < smallImages.length; i++){
    smallImages[i].onclick = function(){
        mainImage.src = smallImages[i].src;
    }
}

