import Inventory from "./components/Inventory";
import AddItem from "./components/AddItem";
import SearchProduct from "./components/SearchProduct";

function App() {
  return (
    <div className="container">
      <h1>Inventory Management System</h1>

      <AddItem />

      <SearchProduct />

      <Inventory />
    </div>
  );
}

export default App;