import { useState } from "react";
import { updateItem } from "../api/inventory";

function UpdateItem({ item }) {
  const [name, setName] = useState(item.name);
  const [price, setPrice] = useState(item.price);
  const [stock, setStock] = useState(item.stock);

  const handleUpdate = () => {
    updateItem(item.id, {
      name,
      price,
      stock,
    })
      .then(() => {
        alert("Item updated successfully!");
        window.location.reload();
      })
      .catch((err) => {
        console.error(err);
        alert("Failed to update item.");
      });
  };

  return (
    <div style={{ marginTop: "10px" }}>
      <input
        type="text"
        placeholder="Product Name"
        value={name}
        onChange={(e) => setName(e.target.value)}
      />

      <br />


      <input
        type="number"
        placeholder="Price"
        value={price}
        onChange={(e) => setPrice(e.target.value)}
      />

      <br />

      <input
        type="number"
        placeholder="Stock"
        value={stock}
        onChange={(e) => setStock(e.target.value)}
      />

      <br />

      <button onClick={handleUpdate}>
        Update
      </button>
    </div>
  );
}

export default UpdateItem;