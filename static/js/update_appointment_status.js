document.addEventListener("DOMContentLoaded", function () {
    // Attach event listener for status change
    document.querySelectorAll(".status-dropdown").forEach((dropdown) => {
        dropdown.addEventListener("change", async function () {
            const appointmentId = this.dataset.appointmentId;
            const newStatus = this.value;

            try {
                const response = await fetch("UpdateStatus/", {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/x-www-form-urlencoded",
                        "X-CSRFToken": getCSRFToken(),
                    },
                    body: `appointment_id=${appointmentId}&status=${newStatus}`,
                });

                const result = await response.json();
                if (result.success) {
                    updateStatusBadge(appointmentId, newStatus);
                    alert("Status updated successfully!");
                } else {
                    alert(result.message);
                }
            } catch (error) {
                console.error("Error updating status:", error);
                alert("An error occurred while updating the status.");
            }
        });
    });

    // Update the status badge color dynamically
    function updateStatusBadge(appointmentId, newStatus) {
        const badge = document.getElementById(`status-badge-${appointmentId}`);
        badge.textContent = newStatus.charAt(0).toUpperCase() + newStatus.slice(1);

        // Update badge color
        badge.className = "badge";
        if (newStatus === "pending") {
            badge.classList.add("bg-warning");
        } else if (newStatus === "confirmed") {
            badge.classList.add("bg-success");
        } else if (newStatus === "cancelled") {
            badge.classList.add("bg-danger");
        }
    }

    // Get CSRF token from cookies
    function getCSRFToken() {
        return document.cookie.split("; ").find(row => row.startsWith("csrftoken="))?.split("=")[1] || "";
    }
});
