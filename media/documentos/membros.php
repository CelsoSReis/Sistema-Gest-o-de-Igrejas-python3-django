<?php 
require_once("../conexao.php");
require_once("verificar.php");
$pagina = 'membros';
?>

<div class="col-md-12 my-3">
	<button
	onclick="inserir()"
	class="btn btn-primary btn-round ms-auto"	
	>
	<i class="fa fa-plus"> </i>
	Novo Membro
	</button>
</div>

<div class="tabela bg-light">
	<?php 

	$query = $pdo->query("SELECT * FROM $pagina where igreja = '$id_igreja' order by nome ASC");
	$res = $query->fetchAll(PDO::FETCH_ASSOC);
	$total_reg = count($res);
	if($total_reg > 0){

		?>

		<table id="example" class="table table-striped table-light table-hover my-4 my-4" style="width:100%">
			<thead>			
				<tr>
					<th>Nome</th>
					<th>CPF</th>
					<th class="esc">Email</th>
					<th class="esc">Telefone</th>
					<th class="esc">Cargo</th>
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
					$cpf = $res[$i]['cpf'];
					$email = $res[$i]['email'];
					$telefone = $res[$i]['telefone'];
					$endereco = $res[$i]['endereco'];
					$foto = $res[$i]['foto'];
					$data_nasc = $res[$i]['data_nasc'];
					$data_cad = $res[$i]['data_cad'];
					$obs = $res[$i]['obs'];
					$igreja = $res[$i]['igreja'];
					$cargo = $res[$i]['cargo'];
					$data_bat = $res[$i]['data_batismo'];
					$igreja = $res[$i]['igreja'];
					$ativo = $res[$i]['ativo'];
					$id = $res[$i]['id'];

					if($obs != ""){
						$classe_obs = 'text-warning';
					}else{
						$classe_obs = 'text-secondary';
					}


					if($ativo == 'Sim'){
			$classe = 'text-success';
			$ativo = 'Desativar Membro';
			$icone = 'fa-check-square';
			$ativar = 'Não';
			$inativa = '';
			$tab = 'Ativo';

		}else{
			$classe = 'text-danger';
			$ativo = 'Ativar Membro';
			$icone = 'fa-square';
			$ativar = 'Sim';
			$inativa = 'text-muted';
			$tab = 'Inativo';
		}


					$query_con = $pdo->query("SELECT * FROM igrejas where id = '$igreja'");
					$res_con = $query_con->fetchAll(PDO::FETCH_ASSOC);
					if(count($res_con) > 0){
						$nome_ig = $res_con[0]['nome'];
					}else{
						$nome_ig = $nome_igreja_sistema;
					}

					$query_con = $pdo->query("SELECT * FROM cargos where id = '$cargo'");
					$res_con = $query_con->fetchAll(PDO::FETCH_ASSOC);
					if(count($res_con) > 0){
						$nome_cargo = $res_con[0]['nome'];
					}else{
						$nome_cargo = '';
					}


					//retirar quebra de texto do obs
					$obs = str_replace(array("\n", "\r"), ' + ', $obs);

					$data_nascF = implode('/', array_reverse(explode('-', $data_nasc)));
					$data_cadF = implode('/', array_reverse(explode('-', $data_cad)));
					$data_batF = implode('/', array_reverse(explode('-', $data_bat)));
					?>			
					<tr class="<?php echo $inativa ?>">
						<td><?php echo $nome ?></td>
						<td><?php echo $cpf ?></td>
						<td class="esc"><?php echo $email ?></td>
						<td class="esc"><?php echo $telefone ?></td>
						<td class="esc"><?php echo $nome_cargo ?></td>
						
						<td class="esc"><img src="../img/membros/<?php echo $foto ?>" width="30px"></td>

						<td class="d-none"><?php echo $tab ?></td>
						
						<td>
							<big>
							<a href="#" onclick="editar('<?php echo $id ?>', '<?php echo $nome ?>', '<?php echo $cpf ?>', '<?php echo $email ?>', '<?php echo $telefone ?>', '<?php echo $endereco ?>', '<?php echo $foto ?>', '<?php echo $data_nasc ?>', '<?php echo $igreja ?>', '<?php echo $nome_ig ?>', '<?php echo $data_bat ?>', '<?php echo $cargo ?>')" title="Editar Registro">	<i class="fa-solid fa fa-pen text-primary"></i> </a>

							<a href="#" onclick="excluir('<?php echo $id ?>' , '<?php echo $nome ?>')" title="Excluir Registro">	<i class="fa fa-trash text-danger"></i> </a>

							<a href="#" onclick="dados('<?php echo $nome ?>', '<?php echo $cpf ?>', '<?php echo $email ?>', '<?php echo $telefone ?>', '<?php echo $endereco ?>', '<?php echo $foto ?>', '<?php echo $data_nascF ?>', '<?php echo $data_cadF ?>', '<?php echo $nome_ig ?>', '<?php echo $data_batF ?>', '<?php echo $nome_cargo ?>')" title="Ver Dados">	<i class="fa fa-info-circle text-primary"></i> </a>

							<a href="#" onclick="obs('<?php echo $id ?>','<?php echo $nome ?>', '<?php echo $obs ?>')" title="Observações">	<i class="fa-regular fa fa-comment-dots text-secondary <?php echo $classe_obs ?>"></i> </a>


							<a href="#" onclick="mudarStatus('<?php echo $id ?>', '<?php echo $ativar ?>')" title="<?php echo $ativo ?>">
								<i class="fa <?php echo $icone ?> <?php echo $classe ?>"></i></a>


								<!--<a href="../rel/relCarteirinha.php?id=<?php echo $id ?>" title="Gerar Carteirinha" target="_blank">
								<i class="fa fa-address-card text-primary"></i></a>-->
								<a href="../rel/relCarteirinha.php?id=<?php echo $id ?>" type="button" class="btn btn-success btn-sm " title="Gerar Carteirinha" target="_blank">Gerar Carteira</a>

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
								<label for="exampleFormControlInput1" class="form-label">Nome</label>
								<input type="text" class="form-control" id="nome" name="nome" placeholder="Insira o Nome"  required>
							</div>
						</div>
						<div class="col-md-3">
							<div class="mb-3">
								<label for="exampleFormControlInput1" class="form-label">CPF</label>
								<input type="text" class="form-control" id="cpf" name="cpf" placeholder="Insira o CPF"  >
							</div>
						</div>

						<div class="col-md-3">
							<div class="mb-3">
								<label for="exampleFormControlInput1" class="form-label">Email</label>
								<input type="email" class="form-control" id="email" name="email" placeholder="Insira o Email" >
							</div>
						</div>

						<div class="col-md-3">
							<div class="mb-3">
								<label for="exampleFormControlInput1" class="form-label">Data Nasc</label>
								<input type="date" class="form-control" id="data_nasc" name="data_nasc" value="<?php echo date('Y-m-d') ?>" >
							</div>
						</div>

					</div>
					<div class="row">
						

						<div class="col-md-3">
							<div class="mb-3">
								<label for="exampleFormControlInput1" class="form-label">Telefone</label>
								<input type="text" class="form-control" id="telefone" name="telefone" placeholder="Insira o Telefone" >
							</div>
						</div>

						<div class="col-md-9">
							<div class="mb-3">
								<label for="exampleFormControlInput1" class="form-label">Endereço</label>
								<input type="text" class="form-control" id="endereco" name="endereco" placeholder="Insira o Endereço">
							</div>
						</div>


					</div>

					<div class="row">
						
						<div class="col-md-4">
							<div class="mb-3">
								<label for="exampleFormControlInput1" class="form-label">Foto</label>
								<input type="file" class="form-control-file" id="imagem" name="imagem" onChange="carregarImg();">
							</div>
						</div>
						<div class="col-md-2">
							<div id="divImg" class="mt-4">
								<img src="../img/membros/sem-foto.jpg"  width="100px" id="target">									
							</div>
						</div>

						<div class="col-md-3">
							<div class="mb-3">
								<label for="exampleFormControlInput1" class="form-label">Cargo Ministerial</label>
								<select class="form-control sel2" id="cargo" name="cargo" style="width:100%;">
									<?php 
									$query = $pdo->query("SELECT * FROM cargos order by id asc");
									$res = $query->fetchAll(PDO::FETCH_ASSOC);
									$total_reg = count($res);
									if($total_reg > 0){

										for($i=0; $i < $total_reg; $i++){
											foreach ($res[$i] as $key => $value){} 

											$nome_reg = $res[$i]['nome'];
											$id_reg = $res[$i]['id'];
											?>
											<option value="<?php echo $id_reg ?>"><?php echo $nome_reg ?></option>

										<?php }} ?>
									</select>
								</div>

							</div>


							<div class="col-md-3">
								<div class="mb-3">
									<label for="exampleFormControlInput1" class="form-label">Data Batismo</label>
									<input type="date" class="form-control" id="data_bat" name="data_bat">
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
		<div class="modal-dialog">
			<div class="modal-content">
				<div class="modal-header">
					<h5 class="modal-title" id="exampleModalLabel">Nome : <span id="nome-dados"></span></h5>
					<button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
				</div>

				<div class="modal-body">

					<span class=""><b>CPF:</b> <span id="cpf-dados"></span></span>
					<hr style="margin:4px">

					<span class=""><b>Email:</b> <span id="email-dados"></span></span>
					<hr style="margin:4px">

					<span class=""><b>Telefone:</b> <span id="telefone-dados"></span></span>
					<hr style="margin:4px">

					<span class=""><b>Endereço:</b> <span id="endereco-dados"></span></span>
					<hr style="margin:4px">

					<span class=""><b>Data de Cadastro:</b> <span id="cadastro-dados"></span></span>
					<hr style="margin:4px">

					<span class=""><b>Data de Nascimento:</b> <span id="nasc-dados"></span></span>
					<hr style="margin:4px">

					<span class=""><b>Igreja:</b> <span id="igreja-dados"></span></span>
					<hr style="margin:4px">

					<span class=""><b>Data de Batismo:</b> <span id="batismo-dados"></span></span>
					<hr style="margin:4px">

					<span class=""><b>Cargo:</b> <span id="membro-dados"></span></span>
					<hr style="margin:4px">

					<span class=""><img src="" id="foto-dados" width="200px"></span>
					<hr style="margin:4px">


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
						<label for="exampleFormControlInput1" class="form-label">Observações (Máximo 500 Caracteres)</label>
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




<script type="text/javascript">var pag = "<?=$pagina?>"</script>
<script src="../js/ajax.js"></script>


<script type="text/javascript">

	function editar(id, nome, cpf, email, telefone, endereco, foto, data_nasc, igreja, nome_ig, data_bat, cargo){
		$('#id').val(id);
		$('#nome').val(nome);
		$('#email').val(email);
		$('#cpf').val(cpf);
		$('#telefone').val(telefone);
		$('#endereco').val(endereco);
		$('#data_nasc').val(data_nasc);
		$('#data_bat').val(data_bat);
		$('#target').attr('src', '../img/membros/' + foto);
		
		$('#igreja').val(igreja).change();
		$('#cargo').val(cargo).change();
		
		$('#tituloModal').text('Editar Registro');
		var myModal = new bootstrap.Modal(document.getElementById('modalForm'), {		});
		myModal.show();
		$('#mensagem').text('');
	}



	function dados(nome, cpf, email, telefone, endereco, foto, data_nasc, data_cad, igreja, data_bat, cargo){

		if(data_bat === '00/00/0000'){
			data_bat = 'Não Batizado!';
		}

		$('#nome-dados').text(nome);
		$('#cpf-dados').text(cpf);
		$('#email-dados').text(email);
		$('#telefone-dados').text(telefone);
		$('#endereco-dados').text(endereco);
		$('#cadastro-dados').text(data_cad);
		$('#nasc-dados').text(data_nasc);
		$('#igreja-dados').text(igreja);
		$('#batismo-dados').text(data_bat);
		$('#membro-dados').text(cargo);
		$('#foto-dados').attr('src', '../img/membros/' + foto);
		
		
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

	function limpar(){
		var data = "<?=$data_atual?>";

		$('#id').val('');
		$('#nome').val('');		
		$('#email').val('');
		$('#cpf').val('');
		$('#telefone').val('');
		$('#endereco').val('');
		$('#data_nasc').val(data);

		document.getElementById("cargo").options.selectedIndex = 0;
		$('#cargo').val($('#cargo').val()).change();
		
		$('#target').attr('src', '../img/membros/sem-foto.jpg');
	}

</script>



<link href="https://cdn.jsdelivr.net/npm/select2@4.1.0-rc.0/dist/css/select2.min.css" rel="stylesheet" />
<script src="https://cdn.jsdelivr.net/npm/select2@4.1.0-rc.0/dist/js/select2.min.js"></script>

<script>
	$(document).ready(function() {
		$('.sel2').select2({
			//placeholder: 'Selecione um Cliente',
			dropdownParent: $('#modalForm')
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