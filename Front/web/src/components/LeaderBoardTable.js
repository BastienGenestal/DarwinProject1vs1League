import React from 'react';
import {bindActionCreators} from "redux";
import {connect} from "react-redux";
import {actionGetLeaderboard} from '../actions/LeaderboardActions'
import {loaders} from './loaders'
import SimpleTable from "./SimpleTable";
import './Table.css'
import gold from '../data/image/medals/1.png'
import silver from '../data/image/medals/2.png'
import bronze from '../data/image/medals/3.png'


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
        return <span className="profile_col" >
            <img className="player_avatar" src={player.avatar_url} alt="avatar"/>
            {player.user_name}
        </span>
    }

    render() {
        const { Leaderboard, LeaderboardIsLoading } = this.props

        if (LeaderboardIsLoading) return loaders[Math.floor(Math.random() * loaders.length)]
        return (<SimpleTable
            name="leaderboard_table"
            filterable
            data={Leaderboard}
            columns=
                {[
                    { Header: "id", accessor: "id", show: false },
                    { Header: "#", width: 100, id: "ranking", accessor: (row) => { return this.display_medal(row) }, className: "center"},
                    { Header: "Name", width: 600, id: "name", accessor: (row) => { return this.display_avatar(row) }, className: "center" },
                    //{ Header: "Elo", id: "elo", accessor: (row) => { return this.display_elo(row) }, className: "center" },
                    { Header: "Elo", id: "elo", accessor: "elo", className: "center" },
                    { Header: "Region", id: "Region", accessor: "region" }
                ]}
            pageSize={Leaderboard && Leaderboard.length}
            defaultSorted={[{ id: "elo", desc: false }]}
            showPagination={false}
        />);
    }
}

const mapStateToProps = (state) => {
    return { Leaderboard: state.Leaderboard, LeaderboardIsLoading: state.LeaderboardIsLoading}
}

const mapDispatchToProps = (dispatch) => ({
    ...bindActionCreators({
        actionGetLeaderboard
    }, dispatch)
})

export default connect(mapStateToProps, mapDispatchToProps)(LeaderBoardTable);