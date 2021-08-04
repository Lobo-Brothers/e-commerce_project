var slides = document.querySelectorAll('.slide');
var buttons = document.querySelectorAll('.btn');
const currentSlide = 1;

var manualNav = function(manual){
    slides.forEach((slide) => {
        slide.classList.remove('active');

        buttons.forEach((btn) => {
            btn.classList.remove('active');
        });
    });
    slides[manual].classList.add('active');
    buttons[manual].classList.add('active');
}

buttons.forEach((btn, i) => {
    btn.addEventListener("click", () => {
        manualNav(i);
        currentSlide = i;
    });
});

var repeat = function(activeClass){
    let active = document.getElementsByClassName('active');
    let i = 1;

    var repeater = () => {
        setTimeout(function(){
            [...active].forEach((activeSlide) => {
                activeSlide.classList.remove('active');
            })

            slides[i].classList.add('active');
            buttons[i].classList.add('active');
            i++;

            if(slides.length == i){
                i = 0;
            }
            if(i >= slides.lenght){
                return;
            }
            repeater();
        }, 10000);
    }
    repeater();
}
repeat();