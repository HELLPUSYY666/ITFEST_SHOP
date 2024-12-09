import React, { useState, useEffect } from "react";
import { BrowserRouter as Router, Route, Routes, Link } from "react-router-dom";
import Home from "./pages/Home";
import Cart from "./components/Cart";
import './App.css';

const App = () => {
  const [cart, setCart] = useState([]);
  const [products, setProducts] = useState([]);

  useEffect(() => {
    fetch("http://localhost:8000/api/products/")
      .then(response => response.json())
      .then(data => setProducts(data))
      .catch(error => console.error('Error fetching products:', error));
  }, []);

  const addToCart = (product) => {
    fetch(`http://localhost:8000/api/add-to-cart/${product.id}/`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        // добавьте заголовки авторизации, если требуется
      },
      body: JSON.stringify({}),
    })
      .then(response => response.json())
      .then(() => {
        setCart((prevCart) => {
          const existingProductIndex = prevCart.findIndex(item => item.id === product.id);
          if (existingProductIndex >= 0) {
            const updatedCart = [...prevCart];
            updatedCart[existingProductIndex].quantity += 1;
            return updatedCart;
          }
          return [...prevCart, { ...product, quantity: 1 }];
        });
      })
      .catch(error => console.error('Error adding to cart:', error));
  };

  return (
    <Router>
      <div className="app">
        <header>
          <h1>Магазин</h1>
          <nav>
            <Link to="/">Главная</Link> | <Link to="/cart">Корзина</Link>
          </nav>
        </header>

        <Routes>
          <Route
            path="/"
            element={<Home products={products} addToCart={addToCart} />}
          />
          <Route path="/cart" element={<Cart cart={cart} setCart={setCart} />} />
        </Routes>
      </div>
    </Router>
  );
};

export default App;
