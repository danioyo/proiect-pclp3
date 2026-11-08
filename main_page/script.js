
const itemsArray = document.querySelectorAll(".itemCategorii");
const yesbuttton = document.querySelector("#yespopup");

itemsArray.forEach(item => {
    item.addEventListener("click", ()=>{
        const popup = document.querySelector(".popup");
        popup.style.display = "block";
    })
});
yesbuttton.addEventListener("click", ()=>{
    document.querySelector(".categorii").style.display = "none";
})
//The Trivia API