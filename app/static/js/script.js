document.addEventListener("DOMContentLoaded", function () {
    // Create Sparkling Stars Effect
    const starsContainer = document.querySelector('.stars');

    for (let i = 0; i < 100; i++) {
        let star = document.createElement("span");
        star.classList.add("star"); 
        star.style.top = Math.random() * 100 + "vh"; 
        star.style.animationDuration = Math.random() * 3 + 2 + "s"; 
        star.style.animationDelay = Math.random() * 2 + "s";
        star.style.left = Math.random() * 100 + "vw"; 
        starsContainer.appendChild(star);
    }
});
