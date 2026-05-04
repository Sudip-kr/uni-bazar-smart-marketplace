console.log("Uni Bazar loaded successfully!");

document.addEventListener("DOMContentLoaded", function () {
    const locationType = document.getElementById("id_location_type");
    const hostelField = document.getElementById("id_hostel_name");

    if (locationType && hostelField) {
        const hostelContainer = hostelField.closest(".col-md-6");

        function toggleHostelField() {
            if (locationType.value === "day_scholar") {
                hostelContainer.style.display = "none";
                hostelField.value = "";
            } else {
                hostelContainer.style.display = "block";
            }
        }

        toggleHostelField();
        locationType.addEventListener("change", toggleHostelField);
    }
});

window.addEventListener("load", function () {
    const preloader = document.getElementById("preloader");
    if (preloader) {
        setTimeout(() => {
            preloader.classList.add("hide");
        }, 2000); 
    }
});

