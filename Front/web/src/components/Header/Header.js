import React from 'react';
import { MDBNavbar, MDBNavbarBrand, MDBNavbarNav,  MDBNavItem, MDBNavLink} from 'mdbreact';
import history from "../../history";
import './Header.css'

class Header extends React.Component {

    render() {
        return (
            <div>
                <header>
                        <MDBNavbar color="blue-gradient" dark expand="md" fixed="top" style={{height: "50px"}}>
                            <MDBNavbarBrand href="/home">
                                <strong>DARWIN PROJECT DUEL LEAGUE</strong>
                            </MDBNavbarBrand>
                            <MDBNavbarNav left>
                                <MDBNavItem onClick={() => history.push("/leaderboard")}>
                                    <MDBNavLink to="leaderboard" className="leaderboard-tab">Leaderboard</MDBNavLink>
                                </MDBNavItem>
                            </MDBNavbarNav>
                        </MDBNavbar>
                </header>
            </div>
        );
    }
}

export default Header;