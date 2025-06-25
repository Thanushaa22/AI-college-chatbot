function sendMessage() {
    const input = document.getElementById("userInput");
    const userMsg = input.value.trim();
    const messages = document.getElementById("messages");

    if (userMsg === "") return;

    // Show user's message
    messages.innerHTML += `<div class="message user">${userMsg}</div>`;
    input.value = "";

    // Typing indicator
    const typing = document.createElement("div");
    typing.className = "message bot typing";
    typing.innerText = "Bot is typing...";
    messages.appendChild(typing);
    messages.scrollTop = messages.scrollHeight;

    fetch("/get", {
        method: "POST",
        headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
        body: `msg=${encodeURIComponent(userMsg)}`
    })
    .then(res => res.json())
    .then(data => {
        typing.remove();
        messages.innerHTML += `<div class="message bot">${data.reply}</div>`;
        messages.scrollTop = messages.scrollHeight;
    })
    .catch(() => {
        typing.remove();
        messages.innerHTML += `<div class="message error">Oops! Something went wrong.</div>`;
    });
}
