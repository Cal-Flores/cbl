import React, { useEffect, useState } from 'react';
import { useDispatch, useSelector } from 'react-redux'

function Playoffs() {
    const [playoffData, setPlayoffData] = useState(null);

    useEffect(() => {
        const fetchPlayoffs = async () => {
            try {
                const response = await fetch('/api/team/playoffs');
                if (response.ok) {
                    const data = await response.json();
                    setPlayoffData(data);
                    console.log('Fetched playoff data:', data);
                } else {
                    console.error('Failed to fetch playoff data');
                }
            } catch (error) {
                console.error('Error fetching data:', error);
            }
        };
        fetchPlayoffs();
    }, []);

    return (
        <div style={{ marginTop: '100px' }}>
            <h1>PLAYOFF PICTURE</h1>
            {playoffData &&
                <div>
                    <div>
                        {playoffData?.afc_leaders?.map(team => (
                            <div>
                                <div>{team.name}</div>
                                <img style={{ height: '55px', width: '55px' }} src={team?.logo_img} />
                            </div>
                        ))}
                    </div>
                    <div></div>
                </div>
            }
        </div>
    )
}

export default Playoffs
