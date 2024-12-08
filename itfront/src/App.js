import React, { useState } from "react";
import { BrowserRouter as Router, Route, Routes, Link } from "react-router-dom";
import Home from "./pages/Home";
import Cart from "./components/Cart";
import './App.css';
import { beer } from "./img/beer.jpeg"
import { burger}  from "./img/burger_01.jpg"
import { fries}  from "./img/fries_preview.jpg"

const App = () => {
  const [cart, setCart] = useState([]);
  
  const products = [
    { id: 1, name: "BEER", price: 85, imageUrl: { beer }  },
    { id: 2, name: "BURGER", price: 300, imageUrl: { burger } },
    { id: 3, name: "FRIES", price: 100, imageUrl: { fries } },
  ];

  const addToCart = (product) => {
    setCart((prevCart) => {
      const existingProductIndex = prevCart.findIndex(item => item.id === product.id);
      if (existingProductIndex >= 0) {
        const updatedCart = [...prevCart];
        updatedCart[existingProductIndex].quantity += 1;
        return updatedCart;
      }
      return [...prevCart, product];
    });
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
