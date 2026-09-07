<?php
session_start(); 
if(!isset($_SESSION["adminid"])) {
	header ("Location: ../admin");
	die();
}

$servername = "localhost";
$username = "root";
$password = "";
$dbname = "intent";

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);
// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}   


$sql = "SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_SCHEMA LIKE 'intent'";
$result = mysqli_query($conn, $sql);
$input = 'Not Found';
$text = $_POST['text'];
$intent = '';
	if(mysqli_num_rows($result)!=0) {
		while($row = mysqli_fetch_assoc($result)){
		//$row = mysqli_fetch_assoc($result);

		$intent = $row['TABLE_NAME'];
		//$sqlx = "use intent";
		//mysqli_query($conn, $sqlx);
		echo $intent;
		echo " ";
		$sql2 = "SELECT * FROM $intent WHERE phrase='$text'";
		$result2 = mysqli_query($conn, $sql2);
		//echo mysqli_num_rows($result2);
		//if($result2 != false){
			//if(mysqli_num_rows($res)) {
			//if(!$res || mysqli_num_rows($res)!=0){
		if(mysqli_num_rows($result2)!=0) {
			//if($result2 = $conn -> query("SELECT * FROM $intent WHERE phrase='$text'")){
				$row2 = mysqli_fetch_assoc($result2);
			//$input = $row2['phrase'];
				$sql3 = "use response";
				echo "in";
				mysqli_query($conn, $sql3);
				$sql4 = "SELECT * FROM $intent ORDER BY rand()";
				$result3 = mysqli_query($conn, $sql4);
			
				$row3 = mysqli_fetch_assoc($result3);
				$input = $row3['phrase'];
				break;
		}
		//if($row['password']== $mypassword){		
		//	$error = 0;
		//}
		//}
		}
	}
  


//$input = "اهلا";
//$input = $row['TABLE_NAME'];
//$input = mysqli_num_rows($result);
//$input = $_POST['text'];
$conn->close();
?>
<form method="post" action="textchatbot.php" id="registerform">



	
<input type="hidden" name="msg" value="<?php echo $input; ?>">

</form>

<script>

document.getElementById("registerform").submit();

</script>
