//Abrir modal Departamento
$(function(){
  $('.modal_departamento').click(function(){ 
    var url = $(this).data('url'); 
    $('.modal-body').load(url,function(){ 
      $('#modal_departamento').modal({show:true}); 
    }); 
  }); 
});


//abrir modal ciudad 
$(function(){ 
  $('.modal_ciudad').click(function(){ 
    var url = $(this).data('url'); 
    $('.modal-body').load(url,function(){ 
      $('#modal_ciudad').modal({show:true}); 
    }); 
  }); 
}); 
