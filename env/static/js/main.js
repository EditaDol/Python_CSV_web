/* When the user clicks on the button,
toggle between hiding and showing the dropdown content */
function myFunction() {
    document.getElementById("myDropdown").classList.toggle("show");
  }

  
  // Close the dropdown menu if the user clicks outside of it
  window.onclick = function(event) {
    if (!event.target.matches('.dropbtn')) {
      var dropdowns = document.getElementsByClassName("dropdown-content");
      var i;
      for (i = 0; i < dropdowns.length; i++) {
        var openDropdown = dropdowns[i];
        if (openDropdown.classList.contains('show')) {
          openDropdown.classList.remove('show');
        }
      }
    }
  }
  // Sales total
$(function() {
    $('a#sales_total').bind('click', function() {
        $.getJSON ( $SCRIPT_ROOT +'sales', function (data) {
       $("#result").text(data.result)
      });
      return false;
    }); 
    });
 
// Average
$(function() {
  $('a#average').bind('click', function() {
      $.getJSON ( $SCRIPT_ROOT +'average', function (data) {
     $("#result").text(data.result)
    });
    return false;
  }); 
  });

  // Min sales month
$(function() {
  $('a#min').bind('click', function() {
      $.getJSON ( $SCRIPT_ROOT +'minimum', function (data) {
     $("#result").text(data.result)
    });
    return false;
  }); 
  });

  // Max sales month
$(function() {
  $('a#max').bind('click', function() {
      $.getJSON ( $SCRIPT_ROOT +'maximum', function (data) {
     $("#result").text(data.result)
    });
    return false;
  }); 
  });

  
    
