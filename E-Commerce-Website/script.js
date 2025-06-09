let products = [];
let cart = [];

const productList = document.getElementById("productList");
const searchBar = document.getElementById("searchbar");

function displayProducts(productArray) {
    productList.innerHTML = "";
    productArray.forEach((product) => {
        const productDiv = document.createElement("div");
        productDiv.className = "product";
        productDiv.innerHTML = `
            <img src="${product.image}" alt="${product.name}">
            <h3>${product.name}</h3>
            <p>$${product.price}</p>
            <button onclick="addToCart(${Number(product.id)})">Add to Cart</button>
        `;
        productList.appendChild(productDiv);
    });
}

function addToCart(productId) {
    const product = products.find(p => Number(p.id) === productId);
    if (product) {
        const alreadyInCart = cart.some(item => Number(item.id) === productId);
        if (!alreadyInCart) {
            cart.push(product);
            alert(`${product.name} added to the cart!`);
            viewCart();
        } else {
            alert(`${product.name} is already in the cart.`);
        }
    }
}

function viewCart() {
    const cartList = document.getElementById("cartList");
    cartList.innerHTML = ""; // Clear cart display

    cart.forEach((item) => {
        const cartItem = document.createElement("div");
        cartItem.className = "cart-item";
        cartItem.innerHTML = `
            <h3>${item.name}</h3>
            <p>Price: $${item.price}</p>
            <button onclick="removeFromCart(${Number(item.id)})">Remove</button>
        `;
        cartList.appendChild(cartItem);
    });

    const total = cart.reduce((sum, item) => sum + item.price, 0);
    document.getElementById("totalPrice").textContent = `Total: $${total}`;
}

function removeFromCart(productId) {
    cart = cart.filter(item => Number(item.id) !== productId);
    viewCart();
}

searchBar.addEventListener("input", (e) => {
    const searchTerm = e.target.value.toLowerCase();
    const filteredProducts = products.filter(product =>
        product.name.toLowerCase().includes(searchTerm)
    );
    displayProducts(filteredProducts);
});
document.addEventListener('DOMContentLoaded', function () {
    fetch('http://localhost:3000/products')
        .then(response => response.json())
        .then(data => {
            products = data;
            displayProducts(products);
            viewCart();  // initialize cart display on load
        })
        .catch(err => {
            console.error("Failed to load products from server:", err);
        });
});

document.getElementById("checkoutButton").addEventListener("click", () => {
    if (cart.length === 0) {
        alert("Your cart is empty!");
        return;
    }
    alert("Thank you for your purchase!");
    cart = [];
    viewCart();
});