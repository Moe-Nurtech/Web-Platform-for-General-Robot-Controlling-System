<?php
session_start(); 
if(!isset($_SESSION["adminid"])) {
	header ("Location: ../../admin");
	die();
}



?>

<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">

  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="generator" content="Mobirise v4.11.4, mobirise.com">
  <meta name="viewport" content="width=device-width, initial-scale=1, minimum-scale=1">
  <link rel="shortcut icon" href="assets/images/water-source-pipe-drop-drink-plumbing-tap-piping-v3-gesture-512-1-128x128-128x128.png" type="image/x-icon">
  <meta name="description" content="">
  
  <title>Joystick Control</title>
  <link rel="stylesheet" href="assets/web/assets/mobirise-icons/mobirise-icons.css">
  <link rel="stylesheet" href="assets/bootstrap/css/bootstrap.min.css">
  <link rel="stylesheet" href="assets/bootstrap/css/bootstrap-grid.min.css">
  <link rel="stylesheet" href="assets/bootstrap/css/bootstrap-reboot.min.css">
  <link rel="stylesheet" href="assets/tether/tether.min.css">
  <link rel="stylesheet" href="assets/dropdown/css/style.css">
  <link rel="stylesheet" href="assets/theme/css/style.css">
  <link rel="preload" as="style" href="assets/mobirise/css/mbr-additional.css"><link rel="stylesheet" href="assets/mobirise/css/mbr-additional.css" type="text/css">


  <script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/nipplejs/0.7.3/nipplejs.js"></script>
<script type="text/javascript" src="http://static.robotwebtools.org/roslibjs/current/roslib.min.js"></script>

<script type="text/javascript" type="text/javascript">
  var ros = new ROSLIB.Ros({
    url : 'ws://localhost:9090'
  });

  ros.on('connection', function() {
    document.getElementById("status").innerHTML = "Connected";
  });

  ros.on('error', function(error) {
    document.getElementById("status").innerHTML = "Error";
  });

  ros.on('close', function() {
    document.getElementById("status").innerHTML = "Closed";
  });
</script>

<script>
var txt_listener = new ROSLIB.Topic({
    ros : ros,
    name : '/txt_msg',
    messageType : 'std_msgs/String'
  });

  txt_listener.subscribe(function(m) {
    document.getElementById("msg").innerHTML = m.data;
  });



cmd_vel_listener = new ROSLIB.Topic({
    ros : ros,
    name : "/cmd_vel",
    messageType : 'geometry_msgs/Twist'
  });

  move = function (linear, angular) {
    var twist = new ROSLIB.Message({
      linear: {
        x: linear,
        y: 0,
        z: 0
      },
      angular: {
        x: 0,
        y: 0,
        z: angular
      }
    });
    cmd_vel_listener.publish(twist);
  }



  txt_listener.subscribe(function(m) {
    document.getElementById("msg").innerHTML = m.data;
    move(1, 0);
  });


    createJoystick = function () {
      var options = {
        zone: document.getElementById('zone_joystick'),
        threshold: 0.1,
        position: { left: 50 + '%' },
        mode: 'static',
        size: 150,
        color: '#000000',
      };
      manager = nipplejs.create(options);

      linear_speed = 0;
      angular_speed = 0;

      self.manager.on('start', function (event, nipple) {
        console.log("Movement start");
      });

      self.manager.on('move', function (event, nipple) {
        console.log("Moving");
      });

      self.manager.on('end', function () {
        console.log("Movement end");
      });



manager.on('start', function (event, nipple) {
  timer = setInterval(function () {
    move(linear_speed, angular_speed);
  }, 25);
});

manager.on('end', function () {
  if (timer) {
    clearInterval(timer);
  }
  self.move(0, 0);
});


manager.on('move', function (event, nipple) {
  max_linear = 5.0; // m/s
  max_angular = 2.0; // rad/s
  max_distance = 75.0; // pixels;
  linear_speed = Math.sin(nipple.angle.radian) * max_linear * nipple.distance/max_distance;
  angular_speed = -Math.cos(nipple.angle.radian) * max_angular * nipple.distance/max_distance;
});





    }
    window.onload = function () {
      createJoystick();
    }



</script>

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
                    Stop Navigation</a></div>
        </div>
    </nav>
</section>

<section class="engine"><a href="https://mobirise.info/z">best css templates</a></section><section class="counters1 counters cid-rWnnxwELsI" id="counters1-g">

    

<br><br><br><br>
<br><br><br><br>    

    <div class="container">
        <h2 class="mbr-section-title pb-3 align-center mbr-fonts-style display-2">Joystick Control</h2>
        <h3 class="mbr-section-subtitle mbr-fonts-style display-5">
            <b><font color="#e83235">Connection Status: </font><span id="status"></span></b>
<br>

<b><font color="#e83235">Last /txt_msg received: </font><span id="msg"></span></b>

</h3>
<br><br><br><br><br><br>
  <div id="zone_joystick" style="position: relative;"></div>

  <br><br><br><br>
  <br><br><br><br>


    <div class="container">

        <div class="container pt-4 mt-2">
            <div class="media-container-row">
                <div class="card p-3 align-center col-12 col-md-6 col-lg-3">
                    <div class="panel-item p-3">
                        <div class="card-img pb-3">
                            <span class="mbr-iconfont mbri-logout"></span>
                        </div>

                        <div class="card-text">
                    
                            <h4 class="mbr-content-title mbr-bold mbr-fonts-style display-7">Joystick Control</h4>
                            <div class="mbr-section-btn text-center"><a class="btn btn-sm btn-secondary-outline display-4" href="../">Stop Controller</a></div>
                        </div>
                        
                    </div>
                    
                </div>



                <div class="card p-3 align-center col-12 col-md-6 col-lg-3">
                    <div class="panel-item p-3">
                        <div class="card-img pb-3">
                            <span class="mbr-iconfont mbri-map-pin"></span>
                        </div>

                        <div class="card-text">
                    
                            <h4 class="mbr-content-title mbr-bold mbr-fonts-style display-7">Save Map</h4>
                            <div class="mbr-section-btn text-center"><a class="btn btn-md btn-primary display-4" href="#">Save</a></div>
                        </div>
                        
                    </div>
                    
                </div>

        



    
            </div>
        </div>
   </div>
   </div>

<br><br><br><br>
<br><br><br><br>
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
</body>
</html>
