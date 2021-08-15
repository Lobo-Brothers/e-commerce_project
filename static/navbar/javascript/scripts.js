// burguer menu
const toggleBtn = document.getElementById('navbar-toggler');
const navDiv = document.querySelector('.navbar-collapse');

toggleBtn.addEventListener('click', function(){
    navDiv.classList.toggle('showNav');
    if(toggleBtn.firstElementChild.className = "fas fa-bars fa-fw"){
        document.body.style.overflow = "hidden";
    } else{
        toggleBtn.firstElementChild.className = "fas fa-bars fa-fw";
        document.body.style.overflow = "visible";
    }
});

// search box

const icon = document.getElementById('search-btn');
const search = document.getElementById('search');

icon.onclick = function(){
    search.classList.toggle('active')
}
