var http = require('http');
var fs = require('fs');
var url = require('url');

// Create a server
http.createServer( function (request, response) {  
   // Parse the request containing file name
   var pathname = url.parse(request.url).pathname;
   
   // Print the name of the file for which request is made.
   console.log("Request for " + pathname + " received.");
   
   // Read the requested file content from file system
   fs.readFile(pathname.substr(1), function (err, data) {
      if (err) {
         console.log(err);
         // HTTP Status: 404 : NOT FOUND
         // Content Type: text/plain
         response.writeHead(404, {'Content-Type': 'text/html'});
      } else {	
         //Page found	  
         // HTTP Status: 200 : OK
         // Content Type: text/plain
         response.writeHead(200, {'Content-Type': 'text/html'});	
         
         // Write the content of the file to response body
         response.write(data.toString());		
      }
      // Send the response body 
      response.end();
   });   
}).listen(8081);

// Console will print the message
console.log('Server running at http://127.0.0.1:8081/');

///////////////////////////////////////////////////////////////////////////////

// Import events module
var events = require('events');
// Create an eventEmitter object
var eventEmitter = new events.EventEmitter();

// Create an event handler as follows
var connectHandler = function connected() {
   console.log('connection succesful.');
  
   // Fire the data_received event 
   eventEmitter.emit('data_received');
}

// Bind the connection event with the handler
eventEmitter.on('connection', connectHandler);
 
// Bind the data_received event with the anonymous function
eventEmitter.on('data_received', function(){
   console.log('data received succesfully.');
});

// Fire the connection event 
eventEmitter.emit('connection');

console.log("Program Ended.");

///////////////////////////////////////////////////////////////////////////////

// Load the http module to create an http server.
var http = require('http'); 

// Create a function to handle every HTTP request
function handler(req, res){

  var form = '';

  if(req.method == "GET"){
        form = '<html>\
            <style>\
                textarea, input {\
                    width: 100%;\
                    height: 100%;\
                }\
                \
                table, th, tr {\
                    border: 1px solid black;\
                    height: 90%\
                }\
                \
                table {\
                    width: 100%;\
                    border-collapse: collapse;\
                }\
                \
                body {\
                    background-color: lightblue;\
                }\
                \
                textarea, input {\
                    color: #FFFFFF;\
                    background-color: #626B6E;\
                }\
                \
                .button {\
                    width: 100%;\
                    height: 100%;\
                    background-color: #4CAF50;\
                }\
                \
            </style>\
            \
            <head>\
                <title>Page Title</title>\
            </head>\
            \
            <body>\
                <table>\
                    <tr>\
                        <td>\
                            <textarea>Messages&#10;&#13;Messages&#10;&#13;Messages&#10;&#13;</textarea>\
                        </td>\
                        <td width="200">\
                            <textarea>User1&#10;&#13;User2&#10;&#13;User3&#10;&#13;User4&#10;&#13;</textarea>\
                        </td>\
                    </tr>\
                    <tr>\
                        <td>\
                            <input type="text" value="This is a message that has yet to be sent.&#10;&#13;" </input>\
                        </td>\
                        <td>\
                            <input type="submit" class ="button" value="Send">\
                        </td>\
                    </tr>\
                </table>\
            </body>\
        </html>\
          ';
      
  //respond
  res.setHeader('Content-Type', 'text/html');
  res.writeHead(200);
  res.end(form);
  
    }else if(req.method == 'POST'){
        //read form data
        req.on('data', function(chunk) {

        //grab form data as string
        var formdata = chunk.toString();
        //respond
        res.setHeader('Content-Type', 'text/html');
        res.writeHead(200);
        res.end(formdata);

    });

    } else {
        res.writeHead(200);
        res.end();
    };

}
///////////////////////////////////
var qs = require('querystring');

function getpost(request, response) {
    if (request.method == 'POST') {
        var body = '';
        request.on('data', function (data) {
            body += data;
            // 1e6 === 1 * Math.pow(10, 6) === 1 * 1000000 ~~~ 1MB
            if (body.length > 1e6) { 
                // FLOOD ATTACK OR FAULTY CLIENT, NUKE REQUEST
                request.connection.destroy();
            }
        });
        request.on('end', function () {

            var POST = qs.parse(body);
            // use POST
            console.log(POST);

        });
    }
}