<html>
<head>
	<title>Home</title>
	<link rel="stylesheet" type="text/css" href="vendor/bootstrap/css/bootstrap.css">
	<link rel="stylesheet" type="text/css" href="mystyle.css">


	<script src="vendor/bootstrap/js/bootstrap.min.js" crossorigin="anonymous"></script>
</head>
<body>
 
	<a href="tambah.php">+ TAMBAH MAHASISWA</a>
	<br/>
	<br/>
	<table border="1">
		<tr>
			<th>NO</th>
			<th>Nama</th>
			<th>Product</th>
			<th>Category</th>
			<th>Price</th>
			<th>Action</th>
		</tr>
		<?php 
		include 'koneksi.php';
		$no = 1;
		$data = mysqli_query($koneksi,"SELECT cashier.name_cashier, product.name,category.name_category, product.price FROM product INNER JOIN cashier ON cashier.id=product.id_cashier INNER JOIN category ON category.id=product.id_category
		");
		while($d = mysqli_fetch_array($data)){
			?>
			<tr>
				<td><?php echo $no++; ?></td>
				<td><?php echo $d['name_cashier']; ?></td>
				<td><?php echo $d['name']; ?></td>
                <td><?php echo $d['name_category']; ?></td>
                <td><?php echo $d['price']; ?></td>
                
				<td>
					<a href="edit.php?id=<?php echo $d['id']; ?>">EDIT</a>
					<a href="hapus.php?id=<?php echo $d['id']; ?>">HAPUS</a>
				</td>
			</tr>
			<?php 
		}
		?>
	</table>
</body>
</html>