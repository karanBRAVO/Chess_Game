// imports
import { config } from "dotenv";
import { ServerService } from "@app/services/index";

// Load the dotenv file
config();

// define the port number
const PORT: number = Number(process.env.PORT) || 8000;

// start the server
try {
  const socket = new ServerService(PORT);
  socket.start();
} catch (err: any) {
  console.log(err);
}
