import http, {IncomingMessage, ServerResponse} from 'http'

console.log("Hello! Node.js × TypeScript");

const server = http.createServer((req: IncomingMessage, res: ServerResponse) => {
    // ここに処理を記述
    res.writeHead(200, { 'Content-Type': 'text/html; charset=utf-8' });
    res.write('<h1>Hello Node HTTP!</h1>');
    res.end();
});

const port = 8080;
server.listen(port);
console.log('Server listen on port ' + port);