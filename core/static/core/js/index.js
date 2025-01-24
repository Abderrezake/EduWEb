const links = document.querySelectorAll('.modules a');

links.forEach(link => {
  link.addEventListener('click', (event) => {
    event.preventDefault(); // Prevent default link behavior

    links.forEach(otherLink => {
      // Remove active class with animation delay
      otherLink.classList.remove('active');
      setTimeout(() => {
        otherLink.style.animation = 'none'; // Reset animation on inactive links
      }, 200); // Adjust delay based on animation duration (ms)
    });

    // Add active class with animation delay
    setTimeout(() => {
      link.classList.add('active');
    }, 200); // Adjust delay based on animation duration (ms)
  });
});


  // JavaScript code to handle clicks on module links
  document.addEventListener('DOMContentLoaded', function () {
    const moduleLinks = document.querySelectorAll('.modules a');
    moduleLinks.forEach(link => {
      link.addEventListener('click', function (event) {
        event.preventDefault();
        const subject = this.id; // Get the subject from the ID
        const videos = document.querySelectorAll('.video');
        videos.forEach(video => {
          // Hide all videos that don't correspond to the clicked subject
          if (!video.classList.contains(subject)) {
            video.style.display = 'none';
          } else {
            video.style.display = 'block';
          }
        });
      });
    });
  });

// Select all list items
const listItems = document.querySelectorAll(".module .mat");

// Add click event listener to each list item
listItems.forEach(item => {
    item.addEventListener("click", (e) => {
        // Prevent default behavior (navigating to the href)
        e.preventDefault();
        
        // Remove the active class from the currently active item
        const currentActiveItem = document.querySelector(".module .mat.active");
        if (currentActiveItem) {
            currentActiveItem.classList.remove("active");
        }

        // Add the active class to the clicked item
        item.classList.add("active");
    });
}); 

const modulesBox = document.querySelector(".module"),
    moduleList = modulesBox.querySelector(".mat"),
    arrowIcons = document.querySelectorAll(".ic i");

let isDragging = false;

const handleIcons = (scrollVal) => {
    let maxScrollableWidth = modulesBox.scrollWidth - modulesBox.clientWidth;
    arrowIcons[0].parentElement.style.display = scrollVal <= 0 ? "none" : "flex";
    arrowIcons[1].parentElement.style.display = maxScrollableWidth - scrollVal <= 1 ? "none" : "flex";
}

arrowIcons.forEach(icon => {
    icon.addEventListener("click", () => {
        // Si l'icône cliquée est à gauche, réduire 340 de modulesBox scrollLeft, sinon ajouter
        let scrollWidth = modulesBox.scrollLeft += icon.id === "left" ? -340 : 340;
        handleIcons(scrollWidth);
    });
});

moduleList.forEach("click", (e) => {
  mat.addEventListener("click", () => {
    modulesBox.querySelector(".active").classList.remove("active");
    mat.classList.add("active");
});
});

const dragging = (e) => {
    if (!isDragging) return;
    modulesBox.classList.add("dragging");
    modulesBox.scrollLeft -= e.movementX;
    handleIcons(modulesBox.scrollLeft);
}

const dragStop = () => {
    isDragging = false;
    modulesBox.classList.remove("dragging");
}

modulesBox.addEventListener("mousedown", () => isDragging = true);
modulesBox.addEventListener("mousemove", dragging);
document.addEventListener("mouseup", dragStop);


