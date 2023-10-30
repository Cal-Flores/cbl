// Inside the GameTime component
import React, { useEffect, useState } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { useParams } from 'react-router-dom';

function GameTime() {
    const dispatch = useDispatch();
    const [dualInfo, setDualInfo] = useState(null);
    const { id } = useParams();

    useEffect(() => {
        const fetchData = async () => {
            try {
                const response = await fetch(`/api/team/game/${id}`);
                if (!response.ok) {
                    throw new Error('Network response was not ok.');
                }
                const data = await response.json();
                setDualInfo(data.Dual_Stats);
            } catch (error) {
                console.error('Error fetching data:', error);
            }
        };
        fetchData();
    }, [id]);

    console.log('Dual Info:', dualInfo);

    return (
        <div style={{ marginTop: '6%' }}>
            <h1>GAME DAY</h1>
            {/* Render the retrieved data in your component */}
        </div>
    );
}

export default GameTime;
