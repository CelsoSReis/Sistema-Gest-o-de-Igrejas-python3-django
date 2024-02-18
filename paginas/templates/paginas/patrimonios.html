<?php 
require_once("../conexao.php");
require_once("verificar.php");
$pagina = 'patrimonios';
?>


<div class="tabela bg-light my-3">
	<?php 

	$query = $pdo->query("SELECT * FROM $pagina order by id desc");
	$res = $query->fetchAll(PDO::FETCH_ASSOC);
	$total_reg = count($res);
	if($total_reg > 0){

		?>

		<table id="example" class="table table-striped table-light table-hover my-4 my-4" style="width:100%">
			<thead>			
				<tr>
					<th>Código</th>
					<th>Nome</th>
					<th class="esc">Cadastrado Por</th>
					<th class="esc">Data Cadastro</th>
					<th class="esc">Pertence a</th>
					<th class="esc">Foto</th>
					<th class="d-none">Ativo</th>					
					<th>Ações</th>
				</tr>		
			</thead>
			<tbody>
				<?php 
				for($i=0; $i < $total_reg; $i++){
					foreach ($res[$i] as $key => $value){} 

						$nome = $res[$i]['nome'];
					$codigo = $res[$i]['codigo'];
					$descricao = $res[$i]['descricao'];
					$valor = $res[$i]['valor'];
					$usuario_cad = $res[$i]['usuario_cad'];
					$foto = $res[$i]['foto'];
					$igreja_cad = $res[$i]['igreja_cad'];
					$data_cad = $res[$i]['data_cad'];
					$obs = $res[$i]['obs'];
					$igreja_item = $res[$i]['igreja_item'];
					$usuario_emprestou = $res[$i]['usuario_emprestou'];
					$data_emprestimo = $res[$i]['data_emprestimo'];
					$ativo = $res[$i]['ativo'];
					$entrada = $res[$i]['entrada'];
					$doador = $res[$i]['doador'];
					$id = $res[$i]['id'];


					
					if($obs != ""){
						$classe_obs = 'text-warning';
					}else{
						$classe_obs = 'text-secondary';
					}


					if($ativo == 'Sim'){
						$classe = 'text-success';
						$ativo = 'Desativar Item';
						$icone = 'bi-check-square';
						$ativar = 'Não';
						$inativa = '';
						$tab = 'Ativo';

					}else{
						$classe = 'text-danger';
						$ativo = 'Ativar Item';
						$icone = 'bi-square';
						$ativar = 'Sim';
						$inativa = 'text-muted';
						$tab = 'Inativo';
					}

					$query_con = $pdo->query("SELECT * FROM usuarios where id = '$usuario_cad'");
					$res_con = $query_con->fetchAll(PDO::FETCH_ASSOC);
					if(count($res_con) > 0){
						$nome_usu_cad = $res_con[0]['nome'];
					}else{
						$nome_usu_cad = '';
					}


					$query_con = $pdo->query("SELECT * FROM usuarios where id = '$usuario_emprestou'");
					$res_con = $query_con->fetchAll(PDO::FETCH_ASSOC);
					if(count($res_con) > 0){
						$nome_usu_emp = $res_con[0]['nome'];
					}else{
						$nome_usu_emp = 'Sem Empréstimo';
					}


					$query_con = $pdo->query("SELECT * FROM igrejas where id = '$igreja_cad'");
					$res_con = $query_con->fetchAll(PDO::FETCH_ASSOC);
					if(count($res_con) > 0){
						$nome_ig_cad = $res_con[0]['nome'];
					}else{
						$nome_ig_cad = '';
					}


					$query_con = $pdo->query("SELECT * FROM igrejas where id = '$igreja_item'");
					$res_con = $query_con->fetchAll(PDO::FETCH_ASSOC);
					if(count($res_con) > 0){
						$nome_ig_item = $res_con[0]['nome'];
					}else{
						$nome_ig_item = '';
					}


					


					//retirar quebra de texto do obs
					$obs = str_replace(array("\n", "\r"), ' + ', $obs);

					$data_cadF = implode('/', array_reverse(explode('-', $data_cad)));
					$data_emprestimoF = implode('/', array_reverse(explode('-', $data_emprestimo)));
					$valorF = number_format($valor, 2, ',', '.');
					?>			
					<tr class="<?php echo $inativa ?> ">
						<td><?php echo $codigo ?></td>
						<td><?php echo $nome ?></td>
						<td class="esc"><?php echo $nome_usu_cad ?></td>
						<td class="esc"><?php echo $data_cadF ?></td>
						<td class="esc"><?php echo $nome_ig_cad ?></td>
						
						<td class="esc"><img src="../img/patrimonios/<?php echo $foto ?>" width="30px"></td>

						<td class="d-none"><?php echo $tab ?></td>
						
						<td>
							<big>
							<a href="#" onclick="editar('<?php echo $id ?>', '<?php echo $codigo ?>', '<?php echo $nome ?>', '<?php echo $descricao ?>', '<?php echo $valor ?>', '<?php echo $foto ?>', '<?php echo $data_cad ?>', '<?php echo $entrada ?>', '<?php echo $doador ?>')" title="Editar Registro">	<i class="bi bi-pencil-square text-primary"></i> </a>

							<a href="#" onclick="excluir('<?php echo $id ?>' , '<?php echo $nome ?>')" title="Excluir Registro">	<i class="bi bi-trash text-danger"></i> </a>

							<a href="#" onclick="dados('<?php echo $codigo ?>', '<?php echo $nome ?>', '<?php echo $descricao ?>', '<?php echo $valor ?>', '<?php echo $foto ?>', '<?php echo $nome_usu_cad ?>', '<?php echo $data_cadF ?>', '<?php echo $nome_ig_cad ?>', '<?php echo $nome_ig_item ?>', '<?php echo $nome_usu_emp ?>', '<?php echo $data_emprestimoF ?>', '<?php echo $tab ?>', '<?php echo $obs ?>', '<?php echo $entrada ?>', '<?php echo $doador ?>')" title="Ver Dados">	<i class="bi bi-info-square-fill text-primary"></i> </a>

							<a href="#" onclick="obs('<?php echo $id ?>','<?php echo $nome ?>', '<?php echo $obs ?>')" title="Observações">	<i class="bi bi-chat-right-text <?php echo $classe_obs ?>"></i> </a>


							<a href="#" onclick="mudarStatus('<?php echo $id ?>', '<?php echo $ativar ?>')" title="<?php echo $ativo ?>">
								<i class="bi <?php echo $icone ?> <?php echo $classe ?>"></i></a>


								
							</big>

							</td>
						</tr>	
					<?php } ?>	
				</tbody>
			</table>
		<?php }else{
			echo 'Não Existem Dados Cadastrados';
		} ?>
	</div>


	<div class="modal fade" id="modalForm" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
		<div class="modal-dialog modal-lg">
			<div class="modal-content">
				<div class="modal-header">
					<h5 class="modal-title" id="tituloModal"></h5>
					<button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
				</div>
				<form id="form" method="post">
					<div class="modal-body">
						<div class="row">
							<div class="col-md-3">
								<div class="mb-3">
									<label for="exampleFormControlInput1" class="form-label">Código</label>
									<input type="text" class="form-control" id="codigo" name="codigo" placeholder="Código do item"  required>
								</div>
							</div>
							<div class="col-md-6">
								<div class="mb-3">
									<label for="exampleFormControlInput1" class="form-label">Nome</label>
									<input type="text" class="form-control" id="nome" name="nome" placeholder="Insira o Nome"  required>
								</div>
							</div>

							<div class="col-md-3">
								<div class="mb-3">
									<label for="exampleFormControlInput1" class="form-label">Data Cadastro</label>
									<input type="date" class="form-control" id="data_cad" name="data_cad" value="<?php echo date('Y-m-d') ?>" required>
								</div>
							</div>


						</div>

						<div class="mb-3">
									<label for="exampleFormControlInput1" class="form-label">Descrição Item</label>
									<input type="text" class="form-control" id="descricao" name="descricao" placeholder="Descrição do Item">
								</div>

						<div class="row">

							<div class="col-md-4">
								<div class="mb-3">
									<label for="exampleFormControlInput1" class="form-label">Entrada (Compra / Doação)</label>
									<select class="form-select" aria-label="Default select example" name="entrada" id="entrada">  
										<option value="Compra">Compra</option>
										<option value="Doação">Doação</option>

									</select>
								</div>
							</div>

							<div class="col-md-4">
								<div class="mb-3">
									<label for="exampleFormControlInput1" class="form-label">Valor</label>
									<input type="text" class="form-control" id="valor" name="valor" placeholder="Valor em caso de compra">
								</div>
							</div>

							<div class="col-md-4">
								<div class="mb-3">
									<label for="exampleFormControlInput1" class="form-label">Doador Por</label>
									<input type="text" class="form-control" id="doador" name="doador" placeholder="Nome do Doador">
								</div>
							</div>



						</div>

						<div class="row">

							<div class="col-md-5">
								<div class="mb-3">
									<label for="exampleFormControlInput1" class="form-label">Foto</label>
									<input type="file" class="form-control-file" id="imagem" name="imagem" onChange="carregarImg();">
								</div>
							</div>
							<div class="col-md-2">
								<div id="divImg" class="mt-4">
									<img src="../img/patrimonios/sem-foto.jpg"  width="100px" id="target">									
								</div>
							</div>

							

							</div>





							<input type="hidden" id="id" name="id">
							<input type="hidden" id="igreja2" name="igreja" value="<?php echo $id_igreja ?>">

						</div>
						<small><div align="center" id="mensagem"></div></small>
						<div class="modal-footer">
							<button type="button" class="btn btn-secondary" data-bs-dismiss="modal" id="btn-fechar">Fechar</button>
							<button type="submit" class="btn btn-primary">Salvar</button>
						</div>
					</form>
				</div>
			</div>
		</div>





		<!-- Modal -->
		<div class="modal fade" id="modalExcluir" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
			<div class="modal-dialog">
				<div class="modal-content">
					<div class="modal-header">
						<h5 class="modal-title" id="exampleModalLabel"><span id="tituloModal">Excluir Registro</span></h5>
						<button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
					</div>
					<form id="form-excluir" method="post">
						<div class="modal-body">

							Deseja Realmente excluir este Registro: <span id="nome-excluido"></span>?

							<small><div id="mensagem-excluir" align="center"></div></small>

							<input type="hidden" class="form-control" name="id-excluir"  id="id-excluir">


						</div>
						<div class="modal-footer">
							<button type="button" class="btn btn-secondary" data-bs-dismiss="modal" id="btn-fechar-excluir">Fechar</button>
							<button type="submit" class="btn btn-danger">Excluir</button>
						</div>
					</form>
				</div>
			</div>
		</div>



	<div class="modal fade" id="modalDados" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
		<div class="modal-dialog modal-lg">
			<div class="modal-content">
				<div class="modal-header">
					<h5 class="modal-title" id="exampleModalLabel">Nome : <span id="nome-dados"></span></h5>
					<button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
				</div>

				<div class="modal-body">
					<small>
					<div class="row">
						<div class="col-md-6">
							<span class=""><b>Código:</b> <span id="codigo-dados"></span></span>
							
						</div>

						<div class="col-md-6">
							<span class=""><b>Descrição:</b> <span id="descricao-dados"></span></span>
							
						</div>
					</div>
					<hr style="margin:4px">

					<div class="row">
						<div class="col-md-6">
							<span class=""><b>Valor:</b> R$ <span id="valor-dados"></span></span>
							
						</div>

						<div class="col-md-6">

							<span class=""><b>Cadastrado Por:</b> <span id="usuario-cad-dados"></span></span>
							
						</div>
					</div>
					<hr style="margin:4px">


					<div class="row">
						<div class="col-md-6">
							<span class=""><b>Data de Cadastro:</b> <span id="data-cad-dados"></span></span>
						</div>

						<div class="col-md-6">

							<span class=""><b>Igreja Dona Item:</b> <span id="igreja-cad-dados"></span></span>
						</div>
					</div>
					<hr style="margin:4px">


					<div class="row">
						<div class="col-md-6">
							<span class=""><b>Igreja Possui Item:</b> <span id="igreja-item-dados"></span></span>
						</div>

						<div class="col-md-6">

							<span class=""><b>Emprestado Por:</b> <span id="usu-emp-dados"></span></span>
						</div>
					</div>
					<hr style="margin:4px">


					<div class="row">
						<div class="col-md-6">
							<span class=""><b>Data Empréstimo:</b> <span id="data-emp-dados"></span></span>
						</div>

						<div class="col-md-6">

							<span class=""><b>Status do Item:</b> <span id="ativo-dados"></span></span>
						</div>
					</div>
					<hr style="margin:4px">


					<div class="row">
						<div class="col-md-6">
							<span class=""><b>Compra / Doação:</b> <span id="entrada-dados"></span></span>
						</div>

						<div class="col-md-6">

							<span class=""><b>Doador Por:</b> <span id="doador-dados"></span></span>
						</div>
					</div>
					<hr style="margin:4px">


					<div class="row">
						<div class="col-md-6">
							<span class=""><b>OBS:</b> <span id="obs-dados"></span></span>
						</div>

						<div class="col-md-6">

							<span class=""><img src="" id="foto-dados" width="170px"></span>
						</div>
					</div>
					<hr style="margin:4px">

				</small>
				</div>

			</form>
		</div>
	</div>
</div>







	<!-- Modal -->
	<div class="modal fade" id="modalObs" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
		<div class="modal-dialog modal-lg">
			<div class="modal-content">
				<div class="modal-header">
					<h5 class="modal-title" id="exampleModalLabel"><span id="tituloModal">Observações - <span id="nome-obs"></span></span></h5>
					<button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
				</div>
				<form id="form-obs" method="post">
					<div class="modal-body">

						<div class="mb-3">
							<label for="exampleFormControlInput1" class="form-label">Observações (Máximo 1000 Caracteres)</label>
							<textarea class="form-control" id="obs" name="obs" maxlength="500" style="height:200px"></textarea>
						</div>



						<small><div id="mensagem-obs" align="center"></div></small>

						<input type="hidden" class="form-control" name="id-obs"  id="id-obs">


					</div>
					<div class="modal-footer">
						<button type="button" class="btn btn-secondary" data-bs-dismiss="modal" id="btn-fechar-obs">Fechar</button>
						<button type="submit" class="btn btn-primary">Salvar</button>
					</div>
				</form>
			</div>
		</div>
	</div>





	<!-- Modal -->
	<div class="modal fade" id="modalTransferir" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
		<div class="modal-dialog">
			<div class="modal-content">
				<div class="modal-header">
					<h5 class="modal-title" id="exampleModalLabel"><span id="tituloModal">Trasferir - <span id="nome-transferir"></span></span></h5>
					<button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
				</div>
				<form id="form-transferir" method="post">
					<div class="modal-body">
					
						<div class="mb-3">
								<label for="exampleFormControlInput1" class="form-label">Igreja</label>
								<select class="form-control sel2" id="igreja" name="igreja" style="width:100%;" required>
									<?php 
									$query = $pdo->query("SELECT * FROM igrejas order by matriz desc, nome asc");
									$res = $query->fetchAll(PDO::FETCH_ASSOC);
									$total_reg = count($res);
									if($total_reg > 0){

										for($i=0; $i < $total_reg; $i++){
											foreach ($res[$i] as $key => $value){} 

												$nome_reg = $res[$i]['nome'];
												$id_reg = $res[$i]['id'];

												if($id_reg != $id_igreja){
											?>
											<option value="<?php echo $id_reg ?>" class="<?php echo $classe_ig ?>"><?php echo $nome_reg ?></option>

										<?php }}} ?>
									</select>
								</div>


						<small><div id="mensagem-transferir" align="center"></div></small>

						<input type="hidden" class="form-control" name="id-transferir"  id="id-transferir">


					</div>
					<div class="modal-footer">
						<button type="button" class="btn btn-secondary" data-bs-dismiss="modal" id="btn-fechar-trasferir">Fechar</button>
						<button type="submit" class="btn btn-success">Transferir</button>
					</div>
				</form>
			</div>
		</div>
	</div>





		<!-- Modal -->
		<div class="modal fade" id="modalDevolver" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
			<div class="modal-dialog">
				<div class="modal-content">
					<div class="modal-header">
						<h5 class="modal-title" id="exampleModalLabel"><span id="tituloModal">Devolver Item</span> - <span id="nome-item"></span></h5>
						<button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
					</div>
					<form id="form-devolver" method="post">
						<div class="modal-body">

							Deseja Realmente devolver este Item: <span id="nome-devolver"></span>?

							<small><div id="mensagem-devolver" align="center"></div></small>

							<input type="hidden" class="form-control" name="id-transferir"  id="id-devolver">
							<input type="hidden" class="form-control" name="igreja" id="id-ig" >


						</div>
						<div class="modal-footer">
							<button type="button" class="btn btn-secondary" data-bs-dismiss="modal" id="btn-fechar-devolver">Fechar</button>
							<button type="submit" class="btn btn-success">Devolver</button>
						</div>
					</form>
				</div>
			</div>
		</div>




	<script type="text/javascript">var pag = "<?=$pagina?>"</script>
	<script src="../js/ajax.js"></script>


	<script type="text/javascript">

		function editar(id, codigo, nome, descricao, valor, foto, data_cad, entrada, doador){
			$('#id').val(id);
			$('#nome').val(nome);
			$('#codigo').val(codigo);
			$('#descricao').val(descricao);
			$('#valor').val(valor);
			$('#data_cad').val(data_cad);
			$('#doador').val(doador);
			$('#entrada').val(entrada).change();
			$('#target').attr('src', '../img/patrimonios/' + foto);

			$('#tituloModal').text('Editar Registro');
			var myModal = new bootstrap.Modal(document.getElementById('modalForm'), {		});
			myModal.show();
			$('#mensagem').text('');
		}



		function dados(codigo, nome, descricao, valor, foto, usuario_cad, data_cad, igreja_cad, igreja_item, usuario_emp, data_emp, ativo, obs, entrada, doador){

			if(data_emp === '00/00/0000'){
				data_emp = 'Sem Empréstimo';
			}

			$('#nome-dados').text(nome);
			$('#descricao-dados').text(descricao);
			$('#codigo-dados').text(codigo);
			$('#valor-dados').text(valor);
			$('#usuario-cad-dados').text(usuario_cad);
			$('#data-cad-dados').text(data_cad);
			$('#igreja-cad-dados').text(igreja_cad);
			$('#igreja-item-dados').text(igreja_item);
			$('#usu-emp-dados').text(usuario_emp);
			$('#data-emp-dados').text(data_emp);
			$('#ativo-dados').text(ativo);
			$('#obs-dados').text(obs);
			$('#entrada-dados').text(entrada);
			$('#doador-dados').text(doador);
			$('#foto-dados').attr('src', '../img/patrimonios/' + foto);


			var myModal = new bootstrap.Modal(document.getElementById('modalDados'), {		});
			myModal.show();
			$('#mensagem').text('');
		}



		function obs(id, nome, obs){
			console.log(obs)

			for (let letra of obs){  				
				if (letra === '+'){
					obs = obs.replace(' +  + ', '\n')
				}			
			}


			$('#nome-obs').text(nome);
			$('#id-obs').val(id);
			$('#obs').val(obs);



			var myModal = new bootstrap.Modal(document.getElementById('modalObs'), {		});
			myModal.show();
			$('#mensagem-obs').text('');
		}

		


function transferir(id, nome){
    $('#id-transferir').val(id);
    $('#nome-transferir').text(nome);
    var myModal = new bootstrap.Modal(document.getElementById('modalTransferir'), {       });
    myModal.show();
    $('#mensagem-transferir').text('');
    limpar();
}




$("#form-transferir").submit(function () {

	event.preventDefault();
	var formData = new FormData(this);

	$.ajax({
		url: pag + "/transferir.php",
		type: 'POST',
		data: formData,

		success: function (mensagem) {
			$('#mensagem-transferir').text('');
			$('#mensagem-transferir').removeClass()
			if (mensagem.trim() == "Alterado com Sucesso") {
                    //$('#nome').val('');
                    //$('#cpf').val('');
                     $('#btn-fechar-trasferir').click();
                     mensagemSalvar();
                     
                     setTimeout(function(){
                        window.location="index.php?pag=" + pag;
                    }, 500)
                     
                    
                     
                } else {

                	$('#mensagem-transferir').addClass('text-danger')
                	$('#mensagem-transferir').text(mensagem)
                }


            },

            cache: false,
            contentType: false,
            processData: false,
            
        });

});




function devolver(id, nome, igreja){
    $('#id-devolver').val(id);
    $('#id-ig').val(igreja);
    $('#nome-devolver').text(nome);
    $('#nome-item').text(nome);
    var myModal = new bootstrap.Modal(document.getElementById('modalDevolver'), {       });
    myModal.show();
    $('#mensagem-devolver').text('');
    limpar();
}



$("#form-devolver").submit(function () {

	event.preventDefault();
	var formData = new FormData(this);

	$.ajax({
		url: pag + "/transferir.php",
		type: 'POST',
		data: formData,

		success: function (mensagem) {
			$('#mensagem-transferir').text('');
			$('#mensagem-transferir').removeClass()
			if (mensagem.trim() == "Alterado com Sucesso") {
                    //$('#nome').val('');
                    //$('#cpf').val('');
                     $('#btn-fechar-trasferir').click();
                     mensagemSalvar();
                     
                     setTimeout(function(){
                        window.location="index.php?pag=" + pag;
                    }, 500)
                     
                    
                     
                } else {

                	$('#mensagem-transferir').addClass('text-danger')
                	$('#mensagem-transferir').text(mensagem)
                }


            },

            cache: false,
            contentType: false,
            processData: false,
            
        });

});



	</script>



	<link href="https://cdn.jsdelivr.net/npm/select2@4.1.0-rc.0/dist/css/select2.min.css" rel="stylesheet" />
	<script src="https://cdn.jsdelivr.net/npm/select2@4.1.0-rc.0/dist/js/select2.min.js"></script>

	<script>
		$(document).ready(function() {
			$('.sel2').select2({
			//placeholder: 'Selecione um Cliente',
			dropdownParent: $('#modalTransferir')
		});
		});


	</script>

	<style type="text/css">
		.select2-selection__rendered {
			line-height: 36px !important;
			font-size:16px !important;
			color:#666666 !important;

		}

		.select2-selection {
			height: 36px !important;
			font-size:16px !important;
			color:#666666 !important;

		}
	</style>  