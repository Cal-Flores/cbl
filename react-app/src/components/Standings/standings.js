import React, { useEffect, useState } from 'react';
import { useDispatch, useSelector } from 'react-redux'
import './standings.css';
import { getAllTeams } from '../../store/teams';
import { Link, Redirect, useHistory, useParams } from 'react-router-dom'


function Standings() {
    const dispatch = useDispatch()
    const history = useHistory()
    const [standingsData, setStandingsData] = useState(null);
    const [nfc_display, setnfc_display] = useState(true);

    useEffect(() => {
        const fetchStandings = async () => {
            try {
                const response = await fetch('/api/team/standings');
                if (response.ok) {
                    const data = await response.json();
                    setStandingsData(data);
                    console.log('Standings Data:', data);
                } else {
                }
            } catch (error) {
            }
        };

        fetchStandings();
    }, []);

    const changeConfNfc = () => {
        setnfc_display(false)
    }
    const changeConfAfc = () => {
        setnfc_display(true)
    }



    return (

        <div style={{ marginTop: '125px' }}>
            <div class='conflinks'>
                <button class='displayBtn' onClick={changeConfAfc}><img style={{ width: '23px', height: '23px', marginRight: '10px' }} src='https://upload.wikimedia.org/wikipedia/commons/thumb/7/7a/American_Football_Conference_logo.svg/2560px-American_Football_Conference_logo.svg.png' />AFC Teams</button>
                <button class='displayBtn' onClick={changeConfNfc}><img style={{ width: '23px', height: '23px', marginRight: '10px' }} src='https://upload.wikimedia.org/wikipedia/commons/thumb/6/6f/National_Football_Conference_logo.svg/1200px-National_Football_Conference_logo.svg.png' />NFC Teams</button>
            </div>
            {nfc_display ? (
                <div>
                    {standingsData &&
                        <div id='stancont'>
                            <div className='standcard'>
                                <div className='standdiv'>North</div>
                                {standingsData?.standings?.aNorth?.aNorth.map(team => (
                                    <div className='standindv' onClick={(e) => history.push(`/teams/stats/${team?.id}`)}>
                                        <div className='standname'>{team?.name}</div>
                                        <img style={{ height: '55px', width: '55px' }} src={team?.logo_img} />
                                        <div className='standrec'>{team?.curr_wins} - {team?.curr_loss}</div>
                                        <div className='standdivrec'>{team?.div_win} - {team?.div_loss}</div>
                                        <div className='standpts'>Points: {team?.points}</div>
                                        <div className='standoff'>
                                            <div>Offense: {team?.offense}</div>
                                            <div>Defense: {team?.defense}</div>
                                        </div>
                                    </div>
                                ))}
                            </div>
                            <div className='standcard'>
                                <div className='standdiv'>East</div>
                                {standingsData?.standings?.aEast?.aEast.map(team => (
                                    <div className='standindv' onClick={(e) => history.push(`/teams/stats/${team?.id}`)}>
                                        <div className='standname'>{team?.name}</div>
                                        <img style={{ height: '55px', width: '55px' }} src={team?.logo_img} />
                                        <div className='standrec'>{team?.curr_wins} - {team?.curr_loss}</div>
                                        <div className='standdivrec'>{team?.div_win} - {team?.div_loss}</div>
                                        <div className='standpts'>Points: {team?.points}</div>
                                        <div className='standoff'>
                                            <div>Offense: {team?.offense}</div>
                                            <div>Defense: {team?.defense}</div>
                                        </div>
                                    </div>
                                ))}
                            </div>
                            <div className='standcard'>
                                <div className='standdiv'>South</div>
                                {standingsData?.standings?.aSouth?.aSouth.map(team => (
                                    <div className='standindv' onClick={(e) => history.push(`/teams/stats/${team?.id}`)}>
                                        <div className='standname'>{team?.name}</div>
                                        <img style={{ height: '55px', width: '55px' }} src={team?.logo_img} />
                                        <div className='standrec'>{team?.curr_wins} - {team?.curr_loss}</div>
                                        <div className='standdivrec'>{team?.div_win} - {team?.div_loss}</div>
                                        <div className='standpts'>Points: {team?.points}</div>
                                        <div className='standoff'>
                                            <div>Offense: {team?.offense}</div>
                                            <div>Defense: {team?.defense}</div>
                                        </div>
                                    </div>
                                ))}
                            </div>
                            <div className='standcard'>
                                <div className='standdiv'>West</div>
                                {standingsData?.standings?.aWest?.aWest.map(team => (
                                    <div className='standindv' onClick={(e) => history.push(`/teams/stats/${team?.id}`)}>
                                        <div className='standname'>{team?.name}</div>
                                        <img style={{ height: '55px', width: '55px' }} src={team?.logo_img} />
                                        <div className='standrec'>{team?.curr_wins} - {team?.curr_loss}</div>
                                        <div className='standdivrec'>{team?.div_win} - {team?.div_loss}</div>
                                        <div className='standpts'>Points: {team?.points}</div>
                                        <div className='standoff'>
                                            <div>Offense: {team?.offense}</div>
                                            <div>Defense: {team?.defense}</div>
                                        </div>
                                    </div>
                                ))}
                            </div>


                        </div>
                    }
                </div>
            ) : (
                <div>
                    {standingsData &&
                        <div id='stancont'>
                            <div className='standcard'>
                                <div className='standdiv'>North</div>
                                {standingsData?.standings?.nNorth?.nNorth.map(team => (
                                    <div className='standindv' onClick={(e) => history.push(`/teams/stats/${team?.id}`)}>
                                        <div className='standname'>{team?.name}</div>
                                        <img style={{ height: '55px', width: '55px' }} src={team?.logo_img} />
                                        <div className='standrec'>{team?.curr_wins} - {team?.curr_loss}</div>
                                        <div className='standdivrec'>{team?.div_win} - {team?.div_loss}</div>
                                        <div className='standpts'>Points: {team?.points}</div>
                                        <div className='standoff'>
                                            <div>Offense: {team?.offense}</div>
                                            <div>Defense: {team?.defense}</div>
                                        </div>
                                    </div>
                                ))}
                            </div>
                            <div className='standcard'>
                                <div className='standdiv'>East</div>
                                {standingsData?.standings?.nEast?.nEast.map(team => (
                                    <div className='standindv' onClick={(e) => history.push(`/teams/stats/${team?.id}`)}>
                                        <div className='standname'>{team?.name}</div>
                                        <img style={{ height: '55px', width: '55px' }} src={team?.logo_img} />
                                        <div className='standrec'>{team?.curr_wins} - {team?.curr_loss}</div>
                                        <div className='standdivrec'>{team?.div_win} - {team?.div_loss}</div>
                                        <div className='standpts'>Points: {team?.points}</div>
                                        <div className='standoff'>
                                            <div>Offense: {team?.offense}</div>
                                            <div>Defense: {team?.defense}</div>
                                        </div>
                                    </div>
                                ))}
                            </div>
                            <div className='standcard'>
                                <div className='standdiv'>South</div>
                                {standingsData?.standings?.nSouth?.nSouth.map(team => (
                                    <div className='standindv' onClick={(e) => history.push(`/teams/stats/${team?.id}`)}>
                                        <div className='standname'>{team?.name}</div>
                                        <img style={{ height: '55px', width: '55px' }} src={team?.logo_img} />
                                        <div className='standrec'>{team?.curr_wins} - {team?.curr_loss}</div>
                                        <div className='standdivrec'>{team?.div_win} - {team?.div_loss}</div>
                                        <div className='standpts'>Points: {team?.points}</div>
                                        <div className='standoff'>
                                            <div>Offense: {team?.offense}</div>
                                            <div>Defense: {team?.defense}</div>
                                        </div>
                                    </div>
                                ))}
                            </div>
                            <div className='standcard'>
                                <div className='standdiv'>West</div>
                                {standingsData?.standings?.nWest?.nWest.map(team => (
                                    <div className='standindv' onClick={(e) => history.push(`/teams/stats/${team?.id}`)}>
                                        <div className='standname'>{team?.name}</div>
                                        <img style={{ height: '55px', width: '55px' }} src={team?.logo_img} />
                                        <div className='standrec'>{team?.curr_wins} - {team?.curr_loss}</div>
                                        <div className='standdivrec'>{team?.div_win} - {team?.div_loss}</div>
                                        <div className='standpts'>Points: {team?.points}</div>
                                        <div className='standoff'>
                                            <div>Offense: {team?.offense}</div>
                                            <div>Defense: {team?.defense}</div>
                                        </div>
                                    </div>
                                ))}
                            </div>


                        </div>
                    }
                </div>
            )

            }
        </div>
    )
}

export default Standings;
