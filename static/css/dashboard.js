const navEl=document.querySelector('.navcls');
// console.log(navEl)
window.addEventListener('scroll',function(){
    if(window.scrollY>=56){
        navEl.classList.add('navbar-scrolled');
    }else if(window.scrollY<56){
        navEl.classList.remove('navbar-scrolled');
    }
});