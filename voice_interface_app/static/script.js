/* voice_interface_app/static/script.js */
const spokenText = document.getElementById('spokenText');
const outputText = document.getElementById('outputText');
const listenButton = document.getElementById('listenButton');

const recognition = new webkitSpeechRecognition(); // For Chrome

listenButton.addEventListener('click', () => {
    listenButton.disabled = true;
    listenButton.textContent = 'Listening...';
    recognition.start();
});

recognition.onresult = (event) => {
    const spokenText = event.results[0][0].transcript;
    // You can now send the spokenText to the server using AJAX or any other method.
};
