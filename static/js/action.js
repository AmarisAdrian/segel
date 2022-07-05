// Cargar la imagen seleccionada
$(function () {
    $("#imagen").change(function () {
        if (this.files) {
            var reader = new FileReader();
            reader.onload = function (e) {
              $('#imagenShow').attr('src', e.target.result);
            }
            reader.readAsDataURL(this.files[0]);
          }
    });
  });
// Cargar la tabla de notificaciones no leidas de sufragante
  $(function(){ 
    $('.btnvotante').click(function(){ 
      var id = $(this).data('id'); 
      $('.table-votante').load('./?action=notificacion&id='+id,function(){ 
        $('#notificacion').html({show:true}); 
      }); 
    }); 
  });
  // Cargar la tabla de notificaciones no leidas de usuario
  $(function(){ 
    $('.btnusuario').click(function(){ 
      var id = $(this).data('id'); 
      $('.table-usuario').load('./?action=notificacion&id='+id,function(){ 
        $('#notificacion').html({show:true}); 
      }); 
    }); 
  });
   // Cargar la tabla de notificaciones no leidas de registros de puesto de votaion
   $(function(){ 
    $('.btnregistro').click(function(){ 
      var id = $(this).data('id'); 
      $('.table-registro').load('./?action=notificacion&id='+id,function(){ 
        $('#notificacion').html({show:true}); 
      }); 
    }); 
  });
// Cargar la tabla de notificaciones leidas de sufragante
$(function(){ 
  $('.btnhvotante').click(function(){ 
    var id = $(this).data('id'); 
    $('.table-hvotante').load('./?action=notificacion&id='+id,function(){ 
      $('#notificacion').html({show:true}); 
      $('#tablahistorialvotantel').DataTable();
    }); 
  }); 
});
// Cargar la tabla de notificaciones leidas de usuario
$(function(){ 
  $('.btnhusuario').click(function(){ 
    var id = $(this).data('id'); 
    $('.table-husuario').load('./?action=notificacion&id='+id,function(){ 
      $('#tablahistorialusuariol').DataTable();
      $('#notificacion').html({show:true}); 
      
    }); 
  }); 
});
 // Cargar la tabla de notificaciones leidas de registros de puesto de votaion
 $(function(){ 
  $('.btnhregistro').click(function(){ 
    var id = $(this).data('id'); 
    $('.table-hregistro').load('./?action=notificacion&id='+id,function(){ 
      $('#notificacion').html({show:true}); 
      $('#tablahistorialregistrol').DataTable();
    }); 
  }); 
});

  $(document).on('hidden.bs.modal','#modalhistorialvotante', function () {
        $.ajax({
           success: function () {
            location.reload();  
          },
          error: function (e) {
            alert("Problemas al tratar de enviar el formulario");
          }
        }); 
  });

  $(document).on('hidden.bs.modal','#modalhistorialregistro', function () {
        $.ajax({
           success: function () {
            location.reload();  
          },
          error: function (e) {
            alert("Problemas al tratar de enviar el formulario");
          }
        }); 
  });

  $(document).on('hidden.bs.modal','#modalmensaje', function () {
    $.ajax({
       success: function () {
        location.reload();  
      },
      error: function (e) {
        alert("Problemas al tratar de enviar el formulario");
      }
    }); 
});

      
