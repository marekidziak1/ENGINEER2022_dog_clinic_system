function topNavigation() {
    var triggerHamburger = $(".js-menu-trigger-mobile");
    var navTop = $(".js-navigation"); 
    var menuNav = $(".js-menu-mobile"); 

    //operation functions 
    function close() {
        triggerHamburger.removeClass('is-active');
        navTop.removeClass('-opened-menu');
        menuNav.removeClass('-opened');
    }
    function open() {
        triggerHamburger.addClass('is-active');
        navTop.addClass('-opened-menu');
        menuNav.addClass('-opened');
    }

    triggerHamburger.click(function() {
        if (triggerHamburger.hasClass('is-active')){
            close();
        } else {
            open();
        }
    });
}

