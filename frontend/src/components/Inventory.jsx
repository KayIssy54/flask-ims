import { useEffect, useState } from "react";
import {
  getInventory,
  deleteItem,
} from "../api/inventory";

function Inventory() {
  const [items, setItems] = useState([]);

  const loadData = () => {
    getInventory()
      .then((res) => setItems(res.data))
      .catch((err) => console.log(err));
  };

  useEffect(() => {
    loadData();
  }, []);

  const handleDelete = (id) => {
    deleteItem(id).then(() => loadData());
  };

  return (
    <div>
      <h2>Inventory List</h2>

      {items.map((item) => (
        <div key={item.id} style={{ border: "1px solid black", margin: 10, padding: 10 }}>
          <h3>{item.name}</h3>
          <p>Price: {item.price}</p>
          <p>Stock: {item.stock}</p>

          <button onClick={() => handleDelete(item.id)}>
            Delete
          </button>
        </div>
      ))}
    </div>
  );
}

export default Inventory;