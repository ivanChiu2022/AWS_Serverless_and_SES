document.addEventListener("DOMContentLoaded", function () {
    const form = document.getElementById("contactForm");
    const result = document.getElementById("result");

    if (!form) {
        console.error("contactForm not found");
        return;
    }

    form.addEventListener("submit", async function (e) {
        e.preventDefault();

        const data = {
            name: document.getElementById("name").value.trim(),
            email: document.getElementById("email").value.trim(),
            subject: document.getElementById("subject").value.trim(),
            description: document.getElementById("message").value.trim()
        };

        try {
            const response = await fetch(
                "https://xxxxxxxx.execute-api.ca-central-1.amazonaws.com/xxxxxxxx", /*Your api key*/
                {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json"
                    },
                    body: JSON.stringify(data)
                }
            );

            const responseText = await response.text();
            console.log("HTTP status:", response.status);
            console.log("Response body:", responseText);

            if (response.ok) {
                alert("Your email has been sent to Ivan Chiu.");
                form.reset();
                if (result) {
                    result.innerText = "Message sent successfully.";
                }
            } else {
                alert("Failed to send message. Please try again later.");
                if (result) {
                    result.innerText = "Failed to send message. " + responseText;
                }
            }
        } catch (error) {
            console.error("Error sending message:", error);
            alert("Network error. Check browser console.");
            if (result) {
                result.innerText = "Network error. Check browser console.";
            }
        }
    });
});
