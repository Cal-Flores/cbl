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
    let dualsObj = useSelector(state => state?.teams?.Team?.Duals) // Access duals from the state
    let duals;
    if (dualsObj) duals = Object?.values(dualsObj)
    console.log('all duals', duals)

    return (
        <div style={{ marginTop: '200px' }}>
           
        </div>
    )
}


export default TeamDetails;
