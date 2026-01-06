const optionAButton = document.getElementById("optionA");
const optionBButton = document.getElementById("optionB");
const resultsDiv = document.getElementById("results");

const API_URL = "http://localhost:5000";

optionAButton.addEventListener("click", () => vote("option_a"));
optionBButton.addEventListener("click", () => vote("option_b"));

async function vote(option) {
    try {
        await fetch(`${API_URL}/vote`, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ vote: option }),
        });
        getResults();
    } catch (error) {
        console.error("Error voting:", error);
        resultsDiv.innerHTML = "<p>Could not submit vote.</p>";
    }
}

async function getResults() {
    try {
        const response = await fetch(`${API_URL}/results`);
        const data = await response.json();
        resultsDiv.innerHTML = `
            <p>Python: ${data.option_a}</p>
            <p>JavaScript: ${data.option_b}</p>
        `;
    } catch (error) {
        console.error("Error getting results:", error);
        resultsDiv.innerHTML = "<p>Could not fetch results.</p>";
    }
}

getResults();
