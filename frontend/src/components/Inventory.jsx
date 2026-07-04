import { useEffect, useState } from "react";
import {
  getInventory,
  deleteItem,
} from "../api/inventory";
import UpdateItem from "./UpdateItem";

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
        <div key={item.id} className="card">
          <h3>{item.name}</h3>

          <p><strong>Barcode:</strong> {item.barcode}</p>

          <p><strong>Price:</strong> Ksh {item.price}</p>

          <p><strong>Stock:</strong> {item.stock}</p>

          <UpdateItem item={item} />

          <button onClick={() => handleDelete(item.id)}>
            Delete
          </button>
        </div>
      ))}
    </div>
  );
}

export default Inventory;