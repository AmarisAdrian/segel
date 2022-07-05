//abrir combo ciudad divipol
$(function(){ 
    $('#iddepartamentodivipol').change(function(){ 
      var id = $(this).val();
      $('#idciudadivipol').load('./?action=addcombociudad&id='+id,function(){ 
        $('#addcombociudad').html({show:true}); 
      }); 
    }); 
  });
  //abrir combo ciudad votante
  $(function(){ 
    $('#idDepartamentoVotante').change(function(){ 
      var id = $(this).val();
      $('#idCiudadVotante').load('./?action=addcombociudad&id='+id,function(){ 
        $('#addcombociudad').html({show:true}); 
      }); 
    }); 
  });
  //abrir combo ciudad puesto de votacion
  $(function(){ 
    $('#idDepartamentoPuesto').change(function(){ 
      var id = $(this).val();
      $('#idCiudadPuesto').load('./?action=addcombociudad&id='+id,function(){ 
        $('#addcombociudad').html({show:true}); 
      }); 
    });
  });
  //abrir combo zona puesto de votacion
  $(function(){ 
    $('#idCiudadPuesto').change(function(){ 
      var id = $(this).val();
      $('#idZonaPuesto').load('./?action=addcombozonasp&id='+id,function(){ 
        $('#addcombozonasp').html({show:true}); 
      }); 
    });
  });
  //abrir combo ciudad en zona de votacion
  $(function(){ 
    $('#idDepartamentoZona').change(function(){ 
      var id = $(this).val();
      $('#idCiudadZona').load('./?action=addcombociudad&id='+id,function(){ 
        $('#addcombociudad').html({show:true}); 
      }); 
    });
  });
  //abrir combo divipol de zona votacion
  $(function(){ 
    $('#idCiudadZona').change(function(){ 
      var id = $(this).val();
      $('#idDivipolZona').load('./?action=addcombodivipol&id='+id,function(){ 
        $('#addcombodivipol').html({show:true}); 
      }); 
    });
  });
  //abrir combo de modal de ciudad votante
  $(function(){ 
    $(document).on('change','#idModalDepartamento',function(){ 
      var id = $(this).val();
      $('.modal-body #idModalCiudad').load('./?action=addcombomodalciudad&id='+id,function(){ 
        $('.modal-body #addcombomodalciudad').html({show:true});
      }); 
    }); 
  });
  //abrir combo de ciudad del modal asignar puesto 
  $(function(){ 
    $(document).on('change','#idDivipolAsignar',function(){
      var id = $(this).val();    
      $('.modal-body #idZonaAsignar').load('./?action=addcombozona&id='+id,function(){ 
        $('.modal-body #addcombozona').html({show:true});   
      }); 
    }); 
   });
   //abrir combo de puesto de votación del modal asignar puesto
  $(function(){ 
    $(document).on('change','#idZonaAsignar',function(){
      var id = $(this).val();    
      $('.modal-body #idZonaPuesto').load('./?action=addcombopuesto&id='+id,function(){ 
        $('.modal-body #addcombopuesto').html({show:true});   
      }); 
    }); 
   });
   //abrir combo de ciudad del modal divipol
  $(function(){ 
    $(document).on('change','#idDepartamentoDivipol',function(){
      var id = $(this).val();    
      $('.modal-body #idCiudadDivipol').load('./?action=addcombociudad&id='+id,function(){ 
        $('.modal-body #addcombociudad').html({show:true});   
      }); 
    }); 
   });
  //abrir combo ciudad perfil
  $(function(){ 
    $('#idDepartamentoPerfil').change(function(){ 
      var id = $(this).val(); 
      $('#idCiudadPerfil').load('./?action=addcombociudad&id='+id,function(){ 
        $('#addcomboperfil').html({show:true}); 
      }); 
    }); 
  });
   //abrir combo ciudad en editar puesto de votacion en inscripciones
   $(function(){ 
    $(document).on('change','#idDepartamentoInscripcion',function(){
      var id = $(this).val(); 
      $('.modal-body #idCiudadInscripcion').load('./?action=addcombociudad&id='+id,function(){ 
        $('.modal-body #addcombociudad').html({show:true}); 
      }); 
    }); 
  });
    //abrir combo zona  en editar puesto de votacion en inscripciones
    $(function(){ 
      $(document).on('change','#idCiudadInscripcion',function(){
        var id = $(this).val(); 
        $('.modal-body #idZonainscripcion').load('./?action=addcombozonasp&id='+id,function(){ 
          $('.modal-body #addcombozonasp').html({show:true}); 
        }); 
      }); 
    });
      //abrir combo puesto en editar puesto de votacion en inscripciones
      $(function(){ 
        $(document).on('change','#idZonainscripcion',function(){
          var id = $(this).val(); 
          $('.modal-body #idPuesto').load('./?action=addcombopuesto&id='+id,function(){ 
            $('.modal-body #addcombopuesto').html({show:true}); 
          }); 
        }); 
      });
    //abrir combo zona en modal editar puesto
    $(function(){ 
      $('#idCiudadPuesto').change(function(){ 
        var id = $(this).val();
        $('#idZonaPuesto').load('./?action=addcombozonasp&id='+id,function(){ 
          $('#addcombozonasp').html({show:true}); 
        }); 
      });
    });
     //abrir combo ciudad modal zona
   $(function(){ 
    $(document).on('change','#idDepartamentoModalZona',function(){
      var id = $(this).val(); 
      $('.modal-body #idCiudadModalZona').load('./?action=addcombociudad&id='+id,function(){ 
        $('.modal-body #addcombociudad').html({show:true}); 
      }); 
    }); 
  });
     //abrir combo divipol del modal zona
    $(function(){ 
      $(document).on('change','#idCiudadModalZona',function(){
        var id = $(this).val(); 
        $('.modal-body #divipol').load('./?action=addcombodivipol&id='+id,function(){ 
          $('.modal-body #addcombodivipol').html({show:true}); 
        }); 
      }); 
    });

       //abrir combo ciudad del modal puesto de votacion
       $(function(){ 
        $(document).on('change','#idDepartamentoModalPuesto',function(){
          var id = $(this).val(); 
          $('.modal-body #idCiudadModalPuesto').load('./?action=addcombociudad&id='+id,function(){ 
            $('.modal-body #addcombociudad').html({show:true}); 
          }); 
        }); 
      });
       //abrir combo ciudad del modal puesto de votacion
       $(function(){ 
        $(document).on('change','#idCiudadModalPuesto',function(){
          var id = $(this).val(); 
          $('.modal-body #idZona').load('./?action=addcombozonasp&id='+id,function(){ 
            $('.modal-body #addcombozonasp').html({show:true}); 
          }); 
        }); 
      });

   //abrir combo ciudad del modal puesto de votacion
   $(function(){ 
    $(document).on('change','#idZonaPuesto',function(){
      var id = $(this).val(); 
      $('.modal-body #idMesa').load('./?action=addcombomesa&id='+id,function(){ 
        $('.modal-body #addcombomesa').html({show:true}); 
      }); 
    }); 
  });
  $(function(){ 
    $(document).on('change','#idPuesto',function(){
      var id = $(this).val(); 
      $('.modal-body #idMesa').load('./?action=addcombomesa&id='+id,function(){ 
        $('.modal-body #addcombomesa').html({show:true}); 
      }); 
    }); 
  });