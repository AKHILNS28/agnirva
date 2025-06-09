const products = 
[
    { id: 1, name: "Laptop", price: 899, image: "images/laptop.webp" },
    { id: 2, name: "Headphones", price: 199, image: "images/headphone.webp" },
    { id: 3, name: "Smartphone", price: 699, image: "images/smartphone.webp" },
    { id: 4, name: "Camera", price: 499, image: "images/camera.webp" },
];
const productList = document.getElementById("productList");
function displayProducts(products) 
{
    productList.innerHTML = "";
    products.forEach((product) => {
        const productDiv = document.createElement("div");
        productDiv.className = "product";
        productDiv.innerHTML = `
            <img src="${product.image}" alt="${product.name}">
            <h3>${product.name}</h3>
            <p>$${product.price}</p>
            <button onclick="addToCart(${product.id})">Add to Cart</button>
        `;
        productList.appendChild(productDiv);
    });
}
displayProducts(products);
const searchBar = document.getElementById("searchbar");
searchBar.addEventListener("input", (e) => {
    const searchTerm = e.target.value.toLowerCase();
    const filteredProducts = products.filter(product =>
        product.name.toLowerCase().includes(searchTerm)
    );
    displayProducts(filteredProducts);
});