var PORT = 33333;
var HOST = 'localhost';
var dgram = require('dgram');
var server = dgram.createSocket('udp4');
var fs = require("fs");
var log = require('sys').log;


server.on('message', function (message, remote) {
	log(message)
	fs.readFile(message, function (err,data) {
	  	if (err) {
	    	return console.log(err);
	  	}
	  	server.send(data, 0, data.length, PORT, HOST, function(err, bytes) {
	    	if (err) 
	        	throw err
	    log('UDP file sent to ' + HOST +':'+ PORT);
	    log('File size: ' + data.length);
	  });
	});
});


server.bind(PORT, HOST);

