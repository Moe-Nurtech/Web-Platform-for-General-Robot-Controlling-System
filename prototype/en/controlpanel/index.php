<?php
session_start(); 
if(!isset($_SESSION["adminid"])) {
	header ("Location: ../admin");
	die();
}



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
  
  <title>Admin</title>
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
                    <a href="../controlpanel">
                        <img src="assets/images/water-source-pipe-drop-drink-plumbing-tap-piping-v3-gesture-512-1-128x128-128x128.png" alt="UAEU" style="height: 3.8rem;">
                    </a>
                </span>
                <span class="navbar-caption-wrap"><a class="navbar-caption text-black display-4" href="../controlpanel">Admin: <font color="#e83235"><?php echo $_SESSION['adminid']; ?></font></a></span>
            </div>
        </div>
        <div class="collapse navbar-collapse" id="navbarSupportedContent">
            <ul class="navbar-nav nav-dropdown" data-app-modern-menu="true"><li class="nav-item">
                    <a class="nav-link link text-black display-4" href="../controlpanel">Home</a>
                </li><li class="nav-item"><a class="nav-link link text-black display-4" href="savedmaps" target="_blank">Saved Maps</a></li>
				<li class="nav-item"><a class="nav-link link text-black display-4" href="loadamap">Load A Map</a></li><li class="nav-item"><a class="nav-link link text-black display-4" href="gps" target="_blank">GPS</a></li>
                <li class="nav-item">
                    <a class="nav-link link text-black display-4" href="livecamera" target="_blank">Live Camera</a>
                </li>
				<li class="nav-item">
                    <a class="nav-link link text-black display-4" href="webshell" target="_blank">Web Shell</a>
                </li>
				<li class="nav-item"><a class="nav-link link text-black display-4" href="voicetotextcommands" target="_blank">Voice To Text Commands</a></li></ul>
            <div class="navbar-buttons mbr-section-btn"><a class="btn btn-sm btn-secondary-outline display-4" href="logout.php">
                    Logout</a></div>
        </div>
    </nav>
</section>

<section class="engine"><a href="https://mobirise.info/z">best css templates</a></section><section class="counters1 counters cid-rWnnxwELsI" id="counters1-g">

    

<br><br><br><br>
<br><br><br><br>    

    <div class="container">
        <h2 class="mbr-section-title pb-3 align-center mbr-fonts-style display-2">Operation Methods</h2>
        <h3 class="mbr-section-subtitle mbr-fonts-style display-5">
            <b><font color="#e83235">UAEU Abu Saif</font> Platform</b></h3>

        <div class="container pt-4 mt-2">
            <div class="media-container-row">
                <div class="card p-3 align-center col-12 col-md-6 col-lg-3">
                    <div class="panel-item p-3">
                        <div class="card-img pb-3">
                            <span class="mbr-iconfont mbri-touch"></span>
                        </div>

                        <div class="card-text">
                    
                            <h4 class="mbr-content-title mbr-bold mbr-fonts-style display-7">Python GUI Run</h4>
                            <div class="mbr-section-btn text-center"><a class="btn btn-md btn-primary display-4" href="loading.php">Start</a></div>
                        </div>
						
                    </div>
					
                </div>



                <div class="card p-3 align-center col-12 col-md-6 col-lg-3">
                    <div class="panel-item p-3">
                        <div class="card-img pb-3">
                            <span class="mbr-iconfont mbri-setting"></span>
                        </div>

                        <div class="card-text">
                    
                            <h4 class="mbr-content-title mbr-bold mbr-fonts-style display-7">Text to Speech</h4>
                            <div class="mbr-section-btn text-center"><a class="btn btn-md btn-primary display-4" href="loadingtexttospeech.php">Start</a></div>
                        </div>
						
                    </div>
					
                </div>

                <div class="card p-3 align-center col-12 col-md-6 col-lg-3">
                    <div class="panel-item p-3">
                        <div class="card-img pb-3">
                            <span class="mbr-iconfont mbri-setting"></span>
                        </div>

                        <div class="card-text">
                    
                            <h4 class="mbr-content-title mbr-bold mbr-fonts-style display-7">Facial Expressions</h4>
                            <div class="mbr-section-btn text-center"><a class="btn btn-md btn-primary display-4" href="loadingfacialexpression.php">Start</a></div>
                        </div>
						
                    </div>
					
                </div>




                <div class="card p-3 align-center col-12 col-md-6 col-lg-3">
                    <div class="panel-item p-3">
                        <div class="card-img pb-3">
                            <span class="mbr-iconfont mbri-setting"></span>
                        </div>

                        <div class="card-text">
                    
                            <h4 class="mbr-content-title mbr-bold mbr-fonts-style display-7">Speech to Text (Single)</h4>
                            <div class="mbr-section-btn text-center"><a class="btn btn-md btn-primary display-4" href="speechtotext.php">Start</a></div>
                        </div>
						
                    </div>
					
                </div>
				
                <div class="card p-3 align-center col-12 col-md-6 col-lg-3">
                    <div class="panel-item p-3">
                        <div class="card-img pb-3">
                            <span class="mbr-iconfont mbri-setting"></span>
                        </div>

                        <div class="card-text">
                    
                            <h4 class="mbr-content-title mbr-bold mbr-fonts-style display-7">Speech to Text (Cont)</h4>
                            <div class="mbr-section-btn text-center"><a class="btn btn-md btn-primary display-4" href="loadingcontspeech.php">Start</a></div>
                        </div>
						
                    </div>
					
                </div>
				
				
				

</div></div>
				
				        <div class="container pt-4 mt-2">
            <div class="media-container-row">
				

                <div class="card p-3 align-center col-12 col-md-6 col-lg-3">
                    <div class="panel-item p-3">
                        <div class="card-img pb-3">
                            <span class="mbr-iconfont mbri-key"></span>
                        </div>

                        <div class="card-text">
                    
                            <h4 class="mbr-content-title mbr-bold mbr-fonts-style display-7">Custom Web Run</h4>
                            <div class="mbr-section-btn text-center"><a class="btn btn-md btn-primary display-4" href="#">Start</a></div>
                        </div>
						
                    </div>
					
                </div>

        

		                <div class="card p-3 align-center col-12 col-md-6 col-lg-3">
                    <div class="panel-item p-3">
                        <div class="card-img pb-3">
                            <span class="mbr-iconfont mbri-setting"></span>
                        </div>

                        <div class="card-text">
                    
                            <h4 class="mbr-content-title mbr-bold mbr-fonts-style display-7">Text Chat Bot</h4>
                            <div class="mbr-section-btn text-center"><a class="btn btn-md btn-primary display-4" href="loadingtextchatbot.php">Start</a></div>
                        </div>
						
                    </div>
					
                </div>



		                <div class="card p-3 align-center col-12 col-md-6 col-lg-3">
                    <div class="panel-item p-3">
                        <div class="card-img pb-3">
                            <span class="mbr-iconfont mbri-setting"></span>
                        </div>

                        <div class="card-text">
                    
                            <h4 class="mbr-content-title mbr-bold mbr-fonts-style display-7">Chat Bot Speaker</h4>
                            <div class="mbr-section-btn text-center"><a class="btn btn-md btn-primary display-4" href="loadingtextchatbotsp.php">Start</a></div>
                        </div>
						
                    </div>
					
                </div>




    
            </div>
        </div>
   </div>
   <br><br><br><br><br><br><br>
<br><br><br><br>
<br><br><br><br>
<br><br><br><br>
<br><br>
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
  
  
</body>
</html>
