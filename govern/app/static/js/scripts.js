var carouselWidth = $(".title-col")[0].scrollWidth;
var cardWidth = $(".home-carousel-item").width();
var scrollPosition = 0;

$(".carousel-control-next").on("click", function () {
    if (scrollPosition < (carouselWidth - (cardWidth * 4))) { //check if you can go any further
        scrollPosition += cardWidth;  //update scroll position
        $(".title-col").animate({ scrollLeft: scrollPosition }, 600); //scroll left
    }
});

$(".carousel-control-prev").on("click", function () {
    if (scrollPosition > 0) {
        scrollPosition -= cardWidth;
        $(".title-col").animate({ scrollLeft: scrollPosition },600);
    }
});
