$(function() {
   $('#side-menu').sticky({topSpacing: 60});

    $(window).scroll(function(){
        if($(document).scrollTop() > 50) {
            $('nav').addClass('shrink');
        } else {
            $('nav').removeClass('shrink');
        }
    });


    $( '#cbp-qtrotator' ).cbpQTRotator();

    new WOW().init();

    $("html").niceScroll({
        scrollspeed: 100,
		mousescrollstep: 38,
		cursorwidth: 5,
		cursorborder: 0,
		cursorcolor: '#333',
		autohidemode: true,
		zindex: 999999999,
		horizrailenabled: false,
		cursorborderradius: 0,
        touchbehavior:true,
        cursordragontouch: true,
    });
});