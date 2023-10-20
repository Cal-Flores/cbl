import React, { useEffect, useState } from 'react';
import { useDispatch, useSelector } from 'react-redux'
import './allTeams.css';
import { getAllTeams } from '../../store/teams';

function AllTeams() {
    const dispatch = useDispatch()
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

    const changeConf = () => {
        if (nfc_display == true) setnfc_display(false)
        else setnfc_display(true)
    }

    if (nfc_display == true) {
        contentDiv = (
            <div>
                <h3>NFC North</h3>
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
                                    <button class='teamBtn'>Players</button>
                                    <button class='teamBtn'>Stats</button>
                                </div>
                            </div>
                        </div>
                    ))}
                </div>

                <h3>NFC East</h3>
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
                                    <button class='teamBtn'>Players</button>
                                    <button class='teamBtn'>Stats</button>
                                </div>
                            </div>
                        </div>
                    ))}
                </div>

                <h3>NFC South</h3>
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
                                    <button class='teamBtn'>Players</button>
                                    <button class='teamBtn'>Stats</button>
                                </div>
                            </div>
                        </div>
                    ))}
                </div>

                <h3>NFC West</h3>
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
                                    <button class='teamBtn'>Players</button>
                                    <button class='teamBtn'>Stats</button>
                                </div>
                            </div>
                        </div>
                    ))}
                </div>
            </div>
        )
    } else {
        contentDiv = (

            <div>
                <h3>AFC North</h3>
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
                                    <button class='teamBtn'>Players</button>
                                    <button class='teamBtn'>Stats</button>
                                </div>
                            </div>
                        </div>
                    ))}
                </div>

                <h3>AFC East</h3>
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
                                    <button class='teamBtn'>Players</button>
                                    <button class='teamBtn'>Stats</button>
                                </div>
                            </div>
                        </div>
                    ))}
                </div>

                <h3>AFC South</h3>
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
                                    <button class='teamBtn'>Players</button>
                                    <button class='teamBtn'>Stats</button>
                                </div>
                            </div>
                        </div>
                    ))}
                </div>

                <h3>AFC West</h3>
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
                                    <button class='teamBtn'>Players</button>
                                    <button class='teamBtn'>Stats</button>
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
        <div>
            <button onClick={changeConf}>AFC</button> <button onClick={changeConf}>NFC</button>

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
