import { useState } from "react";
import { addItem } from "../api/inventory";

function AddItem() {
  const [form, setForm] = useState({
    name: "",
    barcode: "",
    price: "",
    stock: ""
  });

  const handleChange = (e) => {
    setForm({
      ...form,
      [e.target.name]: e.target.value
    });
  };

  const handleSubmit = (e) => {
    e.preventDefault();

    addItem(form)
      .then(() => {
        alert("Item Added!");

        setForm({
          name: "",
          barcode: "",
          price: "",
          stock: ""
        });

        window.location.reload();
      })
      .catch(console.error);
  };

  return (
    <div className="card">
      <h2>Add Product</h2>

      <form onSubmit={handleSubmit}>
        <input
          name="name"
          placeholder="Product Name"
          value={form.name}
          onChange={handleChange}
        />

        <input
          name="barcode"
          placeholder="Barcode"
          value={form.barcode}
          onChange={handleChange}
        />

        <input
          name="price"
          placeholder="Price"
          value={form.price}
          onChange={handleChange}
        />

        <input
          name="stock"
          placeholder="Stock"
          value={form.stock}
          onChange={handleChange}
        />

        <button>Add Item</button>
      </form>
    </div>
  );
}

export default AddItem;