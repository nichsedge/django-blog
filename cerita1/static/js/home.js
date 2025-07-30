var selectActive = -1;


$(document).ready(function () {
    $(".tabcontent").hide();
    $(".bar-click").click(function () {
        const eachStory = document.querySelectorAll(".bar-click");
        for (var i = 0; i < eachStory.length; i++) {
            if (this == eachStory[i]) {
                selectActive = i;
            }
        }
        activateThis(selectActive);
    });

    function activateThis(row) {
        const eachStory = document.querySelectorAll(".bar-click");
        const eachContentStory = document.querySelectorAll(".tabcontent");
        for (var i = 0; i < eachContentStory.length; i++) {
            if (i == selectActive) {
                eachStory[i].style.backgroundColor = "white";
                eachStory[i].style.color = "black";

                eachContentStory[i].style.display = "block";
            } else {
                eachStory[i].style.backgroundColor = "#85671C";
                eachStory[i].style.color = "white";

                eachContentStory[i].style.display = "none";
            }
        }
    }


});

$(window).scroll(function () {
	var sc = $(window).scrollTop()
	if (sc > 150) {
		$("#main-navbar").addClass("navbar-scroll")
	}
	else {
		$("#main-navbar").removeClass("navbar-scroll")
	}
});
