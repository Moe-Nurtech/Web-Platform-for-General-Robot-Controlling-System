const { exec, spawn } = require('child_process');
exec('getwifiip.bat', (err, stdout, stderr) => {
  if (err) {
    console.error(err);
    return;
  }
	var r = /\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b/;
	var t = stdout.match(r);
	console.log(t[0])

});