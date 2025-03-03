document.addEventListener("DOMContentLoaded", function () {
    // Open modal and populate form with message data
    document.querySelectorAll(".edit-message-btn").forEach((button) => {
        button.addEventListener("click", function () {
            const messageId = this.dataset.messageId;
            const messageContent = this.dataset.messageContent;

            document.getElementById("editMessageId").value = messageId;
            document.getElementById("editMessageContent").value = messageContent;

            const editModal = new bootstrap.Modal(document.getElementById("editMessageModal"));
            editModal.show();
        });
    });

    // Handle form submission to edit message
    document.getElementById("editMessageForm").addEventListener("submit", async function (event) {
        event.preventDefault();

        const messageId = document.getElementById("editMessageId").value;
        const newMessage = document.getElementById("editMessageContent").value;

        try {
            const response = await fetch("EditMessage/", {
                method: "POST",
                headers: {
                    "Content-Type": "application/x-www-form-urlencoded",
                    "X-CSRFToken": getCSRFToken(),
                },
                body: `message_id=${messageId}&new_message=${encodeURIComponent(newMessage)}`,
            });

            const result = await response.json();
            if (result.success) {
                alert(result.message);
                // Update the message content dynamically on the page
                const messageCell = document.querySelector(`[data-message-id="${messageId}"]`).parentElement;
                messageCell.querySelector("span").textContent = newMessage;
            } else {
                alert(result.message);
            }
        } catch (error) {
            console.error("Error updating message:", error);
            alert("An error occurred while updating the message.");
        }
    });

    // Get CSRF token from cookies
    function getCSRFToken() {
        return document.cookie.split("; ").find(row => row.startsWith("csrftoken="))?.split("=")[1] || "";
    }
});
