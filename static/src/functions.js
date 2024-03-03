// Function to reset the user's answer
function resetAnswer() {
    document.getElementById("input-box").value = "";
}

function submitForm() {
    document.getElementById("submission").submit();

    // Make a POST request to the Flask route
    fetch('/submit', {
        method: 'POST',
        body: new URLSearchParams({
            'user_guess': userGuess
        }),
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
    })
    .then(response => response.json())
    .then(data => {
        // Display feedback
        document.getElementById("feedback").innerText = data.feedback;
    })
    .catch(error => {
        console.error('Error:', error);
    });
}