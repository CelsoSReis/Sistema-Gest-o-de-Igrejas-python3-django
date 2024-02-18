<?php 
require_once("../conexao.php");
require_once("verificar.php");
$pagina = 'usuarios';
?>

<div class="tabela bg-light mt-4">
	<?php 

	$query = $pdo->query("SELECT * FROM $pagina order by id desc");
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
					<th class="esc">Senha</th>
					<th class="esc">Igreja</th>
					<th class="esc">Foto</th>
					
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
					$senha = $res[$i]['senha'];
					
					$foto = $res[$i]['foto'];
					$igreja = $res[$i]['igreja'];
					$id = $res[$i]['id'];


					$query_con = $pdo->query("SELECT * FROM igrejas where id = '$igreja'");
					$res_con = $query_con->fetchAll(PDO::FETCH_ASSOC);
					if(count($res_con) > 0){
						$nome_ig = $res_con[0]['nome'];
					}else{
						$nome_ig = $nome_igreja_sistema;
					}

					?>			
					<tr>
						<td><?php echo $nome ?></td>
						<td><?php echo $cpf ?></td>
						<td class="esc"><?php echo $email ?></td>
						<td class="esc"><?php echo $senha ?></td>
						<td class="esc"><?php echo $nome_ig ?></td>
						<td class="esc"><img src="../img/membros/<?php echo $foto ?>" width="30px"></td>
						
						<td>
							<a href="#" onclick="editar('<?php echo $id ?>', '<?php echo $nome ?>', '<?php echo $senha ?>')" title="Editar Senha">	<i class="bi bi-pencil-square text-primary"></i> </a>
							
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
	<div class="modal-dialog">
		<div class="modal-content">
			<div class="modal-header">
				<h5 class="modal-title" id="tituloModal"></h5>
				<button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
			</div>
			<form id="form" method="post">
				<div class="modal-body">
					
							<div class="mb-3">
								<label for="exampleFormControlInput1" class="form-label">Senha</label>
								<input type="text" class="form-control" id="senha" name="senha" placeholder="Insira a Senha" required>
							</div>
						
							
					<input type="hidden" id="id" name="id">

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







<script type="text/javascript">var pag = "<?=$pagina?>"</script>
<script src="../js/ajax.js"></script>


<script type="text/javascript">

	function editar(id, nome, senha){
		$('#id').val(id);
		
		$('#senha').val(senha);
				
		$('#tituloModal').text('Editar Senha');
		var myModal = new bootstrap.Modal(document.getElementById('modalForm'), {		});
		myModal.show();
		$('#mensagem').text('');
	}




</script>