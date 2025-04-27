let selectedOption = null;
let selectedType = null;

// Called when the user clicks on an option
function selectOption(element, type) {
    // Remove previous selection
    document.querySelectorAll('.option').forEach(opt => opt.classList.remove('selected'));

    // Highlight new selection
    element.classList.add('selected');
    selectedOption = element;
    selectedType = type;
}

// Called when user clicks "Next"
function handleNext() {
    if (!selectedType) {
        alert("Please select a data type before continuing.");
        return;
    }

    // Send extraction request
    fetch('/extract', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ type: selectedType })
    })
    .then(response => response.json())
    .then(data => {
        alert(data.message);
        if (data.redirect) {
            window.location.href = data.redirect;
        }
    })
    .catch(error => {
        console.error('Extraction error:', error);
        alert("An error occurred during extraction.");
    });
}
