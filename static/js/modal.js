//Abrir modal Departamento
$(function(){
	$('.openmodaldepartamento').click(function(){
    var id = $(this).data('id');
    $('.modal-body').load('./?action=modaldepartamento&id='+id,function(){
    $('#modaldepartamento').modal({show:true}); 
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
//abrir modal votante 
$(function(){ 
  $('.openmodalvotante').click(function(){ 
    var id = $(this).data('id'); 
    $('.modal-body').load('./?action=modalvotante&id='+id,function(){ 
      $('#modalvotante').modal({show:true}); 
    }); 
  }); 
});
//abrir modal divipol
$(function(){ 
  $('.openmodaldivipol').click(function(){ 
    var id = $(this).data('id'); 
    $('.modal-body').load('./?action=modaldivipol&id='+id,function(){ 
      $('#modaldivipol').modal({show:true}); 
    }); 
  }); 
});
//abrir modal zona
$(function(){ 
  $('.openmodalzona').click(function(){ 
    var id = $(this).data('id'); 
    $('.modal-body').load('./?action=modalzona&id='+id,function(){ 
      $('#modalzona').modal({show:true}); 
    }); 
  }); 
});
//abrir modal puesto votacion
$(function(){ 
  $('.openmodalpuestovotacion').click(function(){ 
    var id = $(this).data('id'); 
    var nombre =$(this).data('nombre');
    $('.modal-body').load('./?action=modalpuestovotacion&id='+id+'&nombre='+nombre,function(){ 
      $('#modalpuestovotacion').modal({show:true}); 
    }); 
  }); 
});
// abrir modal de anexos votante registrados
$(function(){ 
  $('#buttonbuscaranexovotante').click(function(){ 
    var id = $('#noDocumentovotante').val();
    if(id!=""){
    $('#tablaanexovotante').load('./?action=modalanexovotante&id='+id,function(){ 
        $('#modalanexovotante').html({show:true});
        $('#noDocumento').val('');
    }); 
  }else{
      $('#noDocumentovotante').focus();
  }}); 
});
// abrir modal de anexos de usuario registrados
$(function(){ 
  $('#buttonbuscaranexousuario').click(function(){ 
    var id = $('#noDocumentoUsuario').val();
    if(id!=""){
    $('#tablaanexousuario').load('./?action=modalanexousuario&id='+id,function(){ 
        $('#modalanexousuario').html({show:true});
        $('#noDocumentoUsuario').val('');
      }); 
    }else{
      $('#noDocumentovotante').focus();
    }}); 
  });

//abrir modal asignar puesto votacion
$(function(){ 
  $('.openmodalasignarpuesto').click(function(){ 
    var id = $(this).data('id'); 
    $('.modal-body').load('./?action=modalasignarpuesto&id='+id,function(){ 
      $('#modalasignarpuesto').modal({show:true}); 
    }); 
  }); 
});
//abrir modal editar puesto votacion asignado
$(function(){ 
  $('.openmodalinscripcion').click(function(){ 
    var id = $(this).data('id'); 
    $('.modal-body').load('./?action=modaleditarpuesto&id='+id,function(){ 
      $('#modaleditarpuesto').modal({show:true}); 
    }); 
  }); 
});
$(function(){ 
  $('.openmodalmensaje').click(function(){ 
    var id = $(this).data('id'); 
    $('.modal-body').load('./?action=modalmensaje&id='+id,function(){ 
      $('#modalmensaje').modal({show:true}); 
    }); 
  }); 
});
$(function(){ 
  $(document).on('click','.openmodalhistorialvotante',function(){ 
    var id = $(this).data('id'); 
    $('.modal-body').load('./?action=modalhistorialvotante&id='+id,function(){ 
      $('.modal-body #modalhistorialvotante').modal({show:true});
    }); 
  }); 
});
$(function(){ 
  $(document).on('click','.openmodalhistorialregistro',function(){ 
    var id = $(this).data('id'); 
    $('.modal-body').load('./?action=modalhistorialregistro&id='+id,function(){ 
      $('.modal-body #modalhistorialregistro').modal({show:true});
    }); 
  }); 
});
$(function(){ 
  $(document).on('click','.openmodalhistorialusuario',function(){ 
    var id = $(this).data('id'); 
    $('.modal-body').load('./?action=modalhistorialusuario&id='+id,function(){ 
      $('.modal-body #modalhistorialusuario').modal({show:true});
    }); 
  }); 
});
$(function () {
  $(document).on('click', '.openmodal_lista', function () {
    var id = $(this).data('id');
    $('.modal-body').load('./?action=modal_lista&id=' + id, function () {
      $('.modal-body #modal_lista').modal({ show: true });
    });
  });
});

$(function(){ 
  $(document).on('click','.celda_anexo_votante',function(){ 
    var id = $(this).data('id'); 
    $('.modal-body').load('./?action=modalimagenanexo&id='+id,function(){ 
      $('.modal-body #modalimagenanexo').modal({show:true});
    }); 
  }); 
});

$(function(){ 
  $(document).on('click','.celda_anexo_usuario',function(){ 
    var id = $(this).data('id'); 
    $('.modal-body').load('./?action=modalimagenanexousuario&id='+id,function(){ 
      $('.modal-body #modalimagenanexousuario').modal({show:true});
    }); 
  }); 
});

$(function(){ 
  $('#btnBuscarVotante').click(function(){  
    var id = $('#noDocumentoVotante').val(); 
    if(id!=""){
    $('#InformacionVotante').load('./?action=modalbuscarvotante&id='+id,function(){ 
        $('#modalbuscarvotante').html({show:true});
        $('.collapse').collapse();
        $('#noDocumentoVotante').val('');
    }); 
  }else{
    $('#noDocumentoVotante').prop('requerid',true); 
  }});

});$(function(){ 
  $('#btnBuscarVotante').click(function(){  
    var id = $('#noDocumentoVotante').val(); 
    $('#InformacionPuestoVotante').load('./?action=modalbuscarpuesto&id='+id,function(){ 
        $('#modalvotante').html({show:true});
        $('.collapsep').collapse();
    }); 
  });
});
