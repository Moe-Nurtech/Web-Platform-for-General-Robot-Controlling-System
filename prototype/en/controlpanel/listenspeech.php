<?php
set_time_limit (0);

$address = "127.0.0.1";

$port = 12347;
$con = 1;
$input = "";

$sock = socket_create(AF_INET, SOCK_STREAM, 0);
$bind = socket_bind($sock, $address, $port);

socket_listen($sock);

while ($con == 1)
{
    $client = socket_accept($sock);
    $input = socket_read($client, 2024);

    if ($input != "") 
    {
        $close = socket_close($sock);
        $con = 0;
		echo $input;
    }

}

//header("Location: display.php?msg=".$input);
?>
<form method="post" action="speechtotext.php" id="registerform">



	
<input type="hidden" name="msg" value="<?php echo $input; ?>">

</form>

<script>

document.getElementById("registerform").submit();

</script>

