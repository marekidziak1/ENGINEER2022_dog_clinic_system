$(document).ready(function(){
    var swiperTermsCalendar = new Swiper('.js-terms-calendar', {
        //watchOverflow: true,
        // spaceBetween: 0,
        // centeredSlides: true,
        // loop: true,
        slidesPerView: 2,
        // slidesPerGroup: 2,  
        navigation: {
            prevEl: '.js-terms-calendar--prev',
            nextEl: '.js-terms-calendar--next',
        },
        breakpoints: {
            551: {
            slidesPerView: 3,
            slidesPerGroup: 4,
            // spaceBetween: 60,
            },
            850: {
            slidesPerView: 4,
            slidesPerGroup: 4,
            //spaceBetween: 30,
            },
            1024: {
            slidesPerView: 4,
            slidesPerGroup: 4,
            //spaceBetween: 30,
            },
            1201: {
            slidesPerView: 4,
            slidesPerGroup: 4,
                //spaceBetween: 30,
            },
        }             
     });
});