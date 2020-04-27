const express = require('express');
const mysql = require('mysql');
const cors = require('cors');
const app = express();

const VARIABLES_I_NEED = "user_name,avatar_url,platform,region,elo,victory,defeat,streak"

const SELECT_ALL_PLAYERS =
    `select @r:=@r+1 as ranking,${VARIABLES_I_NEED}\n` +
    "from players,(select @r:=0) as r order by elo desc\n";

const connection = mysql.createConnection(
    {
        host: 'localhost',
        user: 'root',
        password: 'idfrgenestl',
        database: 'darwin1v1league'
    }
);

app.use(cors());

app.get('/leaderboard', function (req, res) {
    connection.query(SELECT_ALL_PLAYERS, (err, results) => {
        if (err) {
            return res.send(err)
        } else {
            return res.json(results)
        }

    })
})

app.listen(8080, function () {
    console.log('Example app listening on port 8080!')
})