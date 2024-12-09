import React from "react";

const Home = ({ products, addToCart }) => {
  return (
    <div className="product-list">
      {products.map((product) => (
        <div key={product.id} className="product">
          <h2>{product.name}</h2>
          <img src={product.image_url} alt={product.name} />
          <p>Цена: {product.price} руб.</p>
          <button onClick={() => addToCart(product)}>Добавить в корзину</button>
        </div>
      ))}
    </div>
  );
};

export default Home;
