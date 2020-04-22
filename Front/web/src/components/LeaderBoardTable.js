import React from 'react';
import {bindActionCreators} from "redux";
import {connect} from "react-redux";
import {actionGetLeaderboard} from '../actions/LeaderboardActions'
import {loaders} from './loaders'
import SimpleTable from "./SimpleTable";
import './Table.css'

class LeaderBoardTable extends React.Component {

    constructor(props) {
        super(props);
        this.state = {
            rows: [],
            column: [{

            }]
        }
    }

    componentDidMount() {
        this.props.actionGetLeaderboard()
    }

    componentDidUpdate(prevProps, prevState) {
        const {Leaderboard} = this.props
        if (Leaderboard && Leaderboard !== prevProps.Leaderboard) {
        //    this.parseData()
        }
    }

    parseData = () => {
        let { Leaderboard } = this.props
        let newData = []

        if (!Leaderboard || !Leaderboard.length) return ''
        console.log(Leaderboard)
        Leaderboard.forEach((player) => {
            const { avatar_url } = {...player}
            const tempRow = {
                avatar: <img src={avatar_url} alt="playername" width="50px" height="50px"/>,
                ...player,
            }
            newData.push(tempRow)
        })
        this.setState({rows: newData})
    }

    display_avatar(player) {
        return <span className="profile_col" >
            <img className="player_avatar" src={player.avatar_url} alt="avatar"/>
            {player.user_name}
        </span>
    }



    render() {
        const { Leaderboard, LeaderboardIsLoading }= this.props

        if (LeaderboardIsLoading) return loaders[Math.floor(Math.random() * loaders.length)]
        console.log(Leaderboard)
        return (<SimpleTable
            name="leaderboard_table"
            filterable
            data={Leaderboard}
            columns=
                {[
                    { Header: "id", accessor: "id", show: false },
                    { Header: "#", width: 100, id: "ranking", accessor: "ranking" },
                    { Header: "Name", width: 600, id: "name", accessor: (row) => { return this.display_avatar(row) }, className: "center" },
                    { Header: "Elo", id: "elo", accessor: "elo" },
                    { Header: "Region", id: "Region", accessor: "region" }
                ]}
            pageSize={Leaderboard && Leaderboard.length}
            defaultSorted={[{ id: "elo", desc: false }]}
            showPagination/>);
    }
}

/*
                name="leaderboard_table"
                filterable
                data={rows}
                columns=
                    {[
                        { Header: "id", accessor: "id", show: false },
                        { Header: "Name",id: "name", accessor: (row) => { return this.display_avatar(row) }, width: 70, className: "center" },
                        { Header: "Elo",id: "elo", accessor: "elo" },
                        { Header: "Region",id: "Region", accessor: "region" }
                    ]}
                pageSize={rows && rows.length}
                defaultSorted={[{ id: "elo", desc: false }]}
                showPagination
*/
const mapStateToProps = (state) => {
    return { Leaderboard: state.Leaderboard, LeaderboardIsLoading: state.LeaderboardIsLoading}
}

const mapDispatchToProps = (dispatch) => ({
    ...bindActionCreators({
        actionGetLeaderboard
    }, dispatch)
})

export default connect(mapStateToProps, mapDispatchToProps)(LeaderBoardTable);