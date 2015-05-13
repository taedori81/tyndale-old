$(function() {
   $('#side-menu').sticky({topSpacing: 60});

    $(window).scroll(function(){
        if($(document).scrollTop() > 50) {
            $('nav').addClass('shrink');
        } else {
            $('nav').removeClass('shrink');
        }
    });
});