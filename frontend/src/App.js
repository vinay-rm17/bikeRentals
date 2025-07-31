import React, { useState, useEffect } from "react";
import axios from "axios";
import "./App.css";

const App = () => {
  const [bikes, setBikes] = useState([]);
  const [searchQuery, setSearchQuery] = useState("");
  const [priceFilter, setPriceFilter] = useState("");

  useEffect(() => {
    fetchBikes();
  }, []);

  const fetchBikes = async () => {
    try {
      const res = await axios.get("http://127.0.0.1:8000/bikes");
      setBikes(res.data);
    } catch (error) {
      console.error("Error fetching bikes:", error);
    }
  };

  const filteredBikes = bikes.filter((bike) => {
    const matchesSearch = bike["Bike Name"]
      .toLowerCase()
      .includes(searchQuery.toLowerCase());
    const matchesPrice =
      priceFilter === "" || bike["Price (₹)"] <= parseInt(priceFilter);
    return matchesSearch && matchesPrice;
  });
  const providerURLs = {
  "Royal Brothers": "https://www.royalbrothers.com/coorg/bike-rentals",
  "Screaming Eagle Co": "https://screamingeagles.co/",
  "srmbikes": "https://www.srmbikes.com/",
  "TopGear Bike Rentals": "https://topgearbikerentals.com/"
};
  
  return (
    <div className="container">
      <h1 className="title">🚴 Bike Rental Service</h1>

      {/* Search and Filter */}
      <div className="filters">
        <input
          type="text"
          placeholder="Search bikes..."
          value={searchQuery}
          onChange={(e) => setSearchQuery(e.target.value)}
          className="search-input"
        />

        <select
          value={priceFilter}
          onChange={(e) => setPriceFilter(e.target.value)}
          className="price-filter"
        >
          <option value="">All Prices</option>
          <option value="500">Below ₹500</option>
          <option value="1000">Below ₹1000</option>
          <option value="2000">Below ₹2000</option>
        </select>
      </div>

      {/* Bike Cards */}
      <div className="bike-list">
  {filteredBikes.length > 0 ? (
    filteredBikes.map((bike, index) => {
      const url = providerURLs[bike["Provider"]] || "#"; // ✅ Moved inside map
      return (
        <div className="bike-card" key={index}>
          <div className="bike-image-container">
            <img
              src={`/images/${bike["Bike Name"].split(" ")[0].toLowerCase()}.jpg`}
              onError={(e) => {
                e.target.onerror = () => {
                  e.target.onerror = null;
                  e.target.src = "/images/default-bike.jpeg"; // final fallback
                };
                e.target.src = `/images/${bike["Bike Name"].split(" ")[0].toLowerCase()}.jpeg`;
              }}
              alt={bike["Bike Name"]}
              className="bike-image"
            />
          </div>
          <h2>{bike["Bike Name"]}</h2>
          <p>
            <strong>Price:</strong> ₹{bike["Price (₹)"]}
          </p>
          <p>
            <strong>Provider:</strong> {bike["Provider"]}
          </p>
          <a href={url} target="_blank" rel="noopener noreferrer">
            <button className="book-btn">Book Now</button>
          </a>
        </div>
      );
    })
  ) : (
    <p className="no-data">No bikes match your search.</p>
  )}
</div>

      </div>
  );
    };
export default App;
