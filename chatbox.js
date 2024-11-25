// Chatbot responses
const responses = {
  default: "I'm here to help. Can you tell me more about how you're feeling?",
  happy: "That's wonderful to hear! Keep spreading positivity!",
  sad: "I'm sorry you're feeling sad. Sometimes talking to a trusted friend or practicing self-care can help.",
  anxious: "Feeling anxious can be tough. Deep breathing and grounding exercises can often provide relief.",
  stressed: "Stress is challenging. Taking small breaks and focusing on one task at a time might help.",
  angry: "It's okay to feel angry sometimes. Try to channel your energy into something productive, like exercise or art.",
  lonely: "Loneliness is tough. Consider reaching out to someone you trust or engaging in a hobby you enjoy.",
  confused: "It's okay to feel confused. Try breaking down the situation into smaller parts—it might clarify things.",
  excited: "That's great! Channel that energy into something creative or productive.",
  frustrated: "Frustration happens. Take a step back and approach the problem with a fresh perspective.",
  tired: "Feeling tired? A short nap, some hydration, or stepping outside for fresh air might help.",
  scared: "Feeling scared can be overwhelming. Talk to someone you trust or try to focus on what you can control.",
};

const sendButton = document.getElementById("send-btn");
const userInput = document.getElementById("user-input");
const chatWindow = document.getElementById("chat-window");

sendButton.addEventListener("click", function () {
  const message = userInput.value.trim();
  if (message) {
    // Display the user's message
    chatWindow.innerHTML += `<div class="message user-message">${message}</div>`;
    userInput.value = ""; // Clear the input field

    // Determine the bot's response
    let response = responses.default; // Default response
    const lowerMessage = message.toLowerCase();

    if (lowerMessage.includes("happy")) {
      response = responses.happy;
    } else if (lowerMessage.includes("sad")) {
      response = responses.sad;
    } else if (lowerMessage.includes("anxious")) {
      response = responses.anxious;
    } else if (lowerMessage.includes("stressed")) {
      response = responses.stressed;
    } else if (lowerMessage.includes("angry")) {
      response = responses.angry;
    } else if (lowerMessage.includes("lonely")) {
      response = responses.lonely;
    } else if (lowerMessage.includes("confused")) {
      response = responses.confused;
    } else if (lowerMessage.includes("excited")) {
      response = responses.excited;
    } else if (lowerMessage.includes("frustrated")) {
      response = responses.frustrated;
    } else if (lowerMessage.includes("tired")) {
      response = responses.tired;
    } else if (lowerMessage.includes("scared")) {
      response = responses.scared;
    }

    // Display the bot's response
    chatWindow.innerHTML += `<div class="message bot-message">${response}</div>`;

    // Scroll to the bottom of the chat window
    chatWindow.scrollTop = chatWindow.scrollHeight;
  }
});
