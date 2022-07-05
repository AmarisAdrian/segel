$(document).ready(function (mensaje) {
  $('#tablahistorialvotante').DataTable(); 
   var tableciudad =  $('#tablaciudad').DataTable({
      extend: 'collection',
      processing: true,
      'processing': true,
      buttons: [       
         'csv',
         'excel', 
          {
            extend:'pdf',
            messageTop: mensaje
          },
          {
            extend:'print',
            messageTop: mensaje
          }
          
        ],
      });  
      tableciudad.buttons( 0, null ).containers().appendTo('#MenuHerramientaCiudad');

    var tabledepartamento = $('#tabladepartamento').DataTable({
      extend: 'collection',
      buttons: [       
         'csv',
         'excel', 
          {
            extend:'pdf',
            messageTop: mensaje
            
          },
          {
            extend:'print',
            messageTop: mensaje
          }
          
        ],
      });  
      tabledepartamento.buttons( 0, null ).containers().appendTo('#MenuHerramientaDepartamento');

    $('#tablamensajerecibido').DataTable();
    $('#tablamensajeenviado').DataTable();
     $('#tablatoplider').DataTable({
        "order": [[ 0, "desc" ]],
        "destroy": true,
        "paging": false,
        "lengthChange": false,
        "searching": false,
        "ordering": true,
        "info": true,
        "autoWidth": false
     });

    var tablezona = $('#tablazona').DataTable({
      extend: 'collection',
      buttons: [       
         'csv',
         'excel', 
          {
            extend:'pdf',
            messageTop: mensaje
            
          },
          {
            extend:'print',
            messageTop: mensaje
          }
          
        ],
    });
    tablezona.buttons( 0, null ).containers().appendTo( '#MenuHerramientaZona' );

    var tabledivipol = $('#tabladivipol').DataTable({
      extend: 'collection',
      buttons: [       
         'csv',
         'excel', 
          {
            extend:'pdf',
            messageTop: mensaje
            
          },
          {
            extend:'print',
            messageTop: mensaje
          }
          
        ],

      }); 
      tabledivipol.buttons( 0, null ).containers().appendTo( '#MenuHerramientaDivipol' );
      
    var tablepuestovotacion=$('#tablapuestovotacion').DataTable({
      extend: 'collection',
      buttons: [       
         'csv',
         'excel', 
          {
            extend:'pdf',
            messageTop: mensaje
            
          },
          {
            extend:'print',
            messageTop: mensaje
          }
          
        ],
      });  
    tablepuestovotacion.buttons( 0, null ).containers().appendTo('#MenuHerramientaPuestoVotacion');

    var tableinscripcion = $('#tablainscripcion').DataTable({
      extend: 'collection',
      buttons: [       
         'csv',
         'excel', 
          {
            extend:'pdf',
            messageTop: mensaje
            
          },
          {
            extend:'print',
            messageTop: mensaje
          }
          
        ],
      });  
      tableinscripcion.buttons( 0, null ).containers().appendTo( '#MenuHerramientaInscripcion' );

  var tablaestadisticas = $('#tablaestadisticas').DataTable({
    extend: 'collection',
    buttons: [
      'csv',
      'excel',
      {
        extend: 'pdf',
        messageTop: mensaje

      },
      {
        extend: 'print',
        messageTop: mensaje
      }

    ],
  });
  tablaestadisticas.buttons(0, null).containers().appendTo('#MenuHerramientaEstadisticas');
    // counter-up
    $('.counter').counterUp({
      delay: 10,
      time: 600
    });
    $('#TabMensaje a').on('click', function (e) {
      e.preventDefault()
      $(this).tab('show')
    });
  });

