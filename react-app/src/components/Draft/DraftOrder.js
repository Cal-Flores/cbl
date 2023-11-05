import React, { useEffect, useState } from 'react';
import { useDispatch, useSelector } from 'react-redux'
import './draft.css';
import { useHistory } from 'react-router-dom/cjs/react-router-dom.min';


function DraftOrder() {

    const [picks, setPicks] = useState(null);
    const history = useHistory()

    useEffect(() => {
        const fetchPicks = async () => {
            try {
                const response = await fetch('/api/team/order');
                if (response.ok) {
                    const data = await response.json();
                    setPicks(data.Picks);
                } else {
                    console.error('Failed to fetch draft order');
                }
            } catch (error) {
                console.error('Error fetching data:', error);
            }
        };
        fetchPicks();
    }, []);

    useEffect(() => {
        console.log('HERE\'S THE ORDER', picks);
    }, [picks]);

    const [isChecked, setIsChecked] = useState(() => {
        const savedData = localStorage.getItem('checkbox');
        return savedData ? JSON.parse(savedData) : {};
    });

    const handleCheckboxChange = (id) => {
        setIsChecked((prevState) => ({
            ...prevState,
            [id]: !prevState[id]
        }));
    };

    useEffect(() => {
        localStorage.setItem('checkbox', JSON.stringify(isChecked));
    }, [isChecked]);


    return (
        <div style={{ marginTop: '6%', width: '100%' }}>
            <div onClick={(e) => history.push('/draft')} className='orderimg'>
                <img src='https://upload.wikimedia.org/wikipedia/en/f/f6/2021_NFL_Draft_logo.png' />
            </div>
            {picks &&
                <div className='pickcont'>
                    {picks.map(pick => (
                        <div className='pickcard' key={pick.id}>
                            <img style={{ height: '45px', width: '45px' }} src={pick?.team_info?.logo_img} />
                            <div style={{ cursor: 'pointer' }} onClick={(e) => history.push(`/teams/${pick?.team_info?.id}`)}>{pick?.team}</div>
                            <div>Round {pick?.round}</div>
                            <div>Pick {pick?.pick}</div>
                            <div style={{ cursor: 'pointer' }}>
                                <input
                                    type="checkbox"
                                    checked={isChecked[pick.id]}
                                    onChange={() => handleCheckboxChange(pick.id)}
                                />
                                <label>Pick is in</label>
                            </div>
                        </div>
                    ))}


                </div>
            }
        </div>
    )
}


export default DraftOrder
