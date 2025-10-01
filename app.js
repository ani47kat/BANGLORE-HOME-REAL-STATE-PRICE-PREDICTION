
function getBathValue() {
    const uiBathrooms = document.getElementsByName("uiBathrooms");
    for (let i = 0; i < uiBathrooms.length; i++) {
        if (uiBathrooms[i].checked) {
            return parseInt(uiBathrooms[i].value);
        }
    }
    return -1; 
}


function getBHKValue() {
    const uiBHK = document.getElementsByName("uiBHK");
    for (let i = 0; i < uiBHK.length; i++) {
        if (uiBHK[i].checked) {
            return parseInt(uiBHK[i].value);
        }
    }
    return -1; 
}


function onClickedEstimatePrice() {
    const sqft = document.getElementById("uiSqft").value;
    const bhk = getBHKValue();
    const bathrooms = getBathValue();
    const location = document.getElementById("uiLocations").value;
    const estPrice = document.getElementById("uiEstimatedPrice");

    fetch("http://127.0.0.1:5000/predict_home_price", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            total_sqft: sqft,
            bhk: bhk,
            bath: bathrooms,
            location: location
        })
    })
    .then(response => response.json())
    .then(data => {
        if (data.estimated_price !== undefined) {
            estPrice.innerHTML = `<h2>${data.estimated_price} Lakh</h2>`;
        } else {
            estPrice.innerHTML = `<h2>Could not estimate price</h2>`;
        }
    })
    .catch(error => {
        console.error("Error while estimating price:", error);
        estPrice.innerHTML = `<h2>Error estimating price</h2>`;
    });
}


function onPageLoad() {
    const uiLocations = document.getElementById("uiLocations");

    fetch("http://127.0.0.1:5000/get_location_names")
        .then(response => response.json())
        .then(data => {
           
            if (Array.isArray(data.locations)) {
              
                uiLocations.innerHTML = '<option disabled selected>Choose a Location</option>';
                
                data.locations.forEach(location => {
                    const option = document.createElement("option");
                    option.value = location;
                    option.textContent = location;
                    uiLocations.appendChild(option);
                });
            } else {
                console.error("Locations data is not an array:", data.locations);
            }
        })
        .catch(error => {
            console.error("Error fetching locations:", error);
            const errorOption = document.createElement("option");
            errorOption.textContent = "Failed to load locations";
            errorOption.disabled = true;
            uiLocations.appendChild(errorOption);
        });
}

window.onload = onPageLoad;
