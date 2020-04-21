import React from 'react';
import Header from "../components/Header/Header";
import LeaderBoardTable from "../components/LeaderBoardTable";

class LeaderboardPage extends React.Component {

    render() {
        return (
            <div>
                <Header/>
                <div style={{marginTop: '100px'}}>
                    Leaderboard
                    <LeaderBoardTable/>
                </div>
            </div>
        );
    }
}

export default LeaderboardPage;