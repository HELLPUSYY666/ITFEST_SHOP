import React from "react";
import ProductCard from "../components/ProductCard";

const Home = ({ products, addToCart }) => {
  return (
    <div className="home">
      <h1>Наши товары</h1>
      <div className="product-list">
        {products.map((product) => (
          <ProductCard key={product.id} product={product} addToCart={addToCart} />
        ))}
      </div>
    </div>
  );
};

export default Home;
