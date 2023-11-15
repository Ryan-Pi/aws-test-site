function w3_open() {
    document.getElementById("mySidebar").style.display = "block";
    document.getElementById("myOverlay").style.display = "block";
  }
   
  function w3_close() {
    document.getElementById("mySidebar").style.display = "none";
    document.getElementById("myOverlay").style.display = "none";
  }
  
  // Modal Image Gallery
//   function onClick(element) {
//     document.getElementById("img01").src = element.src;
//     document.getElementById("modal01").style.display = "block";
//     var captionText = document.getElementById("caption");
//     captionText.innerHTML = element.alt;
//   }

const count = document.getElementById("counter");
async function updateCounter(){
    const response = await fetch("https://2tsvlc6ueyzsmxekqgsimzi3ye0wkvfz.lambda-url.ap-southeast-2.on.aws/");
    const data = await response.json();
    count.innerHTML = `Hello! You are Visitor ${data}!`;
}
updateCounter();