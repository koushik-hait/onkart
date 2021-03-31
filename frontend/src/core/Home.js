import {React,  useState, useEffect } from "react";
import {getProducts} from "./helper/coreapicalls"
import "../styles.css";
import Base from "./Base";
import Card from "./Card";



export default function Home() {
  const [products, setProducts] = useState([]);
  const [error, setError] = useState(false);

  const loadAllProducts = () => {
    getProducts()
    .then((data) => {
      if(data.error){
        setError(data.error);
        console.log(error);
      } else {
        setProducts(data);
      }
    })
  };

  useEffect(() => {
    loadAllProducts();
     // eslint-disable-next-line
  },[]);

  return (
      <Base title="onkart home page" description="Home onkart store">
      <div className="row">
          <h1>Products</h1>
          {/* <h4>{product.catagory.name}</h4> */}
        {products.map((product, index) => {
          return (
            <div key={index} className="col-4 mb-4">
              <Card product={product}/>
            </div>
          );
        })}
      </div>
      </Base>
  );
}
