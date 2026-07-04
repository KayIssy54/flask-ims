import { useState } from "react";
import { getProduct, addItem } from "../api/inventory";

function SearchProduct() {
  const [barcode, setBarcode] = useState("");
  const [product, setProduct] = useState(null);

  const search = () => {
    getProduct(barcode)
      .then((res) => setProduct(res.data))
      .catch(() => alert("Product not found"));
  };

  const save = () => {
    const price = prompt("Enter Price");
    const stock = prompt("Enter Stock");

    addItem({
      name: product.product_name,
      barcode,
      price,
      stock
    })
      .then(() => {
        alert("Saved!");
        window.location.reload();
      })
      .catch(console.error);
  };

  return (
    <div className="card">

      <h2>OpenFoodFacts Search</h2>

      <input
        placeholder="Barcode"
        value={barcode}
        onChange={(e) => setBarcode(e.target.value)}
      />

      <button onClick={search}>
        Search
      </button>

      {product && (
        <div>

          <h3>{product.product_name}</h3>

          <p>{product.brands}</p>

          <p>{product.ingredients}</p>

          <button onClick={save}>
            Add To Inventory
          </button>

        </div>
      )}

    </div>
  );
}

export default SearchProduct;