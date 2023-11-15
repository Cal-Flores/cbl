import React, { useEffect, useState } from 'react';
import { useDispatch, useSelector } from 'react-redux'
import { useParams, useHistory } from "react-router-dom";
import './teamSchedule.css';


function TeamSchedule() {
    const dispatch = useDispatch();
    const history = useHistory();
    const routeParams = useParams();
    const teamId = routeParams?.teamId

    return (
        <div style={{ marginTop: '5%' }}>
            <div>TEAMS SCHEDULE</div>
        </div>
    )
}

export default TeamSchedule
