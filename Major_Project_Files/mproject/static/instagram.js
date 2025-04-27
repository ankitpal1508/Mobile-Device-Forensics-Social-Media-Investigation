document.addEventListener('DOMContentLoaded', function () {
    const checkboxes = document.querySelectorAll(".checkbox");
    const btnProceed = document.querySelector(".btn-proceed");
    const progressBarContainer = document.querySelector('.progress-container');
    const progressBar = document.getElementById('progress-bar');
    const progressText = document.getElementById('progress-text');
    let selectedOption = null;

    // Event listener for click on option (checkbox click)
    checkboxes.forEach(function (checkbox) {
        checkbox.addEventListener("click", function () {
            const icon = this.querySelector('i');
            
            // Toggle between checked and unchecked states
            if (icon.classList.contains("fa-circle")) {
                icon.classList.remove("fa-circle");
                icon.classList.add("fa-check-circle");
                this.classList.add('completed');
            } else {
                icon.classList.remove("fa-check-circle");
                icon.classList.add("fa-circle");
                this.classList.remove('completed');
            }

            // Set the selected option text
            const label = this.closest('.option').querySelector('p').innerText.trim();
            selectedOption = label;
        });
    });

    // Button proceed click event
    btnProceed.addEventListener("click", function () {
        if (!selectedOption) {
            alert("Please select one option!");
            return;
        }

        let progress = 0;
        progressBar.style.width = "0%";
        progressBarContainer.style.display = "block";
        progressText.innerText = "0%";

        function updateProgress() {
            if (progress >= 100) {
                progressText.innerText = "100%";
                setTimeout(() => {
                    progressBarContainer.style.display = "none";
                    progressText.innerText = "";

                    fetch("http://127.0.0.1:5000/open-folder", {
                        method: "POST",
                        headers: {
                            "Content-Type": "application/json"
                        },
                        body: JSON.stringify({ type: selectedOption, platform: "Instagram" }) // Optional: distinguish source
                    })
                    .then(res => res.json())
                    .then(data => {
                        alert(data.message || data.error);
                    })
                    .catch(err => {
                        console.error(err);
                        alert("Something went wrong!");
                    });
                }, 500);
                return;
            }

            const increment = Math.floor(Math.random() * 15) + 5;
            const delay = Math.floor(Math.random() * 400) + 200;
            progress = Math.min(progress + increment, 100);
            progressBar.style.width = progress + "%";
            progressText.innerText = progress + "%";

            setTimeout(updateProgress, delay);
        }

        updateProgress();
    });
});
