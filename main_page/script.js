const itemsArray = document.querySelectorAll(".itemCategorii");
const yesbuttton = document.querySelector("#yespopup");
const popup = document.querySelector(".popup");
const categoriiContainer = document.querySelector(".categorii");

itemsArray.forEach(item => {
    item.addEventListener("click", () => {
        popup.style.display = "block";
    });
});

yesbuttton.addEventListener("click", () => {
    popup.style.display = "none";
    categoriiContainer.innerHTML = "";
    
    const questionDiv = document.createElement("div");
    questionDiv.classList.add("titluCategorii");
    questionDiv.textContent = "Intrebarea 1";
    categoriiContainer.appendChild(questionDiv);
});
//The Trivia API