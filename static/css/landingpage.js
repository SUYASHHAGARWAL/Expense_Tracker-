const navEl=document.querySelector('.navcls');
const navBtn=document.querySelector('.btn');
const home=document.querySelector('#home')
const about=document.querySelector('#about')
const see_demo=document.querySelector('#see-demo')
const contact=document.querySelector('#contact')

    window.addEventListener('scroll',function(){
        if(window.scrollY>=56){
            navEl.classList.add('navbar-scrolled');
            navBtn.classList.add('btn1');
        }else if(window.scrollY<56){
            navEl.classList.remove('navbar-scrolled');
            navBtn.classList.remove('btn1');
        }
    });

about.addEventListener('click',()=>{
    // window.scrollTo(0,700);
    // var cos=document.querySelector(".section2").offsetTop;
    // console.log(cos)
    // window.scrollTo(0, document.querySelector(".section2").offsetTop-87);
    window.scrollTo({
        top: document.querySelector(".section2").offsetTop-80,
        left: 0,
        behavior: "smooth",
      });
})
home.addEventListener('click',()=>{
    window.scrollTo({
        top: 0,
        left: 0,
        behavior: "smooth",
      });
})
see_demo.addEventListener('click',()=>{
    window.scrollTo({
        top: document.querySelector(".section4").offsetTop-80,
        left: 0,
        behavior: "smooth",
      });
})
contact.addEventListener('click',()=>{
    window.scrollTo({
        top: document.querySelector(".section4").offsetTop-80,
        left: 0,
        behavior: "smooth",
      });
})