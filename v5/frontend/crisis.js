document.addEventListener("DOMContentLoaded", function () {
    const form = document.getElementById("crisis-form");
    const tableBody = document.getElementById("reports-body");

    // ✅ Function to Submit Form Data to Backend
    form.addEventListener("submit", async (event) => {
        event.preventDefault();

        const report = {
            crisisType: document.getElementById("crisis-cause").value.trim(),
            location: document.getElementById("Location").value.trim(),
            severity: document.getElementById("severity-level").value.trim(),
            description: document.getElementById("description").value.trim()
        };

        if (!report.crisisType || !report.location || !report.severity || !report.description) {
            alert("⚠️ Please fill in all fields!");
            return;
        }

        try {
            const response = await fetch("http://localhost:5000/api/reports", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify(report),
            });

            const data = await response.json();
            if (!response.ok) throw new Error(data.message || "Failed to submit report");

            form.reset(); // ✅ Clear form fields
            loadReports(); // ✅ Refresh the report table
        } catch (error) {
            console.error("❌ Error submitting report:", error);
            alert("❌ Submission failed. Check console for details.");
        }
    });

    // ✅ Function to Fetch Reports from Backend
    async function loadReports() {
        tableBody.innerHTML = "";
        try {
            const response = await fetch("http://localhost:5000/api/reports");
            if (!response.ok) throw new Error("Failed to fetch reports");

            const reports = await response.json();
            reports.forEach(report => {
                const row = `<tr>
                    <td>${report.crisisType}</td>
                    <td>${report.location}</td>
                    <td>${report.severity}</td>
                    <td>${report.description}</td>
                </tr>`;
                tableBody.innerHTML += row;
            });
        } catch (error) {
            console.error("❌ Error fetching reports:", error);
            alert("❌ Could not load reports. Check console for details.");
        }
    }

    loadReports(); // ✅ Load reports when page loads
});
