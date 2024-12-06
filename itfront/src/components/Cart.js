import React from "react";

const Cart = ({ cart, setCart }) => {
  const handleQuantityChange = (index, newQuantity) => {
    const updatedCart = [...cart];
    updatedCart[index].quantity = newQuantity;
    setCart(updatedCart);
  };

  const handleRemoveItem = (index) => {
    const updatedCart = cart.filter((_, i) => i !== index);
    setCart(updatedCart);
  };

  const getTotalPrice = () => {
    return cart.reduce((total, item) => total + item.price * item.quantity, 0);
  };

  return (
    <div className="cart">
      <h2>Корзина</h2>
      {cart.length === 0 ? (
        <p>Корзина пуста</p>
      ) : (
        <div>
          {cart.map((item, index) => (
            <div key={index} className="cart-item">
              <img src={item.imageUrl} alt={item.name} />
              <div className="item-details">
                <p>{item.name} - {item.price} ₽</p>
                <input
                  type="number"
                  value={item.quantity}
                  min="1"
                  onChange={(e) => handleQuantityChange(index, parseInt(e.target.value))}
                />
                <button onClick={() => handleRemoveItem(index)}>Удалить</button>
              </div>
            </div>
          ))}
          <div>
            <h3>Общая сумма: {getTotalPrice()} ₽</h3>
            <button>Перейти к оплате</button>
          </div>
        </div>
      )}
    </div>
  );
};

export default Cart;
