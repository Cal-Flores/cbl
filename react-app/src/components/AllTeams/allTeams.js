import React, { useEffect } from 'react';
import { useDispatch, useSelector } from 'react-redux'
import './allTeams.css';
import { getAllTeams } from '../../store/teams';


function AllTeams() {
    const dispatch = useDispatch()

    useEffect(() => {
        dispatch(getAllTeams())
    }, [dispatch])


    return (
        <div>
            <h1>All Teams</h1>
        </div>
    )
}


export default AllTeams;
