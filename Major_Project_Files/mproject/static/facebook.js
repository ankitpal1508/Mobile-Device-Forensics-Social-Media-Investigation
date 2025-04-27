document.addEventListener('DOMContentLoaded', function () {
    const checkboxes = document.querySelectorAll(".checkbox");
    const btnProceed = document.querySelector(".btn-proceed");
    const progressBarContainer = document.querySelector('.progress-container');
    const progressBar = document.getElementById('progress-bar');
    const progressText = document.getElementById('progress-text');
    let selectedOption = null;

    checkboxes.forEach(function (checkbox) {
        checkbox.addEventListener("click", function () {
            checkboxes.forEach(cb => cb.classList.remove('completed'));
            this.classList.add('completed');
            const label = this.closest('.option').querySelector('p').innerText.trim();
            selectedOption = label;
        });
    });

    btnProceed.addEventListener("click", function () {
        if (!selectedOption) {
            alert("Please select one option!");
            return;
        }

        // Show and reset progress
        let progress = 0;
        progressBar.style.width = "0%";
        progressBarContainer.style.display = "block";
        progressText.innerText = "0%";

        // Randomized progress simulation
        function updateProgress() {
            if (progress >= 100) {
                progressText.innerText = "100%";
                setTimeout(() => {
                    progressBarContainer.style.display = "none";
                    progressText.innerText = "";

                    // Call backend after load complete
                    fetch("http://127.0.0.1:5000/open-folder", {
                        method: "POST",
                        headers: {
                            "Content-Type": "application/json"
                        },
                        body: JSON.stringify({ type: selectedOption })
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

            const increment = Math.floor(Math.random() * 15) + 5; // 5–20% step
            const delay = Math.floor(Math.random() * 400) + 200;  // 200–600ms delay
            progress = Math.min(progress + increment, 100);
            progressBar.style.width = progress + "%";
            progressText.innerText = progress + "%";

            setTimeout(updateProgress, delay);
        }

        updateProgress(); // start loading
    });
});
