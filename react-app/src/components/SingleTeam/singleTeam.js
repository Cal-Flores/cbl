import React, { useEffect, useState } from 'react';
import { useDispatch, useSelector } from 'react-redux'
import { useParams } from "react-router-dom";
import { getOneTeam } from '../../store/teams'
import './singleTeam.css';

function SingleTeam() {
    const dispatch = useDispatch()
    const routeParams = useParams();
    const teamId = routeParams.teamId

    let team = useSelector(state => state.teams.Team)
    console.log('heres state', team)

    useEffect(() => {
        dispatch(getOneTeam(teamId))
    }, [dispatch])

    return (
        <div>
            <h2>FIGHTERS</h2>
        </div>
    )
}

export default SingleTeam;
