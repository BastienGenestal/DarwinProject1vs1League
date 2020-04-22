import React from 'react';
import Header from "../components/Header/Header";
import LeaderBoardTable from "../components/LeaderBoardTable";
import './Leaderboard.css'

class LeaderboardPage extends React.Component {

    render() {
        return (
            <div>
                <Header/>
                <div className="leaderboard-page">
                    <div className="module-border-wrap">
                        <h2 className="leaderboard-title">
                            Leaderboard
                        </h2>
                    </div>
                    <div className="leaderboard_container">
                        <LeaderBoardTable/>
                    </div>
                </div>
            </div>
        );
    }
}

export default LeaderboardPage;