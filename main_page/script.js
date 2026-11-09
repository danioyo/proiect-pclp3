const itemsArray = document.querySelectorAll(".itemCategorii");
const yesbuttton = document.querySelector("#yespopup");
const popup = document.querySelector(".popup");
const categoriiContainer = document.querySelector(".categorii");
const url = "https://the-trivia-api.com/v2/questions?categories=history&limit=10";
itemsArray.forEach(item => {
    item.addEventListener("click", () => {
        popup.style.display = "block";
    });
});

yesbuttton.addEventListener("click", async() => {
    popup.style.display = "none";
    categoriiContainer.innerHTML = "";
    const response = await fetch(url);
    const data = await response.json();
    console.log(data);
    console.log(data[0].question)




    const questionDiv = document.createElement("div");
    questionDiv.classList.add("titluCategorii");
    questionDiv.textContent = "Intrebarea 1";
    categoriiContainer.appendChild(questionDiv);
});
//The Trivia API