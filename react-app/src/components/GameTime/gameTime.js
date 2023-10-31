// Inside the GameTime component
import React, { useEffect, useState } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { useParams } from 'react-router-dom';
import './gameTime.css';
import GameTimeForm from './GameTimeForm';

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

    //console.log('Dual Info:', dualInfo);
    let squadOne;
    let squadTwo;
    if (dualInfo?.team_1) {
        squadOne = Object.values(dualInfo?.team_1).sort((a, b) => a.weight - b.weight)
        console.log('HERE IS SQUAD 1', squadOne)
    }
    if (dualInfo?.team_2) {
        squadTwo = Object.values(dualInfo?.team_2).sort((a, b) => a.weight - b.weight)
        console.log('HERE IS SQUAD 2', squadTwo)
    }

    let scoreOne = 0;
    let scoreTwo = 0;
    return (
        <div id='gameday'>
            <h1 style={{ textAlign: 'center' }}>Week {dualInfo?.dual?.week} Dual  #{dualInfo?.dual?.id}</h1>
            <div className='gamehead'>
                <div className='scoreteam'>
                    <div>{dualInfo?.dual?.team_1}</div>
                    <div>{scoreOne}</div>
                </div>
                <div className='gamevs'>vs</div>
                <div className='scoreteam'>
                    <div>{scoreTwo}</div>
                    <div>{dualInfo?.dual?.team_2}</div>
                </div>
            </div>
            <div id='squadcont'>
                <div style={{ marginLeft: '15%' }} className='squadOne'>
                    {squadOne?.map(fighter => (
                        <div className='squadcard'>
                            <img style={{ height: '115px', width: '184px', borderBottom: '1px solid gray', }} onError={(e) => { e.target.src = '../../../images/blank.png' }} src={fighter.prof_img} />
                            <div className='sqaudname'>{fighter?.name}</div>
                            <div>{fighter.points} pts</div>
                            <div>{fighter?.wins} - {fighter?.losses}</div>
                        </div>
                    ))}
                </div>
                <div>
                    <GameTimeForm />
                </div>


                <div style={{ marginRight: '15%' }} className='squadOne'>
                    {squadTwo?.map(fighter => (
                        <div className='squadcard'>
                            <img style={{ height: '115px', width: '184px', borderBottom: '1px solid gray', }} onError={(e) => { e.target.src = '../../../images/blank.png' }} src={fighter.prof_img} />
                            <div className='sqaudname'>{fighter?.name}</div>
                            <div>{fighter.points} pts</div>
                            <div>{fighter?.wins} - {fighter?.losses}</div>
                        </div>
                    ))}
                </div>
            </div>
        </div>
    );
}

export default GameTime;
