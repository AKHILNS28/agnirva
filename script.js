document.addEventListener("DOMContentLoaded", () => 
    {
    const button = document.createElement("button");
    button.textContent = "Click Me!";

    button.addEventListener("click", () => 
        {
        // Show an alert when the button is clicked
        alert("Thanks for visiting my portfolio!");
    });

    document.body.appendChild(button);
});