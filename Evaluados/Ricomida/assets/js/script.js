$(function(){

    $("a").click(function(event){
      if (this.hash !== "") {
        event.preventDefault();
  
        var actualiza = this.hash;
  
        $("html, body").animate({
          scrollTop: $(actualiza).offset().top
        }, 800, function(){
          window.location.hash = actualiza;
        });
      }
    });
  
    $(function () {
      $('[data-toggle="tooltip"]').tooltip()
    })
  
  });