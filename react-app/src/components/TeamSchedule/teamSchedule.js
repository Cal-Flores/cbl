import React, { useEffect, useState } from 'react';
import { useDispatch, useSelector } from 'react-redux'
import { useParams, useHistory } from "react-router-dom";
import './teamSchedule.css';


function TeamSchedule() {
    const dispatch = useDispatch();
    const history = useHistory();
    const routeParams = useParams();
    const teamId = routeParams?.teamId
    const [teamSchedule, setTeamSchedule] = useState([]);


    useEffect(() => {
        const fetchData = async () => {
            try {
                const response = await fetch(`/api/team_routes/schedule/${teamId}`);
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }

                const data = await response.json();
                setTeamSchedule(data.Duals);
            } catch (error) {
                console.error('Error fetching team schedule:', error);
                // Handle error as needed
            }
        };

        if (teamId) {
            fetchData();
        }
    }, [teamId]);

    return (
        <div style={{ marginTop: '5%' }}>
            <div>TEAMS SCHEDULE</div>
            <ul>
                {Object.values(teamSchedule).map((dual) => (
                    <li key={dual.id}>{/* Render dual information here */}</li>
                ))}
            </ul>

        </div>
    )
}

export default TeamSchedule
