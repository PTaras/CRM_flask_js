function getLogo() {
            var getDomain = document.getElementById("domain").value;
            var show = document.getElementById("imgLogo");
            imgurl = 'https://logo.clearbit.com/' + getDomain.trim();
            const modalImg = document.getElementById('myImg');
            show.style.display = "block";
            modalImg.src = imgurl;
            modalImg.alt = getDomain.trim();
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