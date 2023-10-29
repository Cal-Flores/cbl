import React, { useEffect, useState } from 'react';
import { useDispatch, useSelector } from 'react-redux'
import { useParams, useHistory } from "react-router-dom";
import { getOneTeam, teamDuals } from '../../store/teams';
import './teamDetails.css';


function TeamDetails() {
    const dispatch = useDispatch();
    const history = useHistory();
    const routeParams = useParams();
    const teamId = routeParams?.teamId

    useEffect(() => {
        dispatch(getOneTeam(teamId))
    }, [dispatch])

    let team = useSelector(state => state?.teams?.Team)
    let dualsObj = useSelector(state => state?.teams?.Team?.Duals)

    let duals;
    let diff;
    if (dualsObj) {
        duals = Object?.values(dualsObj)
        let pts = 0;
        let opts = 0;
        duals.map(dual => {
            if (dual.winner == team.name) {
                pts += dual.winner_score;
                opts += dual.loser_score;

            }
            else {
                pts += dual.loser_score;
                opts += dual.winner_score;
            }
            console.log('pts', dual.winner_score)
            console.log('opts', dual.loser_score)
        })
        diff = pts - opts
    }
    console.log('all duals', team)

    //style={{ backgroundImage: "url(" + `${team?.bg}` + ")", border: `5px solid ${team?.border}` }}
    return (
        <div>
            <div id='dtcont'>
                <div className='statdt'>
                    <h1 className='tdname'>{team?.name}</h1>
                    <div className='tdconf'>
                        <div>{team?.conf} {team?.divison}</div>
                        <div>Last Season: {team?.win}-{team?.loss} WILDCARD</div>
                    </div>
                    <div className='tdrec'>
                        <div className='tdrecnum'>{team?.win} - {team?.loss}</div>
                    </div>
                    <button onClick={(e) => history.push(`/teams/${team?.id}`)} className='tdbtn'>FIGHTERS</button>
                </div>
                <div id='tdetailcont' style={{ backgroundImage: "url(" + `${team?.detail_bg}` + ")" }} > </div>
            </div>
            <div id='pointnav'>
                <div>TEAM POINTS: {team?.points}</div>
                <div>OFFENSE: {team?.offense}</div>
                <div>DEFENSE: {team?.defense}</div>
                <div>POINT DIFFRENTIAL: {diff}</div>
            </div>
            <div id='dualcont'>
                <div className="grid-header">
                    <div style={{ marginLeft: '8%' }}>Week</div>
                    <div style={{ paddingLeft: '10px' }}>Game</div>
                    <div>{team?.name.split(" ")[team?.name.split(" ").length - 1]}</div>
                    <div>Opponent</div>
                    <div>Outcome</div>
                </div>

                {duals?.map(dual => {
                    if (dual?.winner === team?.name) {
                        return (
                            <div key={dual.id} className="grid-row">
                                <div style={{ marginLeft: '8%' }}>Week {dual?.week}</div>
                                <div style={{ paddingLeft: '10px' }}>vs {dual?.loser}</div>
                                <div style={{ paddingLeft: '20px', color: 'rgb(63, 63, 63)', fontWeight: 'bold' }}>{dual?.winner_score}</div>
                                <div style={{ paddingLeft: '21px' }}>{dual?.loser_score}</div>
                                <div style={{ color: 'green', paddingLeft: '20px' }}>W</div>
                            </div>
                        );
                    } else {
                        return (
                            <div key={dual.id} className="grid-row">
                                <div style={{ marginLeft: '8%' }}>Week {dual?.week}</div>
                                <div style={{ paddingLeft: '10px' }}>vs {dual?.winner}</div>
                                <div style={{ paddingLeft: '20px' }}>{dual?.loser_score}</div>
                                <div style={{ paddingLeft: '20px', color: 'rgb(63, 63, 63)', fontWeight: 'bold' }}>{dual?.winner_score}</div>
                                <div style={{ color: 'red', paddingLeft: '23px' }}>L</div>
                            </div>
                        )
                    }
                })}
            </div>
        </div>
    )
}


export default TeamDetails;
