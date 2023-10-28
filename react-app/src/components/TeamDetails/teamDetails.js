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
    if (dualsObj) duals = Object?.values(dualsObj)
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
                        {/* <div>{team?.points} pts</div>
                    <div className='offdef'>
                        <div>Offense: 67</div>
                        <div>Defense: 33</div>
                    </div> */}
                    </div>
                    <button onClick={(e) => history.push(`/teams/${team?.id}`)} className='tdbtn'>FIGHTERS</button>
                </div>
                <div id='tdetailcont' style={{ backgroundImage: "url(" + `${team?.detail_bg}` + ")" }} > </div>
            </div>
            <div id='pointnav'>
                <div>TEAM POINTS: {team?.points}</div>
                <div>OFFENSE: {team?.offense}</div>
                <div>DEFENSE: {team?.defense}</div>
                <div>POINT DIFFRENTIAL -19</div>
            </div>
            <div id='dualcont'>

            </div>
        </div>
    )
}


export default TeamDetails;
