import React, { useEffect, useState } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { Link, Redirect, useHistory, useParams } from 'react-router-dom'
import './schedule.css';
import { getAllSchedule, getSchedule } from '../../store/teams';

function Schedule() {
    const dispatch = useDispatch();
    const history = useHistory()
    const [week, setWeek] = useState('All');
    const [headerValue, setHeaderValue] = useState('');
    const [scores, setScores] = useState(null);
    const [scoresOBJ, setScoresOBJ] = useState(null);
    const scheduleWeek = useSelector(state => state.teams?.Schedule);
    //console.log('HERES THE DUALS THIS WEEK', scheduleWeek)

    const fetchScores = async () => {
        try {
            const response = await fetch('/api/team/scores');
            if (!response.ok) {
                throw new Error(`HTTP error! Status: ${response.status}`);
            }
            const data = await response.json();
            setScores(data.Scores);
        } catch (error) {
            console.error('Error fetching scores:', error);
        }
    };


    useEffect(() => {
        dispatch(getAllSchedule());
        fetchScores();
    }, [dispatch]);

    let sArr
    if (scheduleWeek) {
        sArr = Object.values(scheduleWeek)
        console.log('night showwww', sArr)
    }

    const handleSearch = (e) => {
        const selectedWeek = parseInt(e.target.value.replace('Week ', ''));
        console.log('youare a number', selectedWeek)
        setWeek(e.target.value);
        setHeaderValue(selectedWeek);
        dispatch(getSchedule(selectedWeek));
    };

    const weekOptions = [];
    for (let i = 1; i <= 16; i++) {
        weekOptions.push(
            <option key={i} value={i}>
                Week {i}
            </option>
        );
    }

    useEffect(() => {
        if (scores !== null) {
            setScoresOBJ(JSON.stringify(scores));
            console.log('YEEEA', scoresOBJ)
        }
    }, [scores]);

    const scoresObject = JSON.parse(scoresOBJ);

    return (

        <div style={{ color: 'rgb(85, 83, 83)', marginTop: '6%', marginBottom: '6%' }}>
            <div className='nflsche'>
                <div>NFL Schedule</div>
                <div style={{ fontSize: '35px' }}>2023 - Week {headerValue}</div>
                <select className='weekselect' style={{ height: '35px', width: '150px' }} value={week} onChange={handleSearch}>
                    <option value="All">All</option>
                    {weekOptions}
                </select>
            </div>
            <div className='scontcont'>
                <div>
                    {sArr?.map((dual, index) => (
                        <div id='sdualcont' key={dual.id}>

                            {dual.completed == false &&
                                <div className='dualdiv'>
                                    <div style={{ color: 'rgb(40, 83, 129)' }}>In Progress</div>
                                    <div>({dual?.team_1?.curr_wins} - {dual?.team_1?.curr_loss})</div>
                                    <div onClick={(e) => history.push(`/teams/stats/${dual?.team_1?.id}`)} className='sname'>{dual?.team_1?.name}</div>
                                    <img style={{ height: '45px', width: '45px' }} src={dual?.team_1?.logo_img} />
                                    <div>VS</div>
                                    <img style={{ height: '45px', width: '45px' }} src={dual?.team_2?.logo_img} />
                                    <div onClick={(e) => history.push(`/teams/stats/${dual?.team_2?.id}`)} className='sname'>{dual?.team_2?.name}</div>
                                    <div>({dual?.team_2?.curr_wins} - {dual?.team_2?.curr_loss})</div>


                                    <button
                                        onClick={() => history.push(`/game/${dual.id}`)}
                                        style={{
                                            fontWeight: 'bold',
                                            cursor: 'pointer',
                                            backgroundColor: 'white',
                                            height: '30px',
                                            width: '60px',
                                            border: 'none',
                                            color: 'rgb(40, 83, 129)',
                                        }}
                                    >
                                        START
                                    </button>

                                </div>
                            }
                            {dual.completed == true &&
                                <div>
                                    {dual?.team_1.name == scoresObject[`${index + 1}`]?.winner ? (
                                        <div className='dualdiv2'>
                                            <div style={{ color: 'green' }}>Complete</div>
                                            <div>({dual?.team_1?.curr_wins} - {dual?.team_1?.curr_loss})</div>
                                            <div style={{ fontWeight: 'bolder' }} onClick={(e) => history.push(`/teams/stats/${dual?.team_1?.id}`)} className='sname'>{scoresObject[`${index + 1}`]?.winner}</div>
                                            <img style={{ height: '45px', width: '45px' }} src={dual?.team_1?.logo_img} />
                                            <div className='scoree' style={{ fontWeight: 'bolder' }}>{scoresObject[`${index + 1}`]?.winner_score}</div>
                                            <div>VS</div>
                                            <div className='scoree'>{scoresObject[`${index + 1}`]?.loser_score}</div>
                                            <img style={{ height: '45px', width: '45px' }} src={dual?.team_2?.logo_img} />
                                            <div onClick={(e) => history.push(`/teams/stats/${dual?.team_2?.id}`)} className='sname'>{scoresObject[`${index + 1}`]?.loser}</div>
                                            <div>({dual?.team_2?.curr_wins} - {dual?.team_2?.curr_loss})</div>
                                            <div>FINAL</div>
                                        </div>
                                    ) : (
                                        <div className='dualdiv2'>
                                            <div style={{ color: 'green' }}>Complete</div>
                                            <div>({dual?.team_1?.curr_wins} - {dual?.team_1?.curr_loss})</div>
                                            <div onClick={(e) => history.push(`/teams/stats/${dual?.team_1?.id}`)} className='sname'>{scoresObject[`${index + 1}`]?.loser}</div>
                                            <img style={{ height: '45px', width: '45px' }} src={dual?.team_1?.logo_img} />
                                            <div className='scoree'>{scoresObject[`${index + 1}`]?.loser_score}</div>

                                            <div>VS</div>

                                            <div className='scoree' style={{ fontWeight: 'bolder' }}>{scoresObject[`${index + 1}`]?.winner_score}</div>
                                            <img style={{ height: '45px', width: '45px' }} src={dual?.team_2?.logo_img} />
                                            <div style={{ fontWeight: 'bolder' }} onClick={(e) => history.push(`/teams/stats/${dual?.team_2?.id}`)} className='sname'>{scoresObject[`${index + 1}`]?.winner}</div>
                                            <div>({dual?.team_2?.curr_wins} - {dual?.team_2?.curr_loss})</div>
                                            <div>FINAL</div>
                                        </div>
                                    )
                                    }

                                </div>
                            }
                        </div>
                    ))}
                </div>
            </div>
        </div>

    );
}

export default Schedule;









{/* <div id='sdualcont'>
    <div className='dualdiv'>
        <div>In Progress</div>
        <div>({dual?.team_1?.win} - {dual?.team_1?.loss})</div>
        <div>{dual?.team_1?.name}</div>
        <img style={{ height: '40px', width: '40px' }} src={dual?.team_1?.logo_img} />
        <div>VS</div>
        <img style={{ height: '40px', width: '40px' }} src={dual?.team_2?.logo_img} />
        <div>{dual?.team_2?.name}</div>
        <div>({dual?.team_2?.win} - {dual?.team_2?.loss})</div>
        <button style={{ fontWeight: 'bold', cursor: 'pointer', backgroundColor: 'white', height: '30px', width: '60px', border: 'none', color: 'rgb(40, 83, 129)' }}>START</button>
    </div>
</div> */}
