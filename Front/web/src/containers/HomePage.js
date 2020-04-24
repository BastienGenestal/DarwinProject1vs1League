import React, { Component } from 'react';
import bgPic from "../data/image/backgroundImage.jpg";
import discord from "../data/image/logos/JPG/discord.png";
import { MDBMask, MDBView, MDBBtn } from 'mdbreact';
import Header from "../components/Header/Header";

const discord_link = "https://discord.gg/axhYkm4"

class HomePage extends Component {

    render() {

    return (
        <div>
            <Header />
          <MDBView src={bgPic}>
              <MDBMask overlay="black-light" className="flex-center flex-column text-white text-center">
                  <h2 className="intro-text">Get into Darwin Duel League</h2>
                  <MDBBtn outline color="light-blue" href={discord_link} target="_blank" size="lg" style={{display:'flex', padding: 0}}>
                      <div className="discordButtonContent">
                          <img alt="discord" src={discord} width='50px'/>
                          <div style={{display: "table-cell", paddingLeft: "5px", margin: "auto", verticalAlign: 'middle'}} >Join Discord</div>
                      </div>
                  </MDBBtn>
              </MDBMask>
          </MDBView>
        </div>
    );
  }
}

export default HomePage;
