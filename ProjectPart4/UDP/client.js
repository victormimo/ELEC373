var PORT = 33333;
var HOST = 'localhost';
var dgram = require('dgram');
var log = require('sys').log;
var client = dgram.createSocket('udp4');
var fs = require("fs");
var wstream = fs.createWriteStream('client.receive');

 client.send('server.send', PORT, HOST, function(err, bytes) {
    if (err) 
        throw err;
    log('File name sent to ' + HOST +':'+ PORT);
    
  });

client.on('message', function (message, remote) {
    wstream.write(message);
    wstream.end();
});

wstream.on('finish', function () {
  console.log('file has been written');
});

