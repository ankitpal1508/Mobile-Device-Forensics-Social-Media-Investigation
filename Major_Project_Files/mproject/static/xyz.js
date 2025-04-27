document.addEventListener('DOMContentLoaded', function () {
    let checkboxes = document.querySelectorAll(".checkbox");
    let btnProceed = document.querySelector(".btn-proceed");
    let selectedDataTypes = [];

    // Checkbox click to toggle 'completed' class and track selection
    checkboxes.forEach(function (checkbox) {
        checkbox.addEventListener("click", function () {
            this.classList.toggle('completed');
            let dataType = this.closest('.option').querySelector('p').innerText;

            // Add or remove from selected data types based on toggle state
            if (this.classList.contains('completed')) {
                if (!selectedDataTypes.includes(dataType)) {
                    selectedDataTypes.push(dataType);
                }
            } else {
                selectedDataTypes = selectedDataTypes.filter(item => item !== dataType);
            }
        });
    });

    // Proceed button click to extract data for the selected options
    btnProceed.addEventListener("click", function () {
        if (selectedDataTypes.length > 0) {
            alert("Options selected! Proceeding with extraction...");

            // Trigger the data extraction for each selected data type
            selectedDataTypes.forEach(dataType => {
                extractData(dataType);
            });
        } else {
            alert("Please choose at least one option!");
        }
    });

    // Function to send selected data type to the server
    function extractData(type) {
        fetch('/extract', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ type: type }),  // Send one type at a time
        })
        .then(response => response.json())
        .then(data => {
            alert(data.message);  // Display server response
        })
        .catch((error) => {
            console.error('Error:', error);
        });
    }
});
