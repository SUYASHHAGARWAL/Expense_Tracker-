const navEl=document.querySelector('.navcls');
const navBtn=document.querySelector('.btn');
const home=document.querySelector('#home')
const about=document.querySelector('#about')
const see_demo=document.querySelector('#see-demo')
const contact=document.querySelector('#contact')
const bground=document.querySelector('.container')
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

const sign_btn=document.querySelector('.btn');
const login_area=document.querySelectorAll('.containing');
const close_btn=document.querySelectorAll('.close-btn');
console.log(sign_btn);
sign_btn.addEventListener('click',function(){
    login_area[0].style.display="block";
    
})  
close_btn[0].addEventListener('click',function(){
    login_area[0].style.display="none";
    login_container.style.display="flex";
    signin_container.style.display="none";
    login_area[0].style.transform="rotateY(0deg)";
})
close_btn[1].addEventListener('click',function(){
    login_area[0].style.display="none";
    login_container.style.display="flex";
    signin_container.style.display="none";
    login_area[0].style.transform="rotateY(0deg)";
})

const new_user=document.querySelector('.new-user');
const login_container=document.querySelector('.login-container');
const signin_container=document.querySelector('.signin-container')
new_user.addEventListener('click',function(){
    login_area[0].style.transform="rotateY(180deg)";
    setTimeout(() => {
        login_container.style.display="none";
        signin_container.style.display="flex";
    }, 250);
})