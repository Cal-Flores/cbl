import React, { useEffect } from 'react';
import { useDispatch, useSelector } from 'react-redux'
import './allTeams.css';
import { getAllTeams } from '../../store/teams';


function AllTeams() {
    const dispatch = useDispatch()
    let teams = useSelector(state => state.teams.All_Teams)
    console.log('Amy smells', teams)

    useEffect(() => {
        dispatch(getAllTeams())
    }, [dispatch])


    return (
        <div>
            <h1>All Teams</h1>
            {teams?.map(team => (
                <h3 key={team.id}> {team.name}</h3>
            ))}

        </div>
    )
}


export default AllTeams;
