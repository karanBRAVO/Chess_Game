import http, { type Server } from "node:http";
import { SocketService } from "@app/services/index";

export class ServerService {
  private readonly _PORT: number;
  private readonly _server: Server;

  constructor(port: number) {
    this._PORT = port;
    this._server = http.createServer((req, res) => {
      if (req.method === "GET" && req.url === "/health") {
        res.writeHead(200, { "Content-Type": "text/plain" });
        res.end("Hello, world!");
      }
    });
  }

  public start() {
    const server = this.server;
    const socket = new SocketService();
    socket.io.attach(server);
    server.listen(this.port, "0.0.0.0", () => {
      console.log(`Server listening on port ${this.port}`);
    });
    socket.listen();
  }

  get server() {
    return this._server;
  }

  get port() {
    return this._PORT;
  }
}
