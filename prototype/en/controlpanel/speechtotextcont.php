
<?php
session_start(); 
if(!isset($_SESSION["adminid"])) {
	header ("Location: ../admin");
	die();
}


$cmddata = exec('netsh interface ip show address "Wi-Fi" | findstr "IP Address"');
$ip = str_replace("IP Address: ", "",$cmddata);
$ip = str_replace(" ", "",$ip);
?>

<!DOCTYPE html>
<html  >
<head>
  <!-- Site made with Mobirise Website Builder v4.11.4, https://mobirise.com -->
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="generator" content="Mobirise v4.11.4, mobirise.com">
  <meta name="viewport" content="width=device-width, initial-scale=1, minimum-scale=1">
  <link rel="shortcut icon" href="assets/images/water-source-pipe-drop-drink-plumbing-tap-piping-v3-gesture-512-1-128x128-128x128.png" type="image/x-icon">
  <meta name="description" content="">
  
  <title>Facial Expressions</title>
  <link rel="stylesheet" href="assets/web/assets/mobirise-icons/mobirise-icons.css">
  <link rel="stylesheet" href="assets/bootstrap/css/bootstrap.min.css">
  <link rel="stylesheet" href="assets/bootstrap/css/bootstrap-grid.min.css">
  <link rel="stylesheet" href="assets/bootstrap/css/bootstrap-reboot.min.css">
  <link rel="stylesheet" href="assets/tether/tether.min.css">
  <link rel="stylesheet" href="assets/dropdown/css/style.css">
  <link rel="stylesheet" href="assets/theme/css/style.css">
  <link rel="preload" as="style" href="assets/mobirise/css/mbr-additional.css"><link rel="stylesheet" href="assets/mobirise/css/mbr-additional.css" type="text/css">
  
  
  
</head>
<body>
  <section class="menu cid-rSknZJrHWX" once="menu" id="menu2-0">

    

    <nav class="navbar navbar-expand beta-menu navbar-dropdown align-items-center navbar-fixed-top collapsed bg-color transparent">
        <button class="navbar-toggler navbar-toggler-right" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
            <div class="hamburger">
                <span></span>
                <span></span>
                <span></span>
                <span></span>
            </div>
        </button>
        <div class="menu-logo">
            <div class="navbar-brand">
                <span class="navbar-logo">
                    <a href="#">
                        <img src="assets/images/water-source-pipe-drop-drink-plumbing-tap-piping-v3-gesture-512-1-128x128-128x128.png" alt="UAEU" style="height: 3.8rem;">
                    </a>
                </span>
                <span class="navbar-caption-wrap"><a class="navbar-caption text-black display-4" href="#">Admin: <font color="#e83235"><?php echo $_SESSION['adminid']; ?></font></a></span>
            </div>
        </div>
        <div class="collapse navbar-collapse" id="navbarSupportedContent">
    
            <div class="navbar-buttons mbr-section-btn"><a class="btn btn-sm btn-secondary-outline display-4" href="stopping.php">
                    Stop</a></div>
        </div>
    </nav>
</section>

<section class="engine"><a href="https://mobirise.info/z">best css templates</a></section><section class="counters1 counters cid-rWnnxwELsI" id="counters1-g">

    

    <br><br><br><br>


    <div class="container">
        <h2 class="mbr-section-title pb-3 align-center mbr-fonts-style display-2">Please Speak To The Microphone In Arabic</h2>
        <h3 class="mbr-section-subtitle mbr-fonts-style display-5">
            <b><font color="green"><div id="root"></div>
</font></b>
        </h3>

        <div class="container pt-4 mt-2">
            <div class="media-container-row">
                <div class="card p-3 align-center col-12 col-md-6 col-lg-3">
                    <div class="panel-item p-3">
                        <div class="card-img pb-3">
                            <span class="mbr-iconfont mbri-logout"></span>
                        </div>

                        <div class="card-text">
                    
                            <h4 class="mbr-content-title mbr-bold mbr-fonts-style display-7">Speech to Text Continuous Run</h4>
                            <div class="mbr-section-btn text-center"><a class="btn btn-sm btn-secondary-outline display-4" href="stoppingcont.php">Stop</a></div>
                        </div>
						
                    </div>
					
                </div>




    
            </div>
        </div>
		
		
		
		
		
		
   </div>
   <br><br><br><br><br><br><br>
   <br><br><br><br><br><br><br>
   <br><br><br><br><br><br><br>
   <br><br><br>
</section>



<section once="footers" class="cid-rWoyfESiJh" id="footer6-m">

   
    <div class="container">
        <div class="media-container-row align-center mbr-white">
            <div class="col-12">
                <p class="mbr-text mb-0 mbr-fonts-style display-7">
                    © Copyright - UAEU AI & Robotics Lab
                </p>
            </div>
        </div>
    </div>
</section>

  <script src="assets/web/assets/jquery/jquery.min.js"></script>
  <script src="assets/popper/popper.min.js"></script>
  <script src="assets/bootstrap/js/bootstrap.min.js"></script>
  <script src="assets/tether/tether.min.js"></script>
  <script src="assets/smoothscroll/smooth-scroll.js"></script>
  <script src="assets/dropdown/js/nav-dropdown.js"></script>
  <script src="assets/dropdown/js/navbar-dropdown.js"></script>
  <script src="assets/touchswipe/jquery.touch-swipe.min.js"></script>
  <script src="assets/viewportchecker/jquery.viewportchecker.js"></script>
  <script src="assets/theme/js/script.js"></script>
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
            
			document.getElementById('root').innerHTML = reader.result;
        };

        reader.readAsText(event.data);
    } else {
        
		document.getElementById('root').innerHTML = reader.result;
    }
});
		
		
    </script>
  
  
</body>
</html>
