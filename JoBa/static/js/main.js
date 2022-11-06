// Make A Photo Gallery In Product Page

var mainImage = document.getElementById('main-image');
var smallImages = document.getElementsByClassName('small-img');

for (let i= 0 ; i < smallImages.length; i++){
    smallImages[i].onclick = function(){
        mainImage.src = smallImages[i].src;
    };
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
};

function topFunction() {
  document.body.scrollTop = 0; 
  document.documentElement.scrollTop = 0; 
};

// Send Email  

function sendEmail() {
    var params ={
      name: document.getElementById("name").value,
      email: document.getElementById("email").value,
      message: document.getElementById("message").value
    };

    const serviceID = "service_ja2h26f";
    const templateID = "template_tvg0ivi";
    emailjs.send(serviceID, templateID, params)
    .then(
      res =>{
        document.getElementById("name").value = "";
        document.getElementById("email").value = "";
        document.getElementById("message").value = "";
        console.log(res);
        alert("Your Message Sent Successfully");
      })
    .catch((res) => console.log(err));
};

// Note Hover Navbar >>> Highlight ??????????????????????????????

// Delete Product 

function deleteProduct(productId){
  fetch("/delete-product",{
      method: "POST",
      body: JSON.stringify({productId : productId})
  }).then((_res) =>{
      window.location.href = "/cart"
  });
}



