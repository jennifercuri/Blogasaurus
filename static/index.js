console.log("hello world")

  let gradfriends = document.getElementById("mouseover");
  gradfriends.addEventListener("mouseover", func);
  gradfriends.addEventListener("mouseout", func1);

  function func()
    {
      gradfriends.setAttribute("style", "width:400px")
      gradfriends.setAttribute('style', "height:400px")
    }

  function func1()
    {
      gradfriends.setAttribute("style", "width:600px")
      gradfriends.setAttribute('style', "height:600px")
      }


//function is not needed it is global

//const gradOne = document.querySelector(gradfriends)
//  gradOne.addEventListener("mouseOver", (e));
//  gradOne.addEventListener("mouseOut", (e));

//function mouseOver () {
  //gradfriends.style.height = "600px"
//  gradfriends.style.width = "600px"
