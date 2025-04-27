// // 
// let app=document.querySelectorAll(".App button")
// app.forEach(function(value,index)
// {
//     value.addEventListener("click",function()
// {
//     alert("Please connect your phone then proceed")
// })
// })
// document.addEventListener('DOMContentLoaded', (event) => {
//     let isDeviceConnected = false;

//     document.getElementById('connectButton').addEventListener('click', async () => {
//         try {
//             const device = await navigator.usb.requestDevice({ filters: [] });
//             if (device) {
//                 alert('Your phone is connected');
//                 isDeviceConnected = true;
//                 document.getElementById('redirectButton').disabled = false;
//             }
//         } catch (error) {
//             console.error('There was an error connecting to the device:', error);
//         }
//     });

//     document.getElementById('redirectButton').addEventListener('click', () => {
//         if (isDeviceConnected) {
//             window.location.href = 'WhatappData.html';
//         } else {
//             alert('Please connect your phone');
//         }
//     });
// });

document.addEventListener('DOMContentLoaded', () => {
    document.getElementById('connectButton').addEventListener('click', async () => {
        try {
            const device = await navigator.usb.requestDevice({ filters: [] });
            if (device) {
                alert('Your device is connected');

                // Update the text and remove hover effect
                const headingElement = document.querySelector('.hovertext');
                if (headingElement) {
                    headingElement.textContent = 'Thanks for connecting your device';

                    // Switch to the no-hover class
                    headingElement.classList.remove('hovertext');
                    headingElement.classList.add('no-hovertext');
                }
            }
        } catch (error) {
            console.error('Error connecting to the device:', error);
        }
    });
});
// Function to check if the device is connected using Web USB API
// Function to check if Web USB API is supported


// Function to check if the device is connected using Web USB API
async function isDeviceConnected() {
    if (!isWebUsbSupported()) {
        console.log('Web USB is not supported by this browser.');
        alert('Web USB API is not supported on your browser. Please try with Chrome or update your browser.');
        return false;
    }

    try {
        const devices = await navigator.usb.getDevices(); // Get list of connected USB devices
        console.log('Connected devices:', devices); // Log devices for debugging
        if (devices.length > 0) {
            console.log('Device connected:', devices);
            return true; // Return true if devices are detected
        } else {
            console.log('No devices connected.');
        }
    } catch (error) {
        console.error('Error checking device connection:', error);
    }

    return false; // Return false if no devices are connected
}

// Handle the SELECT button click
document.getElementById('selectButton').addEventListener('click', async () => {
    const deviceConnected = await isDeviceConnected(); // Check if a device is connected

    if (deviceConnected) {
        alert('Device is connected! Redirecting...');
        console.log('Device is connected');
        // Redirect to another page if the device is connected
        window.location.href = 'MainPage.html';
    } else {
        alert('Please connect your phone first');
        console.log('Device is not connected');
    }
});

// Simulate device connection by making the thank-you message visible (optional for manual testing)
// document.getElementById('thankYouMessage').style.display = 'block'; // Uncomment to simulate connection


// Simulate device connection by making the thank-you message visible (for testing)
// Uncomment the following line to simulate the device being connected:
// document.getElementById('thankYouMessage').style.display = 'block'; // Simulate connection