

// js for background animation
var sliderImg = document.getElementById("slideImg");

var images = new Array(
    "image/img6.png",
    "image/team2.jpg",
    "image/img7.jpg",
);
var len = images.length; 
var i = 0;
function slider(){
    if(i > len-1){
        i = 0;
    }
    sliderImg.src = images[i];
    i++;
    setTimeout('slider()',6000); 
}

// for preloading
var loader = document.getElementById("preloader");

window.addEventListener("load", function(){
    loader.style.display = "none";
})

// for translator
function googleTranslateElementInit() { 
    new google.translate.TranslateElement(
        {pageLanguage: 'en'}, 
        'google_translate_element'
    ); 
} 

// js for hidding menu on media screen

// for showing balance
function bars(){
    let bars = document.getElementById("bars");
    let cancel = document.getElementById("cancel");
    let board_nav = document.getElementById("board_nav");

    if(bars.style.display === "none"){
        bars.style.display = "block";
        board_nav.style.display = "block";
    }
    else{
        bars.style.display = "none";
        cancel.style.display = "block";
        board_nav.style.display = "block";
    }
}

// for hiding balance
function cancel(){
    let bars = document.getElementById("bars");
    let cancel = document.getElementById("cancel");
    let board_nav = document.getElementById("board_nav");

    if(cancel.style.display === "none"){
        cancel.style.display = "block";
        board_nav .style.display = "block";
    }
    else{
        bars.style.display = "block";
        cancel.style.display = "none";
        board_nav .style.display = "none";
    }
}



// js for hidding account balance

// for showing balance
// function show(){
//     let balance_open = document.getElementById("balance_open");
//     let balance_close = document.getElementById("balance_close");
//     let hide = document.getElementById("hide");
//     let show = document.getElementById("show");

//     if(show.style.display === "none"){
//         show.style.display = "block";
//         balance_open.style.display = "block";
//     }
//     else{
//         show.style.display = "none";
//         hide.style.display = "block";
//         balance_open.style.display = "block";
//         balance_close.style.display = "none";
//     }
// }

// for hiding balance
// function hide(){
//     let balance_open = document.getElementById("balance_open");
//     let balance_close = document.getElementById("balance_close");
//     let hide = document.getElementById("hide");
//     let show = document.getElementById("show");

//     if(hide.style.display === "none"){
//         hide.style.display = "block";
//         balance_close .style.display = "block";
//     }
//     else{
//         show.style.display = "block";
//         hide.style.display = "none";
//         balance_close .style.display = "block";
//         balance_open .style.display = "none";
//     }
// }

