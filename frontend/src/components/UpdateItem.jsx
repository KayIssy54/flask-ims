import { useState } from "react";
import { updateItem } from "../api/inventory";

function UpdateItem({ item }) {
  const [price, setPrice] = useState(item.price);
  const [stock, setStock] = useState(item.stock);

  const handleUpdate = () => {
    updateItem(item.id, {
      price,
      stock
    })
      .then(() => {
        alert("Updated!");
        window.location.reload();
      })
      .catch(console.error);
  };

  return (
    <>
      <input
        value={price}
        onChange={(e) => setPrice(e.target.value)}
      />

      <input
        value={stock}
        onChange={(e) => setStock(e.target.value)}
      />

      <button onClick={handleUpdate}>
        Update
      </button>
    </>
  );
}

export default UpdateItem;