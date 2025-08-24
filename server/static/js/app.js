document.addEventListener("DOMContentLoaded", () => {
  const locationSelect = document.getElementById("location");
  const resultDiv = document.getElementById("result");
  const form = document.getElementById("prediction-form");

  // Modal
  const modal = document.getElementById("errorModal");
  const closeBtn = document.querySelector(".close");
  const errorMessage = document.getElementById("errorMessage");

  closeBtn.onclick = () => modal.style.display = "none";
  window.onclick = (event) => { if (event.target === modal) modal.style.display = "none"; };

  // Fetch locations
  fetch("/get_location_names")
    .then(res => res.json())
    .then(data => {
      data.locations.forEach(loc => {
        const option = document.createElement("option");
        option.value = loc;
        option.textContent = loc;
        locationSelect.appendChild(option);
      });
    });

  // Form submit
  form.addEventListener("submit", (e) => {
    e.preventDefault();

    const sqft = parseFloat(document.getElementById("sqft").value);
    const bhk = parseInt(document.getElementById("bhk").value);
    const bath = parseInt(document.getElementById("bath").value);
    const location = document.getElementById("location").value;

    // Validation
    if (sqft <= 0 || bhk <= 0 || bath <= 0) {
      errorMessage.textContent = "Please enter valid positive values for Sqft, BHK, and Bathrooms.";
      modal.style.display = "block";
      return;
    }

    fetch("/predict_home_price", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ sqft, bhk, bath, location })
    })
    .then(res => res.json())
    .then(data => {
  resultDiv.textContent = `Estimated Price: ₹ ${data.estimated_price} Lakhs`;
  resultDiv.classList.add("show");

    });
  });
});
