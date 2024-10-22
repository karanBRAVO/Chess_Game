import type { Server, Socket } from "socket.io";
import { Server as SocketServer } from "socket.io";

export class SocketService {
  private readonly _io: Server;

  constructor() {
    console.log(`Socket service initialized`);
    this._io = new SocketServer({
      cors: {
        allowedHeaders: ["*"],
        origin: "*",
      },
    });
  }

  public listen() {
    const io = this.io;

    io.on("connection", (socket: Socket) => {
      console.log(`Socket connected with id ${socket.id}`);

      socket.on("disconnect", () => {
        console.log(`Socket disconnected with id ${socket.id}`);
      });
    });
  }

  get io() {
    return this._io;
  }
}
