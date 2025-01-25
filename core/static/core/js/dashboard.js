// add hovered class to selected list item
let list = document.querySelectorAll(".navigation li");
// messages
function activeLink() {
  list.forEach((item) => {
    item.classList.remove("hovered");
  });
  this.classList.add("hovered");
}

list.forEach((item) => item.addEventListener("mouseover", activeLink));

// Menu Toggle
let toggle = document.querySelector(".toggle");
let navigation = document.querySelector(".navigation");
let main = document.querySelector(".main");

toggle.onclick = function () {
  navigation.classList.toggle("active");
  main.classList.toggle("active");
};

function toggleSection(sectionId) {
  // Hide all sections
  var sections = document.getElementsByClassName("section");
  for (var i = 0; i < sections.length; i++) {
    sections[i].style.display = "none";
  }

  // Show the selected section
  var section = document.getElementById(sectionId);
  if (section) {
    section.style.display = "block";
  }
}

// Appel de la fonction toggleSection avec l'ID de la section "Profile" pour l'afficher par défaut
toggleSection("profile");

// Ajoutez cet événement de clic à l'élément de navigation "Profile"
var profileLink = document.querySelector('.nav-link[data-target="profile"]');
profileLink.addEventListener("click", function () {
  toggleSection("profile");
});

// Événement de clic pour l'élément de navigation "Messages"
var messagesLink = document.querySelector('.nav-link[data-target="messages"]');
messagesLink.addEventListener("click", function () {
  toggleSection("messages");
});

// Événement de clic pour l'élément de navigation "Settings"
var settingsLink = document.querySelector('.nav-link[data-target="settings"]');
settingsLink.addEventListener("click", function () {
  toggleSection("settings");
});

// Événement de clic pour l'élément de navigation "Sign Out"
var signOutLink = document.querySelector('.nav-link[data-target="sign-out"]');
signOutLink.addEventListener("click", function () {
  toggleSection("sign-out");
});

// chat section

var messageInput = document.getElementById("message-input");
var sendButton = document.getElementById("send-button");
var imageUploadInput = document.getElementById("image-upload");
var chatContainer = document.querySelector(".msg-page");

function sendMessage() {
  var message = messageInput.value.trim();
  var file = imageUploadInput.files[0];

  if (message !== "" || file) {
    var outgoingChat = document.createElement("div");
    outgoingChat.classList.add("outgoing-chats");

    var html = `
      <div class="outgoing-chats-img">
        <img src="./assets/imgs/customer01.jpg" />
      </div>
      <div class="outgoing-msg">
        <div class="outgoing-chats-msg">
    `;

    if (message !== "") {
      html += `
        <p>${message}</p>
      `;
    }

    if (file) {
      var reader = new FileReader();
      reader.onload = function (e) {
        html += `
          <img class="uploaded-image" style="height:150px; width: 300px; border-radius: 5px;" src="${e.target.result}" />
        `;
        finishSendMessage(outgoingChat, html);
      };
      reader.readAsDataURL(file);
    } else {
      finishSendMessage(outgoingChat, html);
    }
  }
}

function finishSendMessage(outgoingChat, html) {
  html += `
    <span class="time">${getCurrentTime()}</span>
  </div>
  </div>
  `;

  outgoingChat.innerHTML = html;
  chatContainer.appendChild(outgoingChat);
  messageInput.value = "";
  imageUploadInput.value = "";
  chatContainer.scrollTop = chatContainer.scrollHeight;
}

sendButton.addEventListener("click", sendMessage);
messageInput.addEventListener("keydown", function (event) {
  if (event.key === "Enter") {
    sendMessage();
  }
});

function getCurrentTime() {
  var date = new Date();
  var currentDate = new Date().toLocaleDateString("fr-FR");

  var hours = date.getHours();
  var minutes = date.getMinutes();
  var ampm = hours >= 12 ? "PM" : "AM";
  hours = hours % 12 || 12;
  minutes = minutes < 10 ? "0" + minutes : minutes;

  var today = new Date().toLocaleDateString("fr-FR");
  var messageDate = currentDate === today ? "Aujourd'hui" : currentDate;

  return hours + ":" + minutes + " " + ampm + " | " + messageDate;
}
