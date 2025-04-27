// let checkboxes = document.querySelectorAll(".checkbox");
// let btnProceed = document.querySelector(".btn-proceed");

// btnProceed.addEventListener("click", function () {
//     let anyChecked = false;
//     let selectedTypes = [];

//     checkboxes.forEach(function (checkbox, index) {
//         if (checkbox.classList.contains('completed')) {
//             anyChecked = true;
//             let dataType = checkbox.nextElementSibling.innerText; // Get the data type from the sibling <p>
//             selectedTypes.push(dataType); // Add the selected type to the array
//         }
//     });

//     if (anyChecked) {
//         alert("Extracting data for: " + selectedTypes.join(", "));
//         extractData(selectedTypes); // Call the extraction function with the selected types
//     } else {
//         alert("Please choose at least one option!");
//     }
// });

// checkboxes.forEach(function (value, index) {
//     value.addEventListener("click", function () {
//         this.classList.toggle('completed');
//     });
// });

// function extractData(types) {
//     fetch('/extract', {
//         method: 'POST',
//         headers: {
//             'Content-Type': 'application/json',
//         },
//         body: JSON.stringify({ types: types }), // Send all selected types
//     })
//     .then(response => response.json())
//     .then(data => {
//         alert(data.message);
//     })
//     .catch((error) => {
//         console.error('Error:', error);
//     });
// }
let checkboxes = document.querySelectorAll(".checkbox");
let btnProceed = document.querySelector(".btn-proceed");

btnProceed.addEventListener("click", function () {
    let anyChecked = false;
    let selectedTypes = [];

    checkboxes.forEach(function (checkbox, index) {
        if (checkbox.classList.contains('completed')) {
            anyChecked = true;
            let dataType = checkbox.nextElementSibling.innerText; // Get the data type from the sibling <p>
            selectedTypes.push(dataType); // Add the selected type to the array
        }
    });

    if (anyChecked) {
        alert("Extracting data for: " + selectedTypes.join(", "));
        extractData(selectedTypes); // Call the extraction function with the selected types
    } else {
        alert("Please choose at least one option!");
    }
});

checkboxes.forEach(function (value, index) {
    value.addEventListener("click", function () {
        this.classList.toggle('completed');
    });
});

function extractData(types) {
    fetch('/extract', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ types: types }), // Send all selected types
    })
    .then(response => response.json())
    .then(data => {
        alert(data.message);
    })
    .catch((error) => {
        console.error('Error:', error);
    });
}

