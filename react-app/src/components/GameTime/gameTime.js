// Inside the GameTime component
import React, { useEffect, useState } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { useParams, useHistory, } from 'react-router-dom';
import './gameTime.css';
import GameTimeForm from './GameTimeForm';

function GameTime() {
    const dispatch = useDispatch();
    const history = useHistory()
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

    console.log('Dual Info:', dualInfo?.dual?.team_1);
    let squadOne;
    let squadTwo;
    if (dualInfo?.team_1) {
        squadOne = Object.values(dualInfo?.team_1).sort((a, b) => a.weight - b.weight)
        console.log('HERE IS SQUAD DUALS', dualInfo)
    }
    if (dualInfo?.team_2) {
        squadTwo = Object.values(dualInfo?.team_2).sort((a, b) => a.weight - b.weight)
    }

    const [scoreOne, setScoreOne] = useState(0); // Using the useState hook
    const [scoreTwo, setScoreTwo] = useState(0); // Using the useState hook

    const scoreOnePlus = () => {
        setScoreOne(scoreOne + 1);
    };

    const scoreOneMinus = () => {
        setScoreOne(scoreOne - 1);
    };
    const scoreTwoPlus = () => {
        setScoreTwo(scoreTwo + 1);
    };

    const scoreTwoMinus = () => {
        setScoreTwo(scoreTwo - 1);
    };
    return (
        <div id='gameday'>
            <h1 style={{ textAlign: 'center' }}>Week {dualInfo?.dual?.week} Dual  #{dualInfo?.dual?.id}</h1>
            <div className='gamehead'>
                <div className='scoreteam'>
                    <div className='squadbtn'>
                        <button className='addbtn' onClick={scoreOnePlus}>+</button>
                        <button className='subbtn' onClick={scoreOneMinus}>-</button>
                    </div>
                    <div>{dualInfo?.dual?.team_1}</div>
                    <div>{scoreOne}</div>
                </div>
                <div className='gamevs'>vs</div>
                <div className='scoreteam'>
                    <div>{scoreTwo}</div>
                    <div>{dualInfo?.dual?.team_2}</div>
                    <div className='squadbtn'>
                        <button className='addbtn' onClick={scoreTwoPlus}>+</button>
                        <button className='subbtn' onClick={scoreTwoMinus}>-</button>
                    </div>
                </div>
            </div>
            <div id='squadcont'>
                <div style={{ marginLeft: '15%' }} className='squadOne'>
                    {squadOne?.map(fighter => (
                        <div className='squadcard'>
                            <img onClick={(e) => history.push(`/fighter/${fighter?.id}`)} style={{ height: '115px', width: '184px', borderBottom: '1px solid gray', }} onError={(e) => { e.target.src = '../../../images/blank.png' }} src={fighter.prof_img} />
                            <div className='sqaudname'>{fighter?.name}</div>
                            <div>{fighter.points} pts</div>
                            <div>{fighter?.wins} - {fighter?.losses}</div>
                        </div>
                    ))}
                </div>
                <div>
                    <GameTimeForm scoreOne={scoreOne} scoreTwo={scoreTwo} />
                </div>


                <div style={{ marginRight: '15%' }} className='squadOne'>
                    {squadTwo?.map(fighter => (
                        <button onClick={(e) => history.push(`/fighter/${fighter?.id}`)} className='squadcard'>
                            <img style={{ height: '115px', width: '184px', borderBottom: '1px solid gray', }} onError={(e) => { e.target.src = '../../../images/blank.png' }} src={fighter.prof_img} />
                            <div className='sqaudname'>{fighter?.name}</div>
                            <div>{fighter.points} pts</div>
                            <div>{fighter?.wins} - {fighter?.losses}</div>
                        </button>
                    ))}
                </div>
            </div>
        </div>
    );
}

export default GameTime;
