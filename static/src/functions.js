// Function to reset the user's answer
function resetAnswer() {
    document.getElementById("input-box").value = "";
}

// Function to update the "Feedback" and "Score" sections dynamically
// function submitForm() {
//     var form = document.getElementById('submission');
//     var formData = new FormData(form);

//     var xhr = new XMLHttpRequest();
//     xhr.open('POST', '/submit', true);
//     xhr.onload = function() {
//         if (xhr.status === 200) {
//             var response = JSON.parse(xhr.responseText);
//             document.getElementById('feedback').innerText = response.feedback;
//             if (response.feedback === "That's right!") {
//                 document.getElementById('score').innerText = response.score;
//                 setTimeout(function() {
//                     resetAnswer();
//                     loadNextQuestion();
//                 }, 3000);
//             }

//         }
//     };
//     xhr.send(formData);
// }

// Function to update the "Feedback" and "Score" sections dynamically
function submitForm() {
    var form = document.getElementById('submission');
    var formData = new FormData(form);

    var xhr = new XMLHttpRequest();
    xhr.open('POST', '/submit', true);
    xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
    xhr.onload = function() {
        if (xhr.status === 200) {
            var response = JSON.parse(xhr.responseText);
            document.getElementById('feedback').innerText = response.feedback;
            if (response.feedback === "That's right!") { // This if statement will update the function and resets the input box after 3 seconds if an answer is correct.
                document.getElementById('score').innerText = response.score;
                setTimeout(function() {
                    resetAnswer();
                    document.getElementById('question').innerText = response.question;
                    }, 3000);
            }
            
        }
    };
    xhr.send(new URLSearchParams(formData)); // Send form data as URLSearchParams
}