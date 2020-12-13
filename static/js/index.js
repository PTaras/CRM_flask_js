function getLogo() {
   var getDomain = document.getElementById("domain").value;
   var show = document.getElementById("imgLogo");
   var delTrim = getDomain.trim();
   if (delTrim.match(/http.*/) === null) {
       const imgurl = 'https://logo.clearbit.com/' + delTrim;
       const modalImg = document.getElementById('myImg');
       show.style.display = "block";
       modalImg.src = imgurl;
       modalImg.alt = delTrim;
   } else {
       const url = new URL(delTrim);
       const imglURL = url.hostname;
       const imgurl = 'https://logo.clearbit.com/' + imglURL;
       const modalImg = document.getElementById('myImg');
       console.log(imglURL, imgurl)
       show.style.display = "block";
       modalImg.src = imgurl;
       modalImg.alt = imglURL;
   }
  };

 function showLogo() {
    var getDomain = document.getElementById("domain").value;
    var show = document.getElementById("imgLogo");
    show.style.display = "none";
    getDomain.value = "";
  };

  function deleteLogo() {
    var getDomain = document.getElementById("domain").value;
    var show = document.getElementById("imgLogo");
    show.style.display = "none";
    getDomain.value = "";
  };

  function sort_domain() {
    req = $.ajax({
        url: '/sorted_domain',
        success: function(response) {
         $("#main-container").html( response);
        }
    });
  };

  function sort_id() {
    req = $.ajax({
        url: '/sorted_id',
        success: function(response) {
         $("#main-container").html( response);
        }
    });
  };

   function sort_logos() {
    req = $.ajax({
        url: '/sorted_logos',
        success: function(response) {
         $("#main-container").html( response);
        }
    });
  };

   function sort_date() {
    req = $.ajax({
        url: '/sorted_date',
        success: function(response) {
         $("#main-container").html( response);
        }
    });
  };