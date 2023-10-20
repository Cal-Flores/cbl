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
                <div style={{
                    width: '400px',
                    height: '150px',
                    backgroundImage: "url(" + `${team.background_img}` + ")",
                    backgroundPosition: 'center',
                    backgroundSize: 'cover',
                    backgroundRepeat: 'no-repeat'
                }} key={team.id}>
                    <h3> {team.name}</h3>
                    <img src={team?.logo_img} style={{ width: '140px', height: '140px' }} />
                </div>
            ))}

        </div>
    )
}


export default AllTeams;
