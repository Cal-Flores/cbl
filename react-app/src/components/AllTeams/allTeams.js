import React, { useEffect, useState } from 'react';
import { useDispatch, useSelector } from 'react-redux'
import './allTeams.css';
import { getAllTeams } from '../../store/teams';
import { Link, Redirect, useHistory, useParams } from 'react-router-dom'

function AllTeams() {
    const dispatch = useDispatch()
    const history = useHistory()
    let teams = useSelector(state => state.teams.All_Teams)


    const [nfc_display, setnfc_display] = useState(true);

    let nfcNorth = teams?.filter(team => team.conf == 'NFC' && team.divison == 'North')
    let nfcEast = teams?.filter(team => team.conf == 'NFC' && team.divison == 'East')
    let nfcSouth = teams?.filter(team => team.conf == 'NFC' && team.divison == 'South')
    let nfcWest = teams?.filter(team => team.conf == 'NFC' && team.divison == 'West')

    let afcNorth = teams?.filter(team => team.conf == 'AFC' && team.divison == 'North')
    let afcEast = teams?.filter(team => team.conf == 'AFC' && team.divison == 'East')
    let afcSouth = teams?.filter(team => team.conf == 'AFC' && team.divison == 'South')
    let afcWest = teams?.filter(team => team.conf == 'AFC' && team.divison == 'West')
    let contentDiv;

    const changeConfNfc = () => {
        setnfc_display(false)
    }
    const changeConfAfc = () => {
        setnfc_display(true)
    }

    if (nfc_display == true) {
        contentDiv = (
            <div>
                <h4>NFC North</h4>
                <div id='allTeamCont'>
                    {nfcNorth?.map(team => (
                        <div id='teamCard' style={{ backgroundImage: "url(" + `${team.background_img}` + ")" }} key={team.id}>
                            <div>
                                <img src={team?.logo_img} style={{ width: '160px', height: '160px' }} />
                            </div>
                            <div class='teamInfo'>
                                <div>
                                    <h3 class='teamName'> {team.name}</h3>
                                </div>
                                <div>
                                    <button onClick={(e) => history.push(`/teams/${team.id}`)} class='teamBtn'>Fighters</button>
                                    <button onClick={(e) => history.push(`/teams/stats/${team.id}`)} class='teamBtn'>Stats</button>
                                </div>
                            </div>
                        </div>
                    ))}
                </div>

                <h4>NFC East</h4>
                <div id='allTeamCont'>
                    {nfcEast?.map(team => (
                        <div id='teamCard' style={{ backgroundImage: "url(" + `${team.background_img}` + ")" }} key={team.id}>
                            <div>
                                <img src={team?.logo_img} style={{ width: '160px', height: '160px' }} />
                            </div>
                            <div class='teamInfo'>
                                <div>
                                    <h3 class='teamName'> {team.name}</h3>
                                </div>
                                <div>
                                    <button onClick={(e) => history.push(`/teams/${team.id}`)} class='teamBtn'>Players</button>
                                    <button onClick={(e) => history.push(`/teams/stats/${team.id}`)} class='teamBtn'>Stats</button>
                                </div>
                            </div>
                        </div>
                    ))}
                </div>

                <h4>NFC South</h4>
                <div id='allTeamCont'>
                    {nfcSouth?.map(team => (
                        <div id='teamCard' style={{ backgroundImage: "url(" + `${team.background_img}` + ")" }} key={team.id}>
                            <div>
                                <img src={team?.logo_img} style={{ width: '160px', height: '160px' }} />
                            </div>
                            <div class='teamInfo'>
                                <div>
                                    <h3 class='teamName'> {team.name}</h3>
                                </div>
                                <div>
                                    <button onClick={(e) => history.push(`/teams/${team.id}`)} class='teamBtn'>Players</button>
                                    <button onClick={(e) => history.push(`/teams/stats/${team.id}`)} class='teamBtn'>Stats</button>
                                </div>
                            </div>
                        </div>
                    ))}
                </div>

                <h4>NFC West</h4>
                <div id='allTeamCont'>
                    {nfcWest?.map(team => (
                        <div id='teamCard' style={{ backgroundImage: "url(" + `${team.background_img}` + ")" }} key={team.id}>
                            <div>
                                <img src={team?.logo_img} style={{ width: '160px', height: '160px' }} />
                            </div>
                            <div class='teamInfo'>
                                <div>
                                    <h3 class='teamName'> {team.name}</h3>
                                </div>
                                <div>
                                    <button onClick={(e) => history.push(`/teams/${team.id}`)} class='teamBtn'>Players</button>
                                    <button onClick={(e) => history.push(`/teams/stats/${team.id}`)} class='teamBtn'>Stats</button>
                                </div>
                            </div>
                        </div>
                    ))}
                </div>
            </div >
        )
    } else {
        contentDiv = (

            <div>
                <h4>AFC North</h4>
                <div id='allTeamCont'>
                    {afcNorth?.map(team => (
                        <div id='teamCard' style={{ backgroundImage: "url(" + `${team.background_img}` + ")" }} key={team.id}>
                            <div>
                                <img src={team?.logo_img} style={{ width: '160px', height: '160px' }} />
                            </div>
                            <div class='teamInfo'>
                                <div>
                                    <h3 class='teamName'> {team.name}</h3>
                                </div>
                                <div>
                                    <button onClick={(e) => history.push(`/teams/${team.id}`)} class='teamBtn'>Players</button>
                                    <button onClick={(e) => history.push(`/teams/stats/${team.id}`)} class='teamBtn'>Stats</button>
                                </div>
                            </div>
                        </div>
                    ))}
                </div>

                <h4>AFC East</h4>
                <div id='allTeamCont'>
                    {afcEast?.map(team => (
                        <div id='teamCard' style={{ backgroundImage: "url(" + `${team.background_img}` + ")" }} key={team.id}>
                            <div>
                                <img src={team?.logo_img} style={{ width: '160px', height: '160px' }} />
                            </div>
                            <div class='teamInfo'>
                                <div>
                                    <h3 class='teamName'> {team.name}</h3>
                                </div>
                                <div>
                                    <button onClick={(e) => history.push(`/teams/${team.id}`)} class='teamBtn'>Players</button>
                                    <button onClick={(e) => history.push(`/teams/stats/${team.id}`)} class='teamBtn'>Stats</button>
                                </div>
                            </div>
                        </div>
                    ))}
                </div>

                <h4>AFC South</h4>
                <div id='allTeamCont'>
                    {afcSouth?.map(team => (
                        <div id='teamCard' style={{ backgroundImage: "url(" + `${team.background_img}` + ")" }} key={team.id}>
                            <div>
                                <img src={team?.logo_img} style={{ width: '160px', height: '160px' }} />
                            </div>
                            <div class='teamInfo'>
                                <div>
                                    <h3 class='teamName'> {team.name}</h3>
                                </div>
                                <div>
                                    <button onClick={(e) => history.push(`/teams/${team.id}`)} class='teamBtn'>Players</button>
                                    <button onClick={(e) => history.push(`/teams/stats/${team.id}`)} class='teamBtn'>Stats</button>
                                </div>
                            </div>
                        </div>
                    ))}
                </div>

                <h4>AFC West</h4>
                <div id='allTeamCont'>
                    {afcWest?.map(team => (
                        <div id='teamCard' style={{ backgroundImage: "url(" + `${team.background_img}` + ")" }} key={team.id}>
                            <div>
                                <img src={team?.logo_img} style={{ width: '160px', height: '160px' }} />
                            </div>
                            <div class='teamInfo'>
                                <div>
                                    <h3 class='teamName'> {team.name}</h3>
                                </div>
                                <div>
                                    <button onClick={(e) => history.push(`/teams/${team.id}`)} class='teamBtn'>Players</button>
                                    <button onClick={(e) => history.push(`/teams/stats/${team.id}`)} class='teamBtn'>Stats</button>
                                </div>
                            </div>
                        </div>
                    ))}
                </div>
            </div>
        )
    }




    useEffect(() => {
        dispatch(getAllTeams())
    }, [dispatch])


    return (
        <div id='teamcont'>
            <div class='conflinks'>
                <button class='displayBtn' onClick={changeConfAfc}><img style={{ width: '23px', height: '23px', marginRight: '10px' }} src='https://upload.wikimedia.org/wikipedia/commons/thumb/6/6f/National_Football_Conference_logo.svg/1200px-National_Football_Conference_logo.svg.png' />NFC Teams</button>
                <button class='displayBtn' onClick={changeConfNfc}><img style={{ width: '23px', height: '23px', marginRight: '10px' }} src='https://upload.wikimedia.org/wikipedia/commons/thumb/7/7a/American_Football_Conference_logo.svg/2560px-American_Football_Conference_logo.svg.png' />AFC Teams</button>
            </div>

            {nfc_display ? (
                <div>
                    {contentDiv}
                </div>
            ) : (
                <div>
                    {contentDiv}
                </div>
            )}
        </div>
    );
};



export default AllTeams;
