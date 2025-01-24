function toggleMenu() {
  const menu = document.querySelector(".menu-links");
  const icon = document.querySelector(".hamburger-icon");
  menu.classList.toggle("open");
  icon.classList.toggle("open");
}
 

var timeSets = [];

$(function () {
    var isMouseDown = false;
    $("#timeTable td")
            .mousedown(function () {
                isMouseDown = true;
                $(this).toggleClass("highlighted");                  
                return false; 
            })
            .mouseover(function () {
                if (isMouseDown) {
                    $(this).toggleClass("highlighted");                        
                }
            });
    $(document).mouseup(function () {
                isMouseDown = false;
            });
    $('#btn-save-TS').on('click', function () {
        saveTimeSave();
    });        
});

var saveTimeSave = function () {
    for (i = 1; i < 8; i++) {
        for (j = 0; j < 24; j++) {
            if ($("#" + i + "" + j).css("backgroundColor") == "rgb(135, 206, 235)") {
                if (timeSets.indexOf(i + "" + j) == -1) {
                    timeSets.push(i + "" + j);
                }
            }else{
                realIndex = timeSets.indexOf(i + "" + j);
                if (realIndex != -1) {
                    timeSets.splice(realIndex, 1);
                }
            }
        }
    }
    console.log(timeSets.valueOf());    
};


$(document).ready(function(){				

  $("#follow-button").click(function(){
    if ($("#follow-button").text() == "+ Follow"){
      // *** State Change: To Following ***      
      // We want the button to squish (or shrink) by 10px as a reaction to the click and for it to last 100ms    
      $("#follow-button").animate({ width: '-=10px' }, 100, 'easeInCubic', function () {});
      
      // then now we want the button to expand out to it's full state
      // The left translation is to keep the button centred with it's longer width
      $("#follow-button").animate({ width: '+=45px', left: '-=15px' }, 600, 'easeInOutBack', function () { 
        $("#follow-button").css("color", "#fff");
        $("#follow-button").text("Following");

        // Animate the background transition from white to green. Using JQuery Color
        $("#follow-button").animate({
          backgroundColor: "#2EB82E",
          borderColor: "#2EB82E"
        }, 1000 );
      });
    }else{
      
      // *** State Change: Unfollow ***     
      // Change the button back to it's original state
      $("#follow-button").animate({ width: '-=25px', left: '+=15px' }, 600, 'easeInOutBack', function () { 
        $("#follow-button").text("+ Follow");
        $("#follow-button").css("color", "#3399FF");
        $("#follow-button").css("background-color", "#ffffff");
        $("#follow-button").css("border-color", "#3399FF");
      });
    }
  }); 
});