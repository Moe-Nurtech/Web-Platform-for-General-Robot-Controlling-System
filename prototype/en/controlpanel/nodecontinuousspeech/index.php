<?php
$cmddata = exec('netsh interface ip show address "Wi-Fi" | findstr "IP Address"');
$ip = str_replace("IP Address: ", "",$cmddata);
$ip = str_replace(" ", "",$ip);
?>
<html>
<body>
    <div id="root"></div>
    <script>
        var host = <?php echo "'ws://$ip:6969'" ?>;
        var socket = new WebSocket(host);
		
		
		socket.binaryType = "blob";

// Log socket opening and closing
socket.addEventListener("open", event => {
    console.log("Websocket connection opened");
});
socket.addEventListener("close", event => {
    console.log("Websocket connection closed");
});

// Handle the message
socket.addEventListener("message", event => {
    if (event.data instanceof Blob) {
        reader = new FileReader();

        reader.onload = () => {
            console.log("Result: " + reader.result);
			document.getElementById('root').innerHTML = reader.result;
        };

        reader.readAsText(event.data);
    } else {
        console.log("Result: " + event.data);
		document.getElementById('root').innerHTML = reader.result;
    }
});
		
		
    </script>
</body>
</html>

