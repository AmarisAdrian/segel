$(document).on('submit', '#FrmAddCiudad', function (e){
    let url = $("#FrmAddCiudad").data("url")
    let csrftoken = $("input[name=csrfmiddlewaretoken").val()
    let id_departamento =  $("#id_departamento").val()
    let id_nombre =  $("#id_nombre").val()
    var data = {'id_departamento': id_departamento,'id_nombre':id_nombre ,'csrfmiddlewaretoken': csrftoken }
    $.ajax({
        type: "POST",
        url: url,
        dataType: "json",
        data:  data,
        beforeSend: function () {
            Swal.fire({
                imageUrl: '/static/img/Loading.gif',
                imageWidth: 250,
                imageHeight: 200,
                imageAlt: 'Custom image',
                showConfirmButton: false,
                title: 'Cargando ...',
            });
        },
        complete: function (data) {
            if (data.responseJSON.status == "success" && data.responseJSON.code == 201) {
                Swal.fire({
                    title: data.responseJSON.status + ' ' + data.responseJSON.code,
                    text: data.responseJSON.msj,
                    icon: data.responseJSON.status,
                    timer: 4000,
                }).then(() => {
                   location.reload()
                });
            }else{
                Swal.fire({
                    title: data.responseJSON.status + ' ' + data.responseJSON.code,
                    text: data.responseJSON.msj,
                    icon: data.responseJSON.status,
                    timer: 4000,
                });
            }
        } ,fail: function (jqXHR, textStatus, errorThrown) {
            alert("\nError: " + jqXHR.status + ' \nMensaje ' + textStatus + ' \nestado ' + errorThrown);
        },
    });
    return false;
});