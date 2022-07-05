<?php
if(isset($_SESSION)){
 $NoDocumento =  $_SESSION['noDocumento']; 
 $Usuario = UsuarioData::GetByDocumento($NoDocumento);  
?>
<section>
<div class="container-fluid">
<div class="row">
        <div class="col-xl-12 col-lg-12 col-md-12 col-sm-12">
            <div class="breadcrumb-holder">
                <h1 class="main-title float-left">Inscripciones de cedula</h1>
                <ol class="breadcrumb float-right">
                    <li class="breadcrumb-item"><a href="?view=home">Home</a></li>
                    <li class="breadcrumb-item active">Inscripciones registradas</li>
                </ol>
                <div class="clearfix"></div>
            </div>
        </div>
    </div>
<div class="row">
        <div class="col-xl-12 col-lg-12 col-md-12 col-sm-12">

                <div class="card">
                    <div class="card-header">
                        <h3>
                                <div class="dropdown">
                                    <i class="fa fa-list"></i> Lista de inscripciones registradas
                                    <button class="btn btn-info dropdown-toggle" type="button" id="MenuHerramienta"
                                        data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                                        Exportar
                                    </button>
                                    <div class="dropdown-menu" id="MenuHerramientaInscripcion" aria-labelledby="MenuHerramienta">

                                    </div>
                                </div>          
                        </h3>
                    </div> 
                    <?php 
                     if($Usuario->idTipoUsuario==1){
                         $Reg = SpData::GetAllVotanteInscrito();
                      }
                      if($Usuario->idTipoUsuario==2){
                         $Reg = SpData::GetAllVotanteInscrito();
                      }
                      if($Usuario->idTipoUsuario==3){
                        $Reg = SpData::GetAllVotanteInscritoByUsuario($Usuario->id);
                      }
                    if((count($Reg)>0)){
                    ?>
                    <div class="card-body">
                            <div class="table-responsive">
                                    <table id="tablainscripcion" class="table table-striped ">
                                        <thead class="bg-primary text-white">
                                            <tr>
                                                <th>id</th>
                                                <th>Identificacion</th>
                                                <th>Nombres</th>
                                                <th>Apellidos</th>
                                                <th>Puesto</th>
                                                <th>Mesa</th>
                                                <th>Comentario</th>
                                                <th></th>
                                            </tr>
                                        </thead>
                                        <tbody>
                                            <?php
                                                   foreach($Reg as $Reg){

                                                    ?>
                                            <tr>
                                                <td><?php echo $Reg->id; ?></td>
                                                <td><?php echo $Reg->noDocumento; ?></td>
                                                <td><?php echo $Reg->nombre ?></td>
                                                <td><?php echo $Reg->apellido; ?></td>
                                                <td><?php echo $Reg->puesto ?></td>
                                                <td><?php echo $Reg->mesa ?></td>
                                                <td><?php echo $Reg->comentario ?></td>
                                                <td style="width:100px;">
                                                    <a href="#" data-target="#modalinscripcion"
                                                        data-id="<?php echo $Reg->id; ?>" data-toggle="modal"
                                                        class="openmodalinscripcion btn btn-success btn-circle btn-sm" title="Ver"
                                                        data-placement="top"> <i class="fa fa-eye" aria-hidden="true"></i></a>
                                                    <a href="#"
                                                        data-id="<?php echo $Reg->id; ?>,<?php echo $Reg->nombre; ?>"
                                                        class="btndelinscripcion btn btn-danger btn-circle btn-sm" title="Borrar"
                                                        data-toggle="tooltip" data-placement="top" data-method="DELETE"
                                                        onclick="Alert('btndelinscripcion','inscripcion','./?action=delinscripcion&id=<?php echo $Reg->id; ?>');"><i
                                                            class="fa fa-trash"></i></a>
                                                </td>
                                            </tr>
                                            <?php
                                                        }					    
                                                    ?>
                                        </tbody>
                                    </table>
                                </div>
                    </div>  
                    <?php } else { ?>
                        <div class="alert alert-danger">
                            <span>
                                <b>No hay inscripciones realizadas</b>
                            </span>
                        </div>
                        <?php } ?>                
                </div>
        </div>
</div>    
</div>
<div id="modalinscripcion" class="modal" tabindex="-1" role="dialog">
    <div class="modal-dialog modal-lg" role="document">
        <div class="modal-content">
            <div class="modal-header bg-primary">
                <h5 class="modal-title text-light"><i class="fas fa-map-marker"></i> Inscripcion</h5>
                <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                    <span aria-hidden="true">&times;</span>
                </button>
            </div>
            <div class="modal-body">
            </div>
        </div>
    </div>
</div>
</section>
<?php }else{ ?>
    <div class="alert alert-danger">
                        <span>
                            <b>Error al enviar los datos</b>
                        </span>
                    </div>
<?php } ?> 
