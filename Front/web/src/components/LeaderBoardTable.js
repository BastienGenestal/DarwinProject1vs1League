import React from 'react';
import {bindActionCreators} from "redux";
import {connect} from "react-redux";
import {actionGetLeaderboard} from '../actions/LeaderboardActions'
import {loaders} from './loaders'
import SimpleTable from "./SimpleTable";
import {MDBCol, MDBRow} from "mdbreact";
import './Table.css'
import gold from '../data/image/medals/1.png'
import silver from '../data/image/medals/2.png'
import bronze from '../data/image/medals/3.png'
import steamLogo from '../data/image/logos/PC.png'
import XboxLogo from '../data/image/logos/Xbox.png'
import PS4Logo from '../data/image/logos/PS4.png'

class LeaderBoardTable extends React.Component {

    componentDidMount() {
        this.props.actionGetLeaderboard()
    }

    display_medal(player) {
        if (player.ranking > 3)
            return player.ranking
        const src = player.ranking === 3 ? gold : player.ranking === 2 ? silver : bronze
        return <span className="container_medal">
            <img className="player_medal" width="50px" height="50px" src={src} alt="medal"/>
            <div className="centered">{player.ranking}</div>
        </span>
    }

    display_avatar(player) {
        return <span className="profile_col">
            <img className="player_avatar" src={player.avatar_url} alt="avatar"/>
            {player.user_name}
        </span>
    }

    get_winrate(player) {
        if (!player.victory)
            return ''
        const winrate = Math.round((player.victory / (player.victory + player.defeat)) * 100, 2)
        let color = ''
        if (winrate > 50)
            color = "#45ff51"
        if (winrate < 50)
            color = "#ff8345"
        return <div style={{color: color}}>{winrate} %</div>
    }

    get_streak(player) {
        if (!player.streak)
            return ''
        return player.streak
    }

    get_matchplayed(player) {
        const match_played = player.victory + player.defeat
        if (!match_played)
            return ''
        return match_played
    }

    get_platform(row) {
        let src = ''
        switch (row.platform) {
            case 'PC':
                src = steamLogo
                break;
            case 'Xbox':
                src = XboxLogo
                break;
            case 'PS4':
                src = PS4Logo
                break;
            default:
                break;
        }
        if (!src)
            return ''
        return <img width="50px" height="50px" src={src} alt={row.platform}/>
    }

    get_rank_and_color_from_elo(elo) {
        const rolesValues = [
            ["Godlike", 1500, "rgba(252, 196, 22, 0.95)"],
            ["Master", 750, "rgba(255, 125, 0, 0.95)"],
            ["Pro", 600, "rgba(181, 102, 241, 0.65)"],
            ["Expert", 550, "rgba(81, 165, 248, 0.65)"],
            ["Inmate", 400, "rgba(62, 238, 80, 0.65)"],
            ["Newbie", 250, "rgba(255, 255, 255, 0.5)"],
            ["Medkit", 100, "rgba(80, 80, 80, 0.65)"]
        ]
        for (let i = 0; i < rolesValues.length; i++)
            if (elo >= rolesValues[i][1])
                return rolesValues[i]
    }

    render_elo(row) {
        const rank = this.get_rank_and_color_from_elo(row.elo)
        return <div className="elo-col">
                {row.elo}
                <div className={"rank-badge " + rank[0]} style={{backgroundColor: rank[2]}}>
                    {rank[0]}
                </div>
        </div>
    }

    render() {
        const {Leaderboard, LeaderboardIsLoading} = this.props

        if (LeaderboardIsLoading) return loaders[Math.floor(Math.random() * loaders.length)]
        if (Leaderboard === -1)
            return <div>Seems like server is dead lul</div>
        return (
            <MDBRow style={{width: '100%'}}>
                <MDBCol>
                    <SimpleTable
                        name="leaderboard_table"
                        filterable
                        data={Leaderboard}
                        columns=
                            {[
                                {Header: "id", accessor: "id", show: false},
                                {
                                    Header: "#", width: 100, id: "ranking", accessor: (row) => {
                                        return this.display_medal(row)
                                    }, className: "center"
                                },
                                {
                                    Header: "Name", id: "name", accessor: (row) => {
                                        return this.display_avatar(row)
                                    }, className: "center"
                                },
                                {Header: "Elo",  width: 150,  id: "elo", accessor: (row) => {return this.render_elo(row)}, className: "center"},
                                {
                                    Header: "Victory",
                                    width: 150,
                                    id: "victory",
                                    accessor: "victory",
                                    className: "center"
                                },
                                {Header: "Defeat", width: 150, id: "defeat", accessor: "defeat", className: "center"},
                                {
                                    Header: "Winrate", width: 125, id: "winrate", accessor: (row) => {
                                        return this.get_winrate(row)
                                    }, className: "center"
                                },
                                {
                                    Header: "Streak", width: 125, id: "streak", accessor: (row) => {
                                        return this.get_streak(row)
                                    }, className: "center"
                                },
                                {
                                    Header: "Match played", width: 175, id: "played", accessor: (row) => {
                                        return this.get_matchplayed(row)
                                    }, className: "center"
                                },
                                {Header: "Region", width: 150, id: "Region", accessor: "region"},
                                {
                                    Header: "Platform", width: 150, id: "Platform", accessor: (row) => {
                                        return this.get_platform(row)
                                    }
                                }
                            ]}
                        pageSize={Leaderboard && Leaderboard.length}
                        defaultSorted={[{id: "elo", desc: false}]}
                        showPagination={false}
                    />
                </MDBCol>
            </MDBRow>);
    }
}

const mapStateToProps = (state) => {
    return {Leaderboard: state.Leaderboard, LeaderboardIsLoading: state.LeaderboardIsLoading}
}

const mapDispatchToProps = (dispatch) => ({
    ...bindActionCreators({
        actionGetLeaderboard
    }, dispatch)
})

export default connect(mapStateToProps, mapDispatchToProps)(LeaderBoardTable);