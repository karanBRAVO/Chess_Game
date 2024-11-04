import { Server as SocketServer, type Server, type Socket } from "socket.io";

interface IAuthDetails {
  id: string;
  name: string;
  username: string;
}

interface IUser extends IAuthDetails {
  socid: string;
}

interface IMatchMap {
  uid1: string;
  socid1: string;
  uid2: string;
  socid2: string;
}

interface IWaitingMap {
  uid: string;
  socid: string;
}

export class SocketService {
  private readonly _io: Server;
  private user_map: IUser[];
  private user_match_map: IMatchMap[];
  private user_waiting_map: IWaitingMap[];

  constructor() {
    console.log(`Socket service initialized`);
    this._io = new SocketServer({
      cors: {
        allowedHeaders: ["*"],
        origin: "*",
      },
    });
    this.user_map = [];
    this.user_match_map = [];
    this.user_waiting_map = [];
  }

  private userExists(socid: string) {
    return this.user_map.findIndex((v) => v.socid === socid) !== -1
      ? true
      : false;
  }

  private addToUserMap(data: IUser) {
    if (!this.userExists(data.socid)) {
      this.user_map.push(data);
    }
  }

  private removeFromUserMap(socid: string) {
    if (this.userExists(socid)) {
      this.user_map = this.user_map.filter((v) => v.socid !== socid);
    }
  }

  private isUserInMatch(uid: string) {
    return this.user_match_map.findIndex(
      (v) => v.uid1 === uid || v.uid2 === uid,
    ) !== -1
      ? true
      : false;
  }

  private createMatch(data: IMatchMap) {
    if (!this.isUserInMatch(data.uid1) && !this.isUserInMatch(data.uid2)) {
      this.user_match_map.push(data);
    }
  }

  private removeFromMatch(socid: string) {
    this.user_match_map = this.user_match_map.filter(
      (v) => v.socid1 !== socid && v.socid2 !== socid,
    );
  }

  private addToWaitingList(data: IWaitingMap) {
    this.user_waiting_map.push(data);
  }

  private removeFromWaitingList(socid: string) {
    this.user_waiting_map = this.user_waiting_map.filter(
      (v) => v.socid !== socid,
    );
  }

  public listen() {
    const io = this.io;

    io.on("connection", (socket: Socket) => {
      // get user details
      const {
        id: userId,
        name,
        username,
      } = socket.handshake.auth as IAuthDetails;
      console.log(
        `Socket connected with id ${socket.id}\nUser details: ${userId} ${name} ${username}`,
      );

      // add to user details list
      const userData: IUser = {
        id: userId,
        name: name,
        username: username,
        socid: socket.id,
      };
      this.addToUserMap(userData);

      // add to waiting list
      const waitingData: IWaitingMap = {
        uid: userId,
        socid: socket.id,
      };
      this.addToWaitingList(waitingData);

      // match-making
      if (this.user_waiting_map.length >= 2) {
        console.log(`Match making...`);
        const player1 = this.user_waiting_map[0];
        const player2 = this.user_waiting_map[1];
        this.removeFromWaitingList(player1.socid);
        this.removeFromWaitingList(player2.socid);

        const matchData: IMatchMap = {
          uid1: player1.uid,
          socid1: player1.socid,
          uid2: player2.uid,
          socid2: player2.socid,
        };
        if (
          !this.isUserInMatch(matchData.uid1) &&
          !this.isUserInMatch(matchData.uid2)
        ) {
          this.createMatch(matchData);

          // emit match details
          const player1Info = this.playerInfo(player1.socid);
          const player2Info = this.playerInfo(player2.socid);
          const firstTurn = Math.random() < 0.5 ? "w" : "b";
          this.send_message(player1.socid, "--server:match", {
            id: player2.uid,
            name: player2Info?.name,
            username: player2Info?.username,
            army: "white",
            firstTurn,
          });
          this.send_message(player2.socid, "--server:match", {
            id: player1.uid,
            name: player1Info?.name,
            username: player1Info?.username,
            army: "black",
            firstTurn,
          });
        }
      }

      this.print_info();

      // player move
      socket.on("--client:piece-move", (data) => {
        console.log(`[MOVE] Socket id: ${socket.id}`, data);
        const playerMatchInfo = this.playerMatchInfo(socket.id);
        console.log(playerMatchInfo);
        if (playerMatchInfo) {
          const opponentSocId =
            playerMatchInfo.socid1 === socket.id
              ? playerMatchInfo.socid2
              : playerMatchInfo.socid1;
          this.send_message(opponentSocId, "--server:piece-move", {
            name: data["name"],
            pos: data["pos"],
          });
        }
      });

      // disconnect
      socket.on("disconnect", () => {
        this.removeFromUserMap(socket.id);
        this.removeFromWaitingList(socket.id);
        this.removeFromMatch(socket.id);
        this.print_info();
        console.log(`Socket disconnected with id ${socket.id}`);
      });
    });
  }

  get io() {
    return this._io;
  }

  private playerInfo(socid: string) {
    return this.user_map.find((v) => v.socid === socid);
  }

  private playerMatchInfo(socid: string) {
    return this.user_match_map.find(
      (v) => v.socid1 === socid || v.socid2 === socid,
    );
  }

  private print_info() {
    console.log({
      users: this.user_map,
      match: this.user_match_map,
      waiting: this.user_waiting_map,
    });
  }

  private send_message(sid: string, evt: string, data: any) {
    this.io.to(sid).emit(evt, data);
  }
}
