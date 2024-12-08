import React from "react";

const ProductCard = ({ product, addToCart }) => {
  const handleAddToCart = () => {
    const updatedProduct = { ...product, quantity: 1 };  // Начальное количество = 1
    addToCart(updatedProduct);
  };

  return (
    <div className="product-card">
      <img src={product.imageUrl} alt={product.name} />
      <h3>{product.name}</h3>
      <p>{product.price} ₽</p>
      <button onClick={handleAddToCart}>Добавить в корзину</button>
    </div>
  );
};

export default ProductCard;
