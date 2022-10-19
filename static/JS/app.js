// create function 
const navSlide = function(){
    // select burger div and nav div from the DOM
    const burger = document.querySelector(".burger");
    console.log(burger)
    const nav = document.querySelector(".nav-links");
    console.log(nav)
    // select all the links
    const navLinks = nav.querySelectorAll(".nav-links li");

  

//toggle navigation
burger.addEventListener('click', function(){
    nav.classList.toggle("nav-active");


     navLinks.forEach((link, index) => {
       // console.log(link, index);
       if(link.style.animation === true){
        link.style.animation ='';
       }else{
          //animate link
          link.style.animation =`navLinkFade 0.5s ease forwards ${index / 7 + 0.2}s`
       }

     });

     // burger animation
     burger.classList.toggle("toggle")
});


}
navSlide()

// product filter section starts 19/07/2022
const btns = document.querySelectorAll(".btn");
console.log(btns)
const blogItems = document.querySelectorAll('.card-itms');
console.log(blogItems)

for(let i = 0; i < btns.length; i++ ){
btns[i].addEventListener('click',function(e){
  e.preventDefault()
  const filter = e.target.dataset.filter


// create foreach loop
blogItems.forEach((blogItem) => {
  if(filter === 'all'){
    blogItem.style.display = 'flex';
     btns[4].classList.remove('active')
     btns[1].classList.remove('active')
     btns[2].classList.remove('active')
     btns[3].classList.remove('active')


     btns[0].classList.add('active')
     btns[0].style.color ='antiquewhite'

  } else{

    btns[0].classList.remove('active')

    if(blogItem.classList.contains(filter)){
      blogItem.style.display = 'flex';

if(btns[1] === e.target){
  btns[1].classList.add('active')
}else{
  btns[1].classList.remove('active')
}
if(btns[2] === e.target){
  btns[2].classList.add('active')
}else{
  btns[2].classList.remove('active')
}
if(btns[3] === e.target){
  btns[3].classList.add('active')
}else{
  btns[3].classList.remove('active')
}
if(btns[4] === e.target){
  btns[4].classList.add('active')
}else{
  btns[4].classList.remove('active')
}

    }
    else{
        blogItem.style.display = 'none';
    }
  }

  

})

})
}




// product filter section ends

// SEARCH FILTER

const search = document.querySelector('#search');
search.addEventListener("keyup", (e) => {
  e.preventDefault()
  const searchValue = search.value.toLowerCase().trim();
console.log(searchValue)
// loop through blog category
for (let i = 0; i < blogItems.length; i++) {
  console.log(searchValue)
  if(blogItems[i].classList.contains(searchValue)) {
    blogItems[i].style.display = 'flex';
  }else if(searchValue === ""){
    blogItems[i].style.display = 'flex';
  }else{
    blogItems[i].style.display = 'none';
  }
}



})


