import React, { useEffect, useState } from 'react';
import { useDispatch, useSelector } from 'react-redux'
import './playoffs.css';

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
            <div style={{ fontSize: '22px', marginLeft: '5%' }}>PLAYOFF PICTURE</div>
            <hr></hr>
            {playoffData &&
                <div>
                    <div className='playdiv'>
                        <div className='playdivson'>
                            <h3 className='playhead'>Division Leaders</h3>
                            <p className='playpara'>If the season ended today, these would be the leaders</p>
                            {playoffData?.afc_leaders?.map((team, index) => (
                                <div className='playcardwrap'>
                                    <div className='playcard' key={index}>
                                        <span>{index + 1}</span>
                                        <img style={{ height: '55px', width: '55px' }} src={team?.logo_img} />
                                        <img style={{ width: '150px', height: '28px', marginRight: '15%', marginLeft: '4%' }} src={team.heavy} />
                                        <div>{team?.curr_wins} - {team?.curr_loss}</div>
                                        <div>·</div>
                                        <div>{team?.conf} {team?.divison}</div>
                                    </div>
                                    <div className='playbye'>
                                        <div className='playnext'>Next Week Matchup</div>
                                        <img style={{ height: '30px', width: '30px' }} src={team?.logo_img} />
                                        <div>Bye</div>
                                    </div>
                                </div>

                            ))}
                            {playoffData?.afc_playoff_teams?.map((team, index) => (
                                <div className='playcardwrap'>
                                    <div className='playcard' key={index}>
                                        <span>{index + 5}</span>
                                        <img style={{ height: '55px', width: '55px' }} src={team?.logo_img} />
                                        <img style={{ width: '150px', height: '28px', marginRight: '15%', marginLeft: '4%' }} src={team.heavy} />
                                        <div>{team?.curr_wins} - {team?.curr_loss}</div>
                                        <div>·</div>
                                        <div>{team?.conf} {team?.divison}</div>
                                    </div>
                                    <div className='playbye'>
                                        <div className='playnext'>Next Week Matchup</div>
                                        <img style={{ height: '30px', width: '30px' }} src={team?.logo_img} />
                                        <div>Bye</div>
                                    </div>
                                </div>
                            ))}
                        </div>

                        <div className='playdivson'>
                            <h3 className='playhead'>Division Leaders</h3>
                            <p className='playpara'>If the season ended today, these would be the leaders</p>
                            {playoffData?.nfc_leaders?.map((team, index) => (
                                <div className='playcardwrap'>
                                    <div className='playcard' key={index}>
                                        <span>{index + 1}</span>
                                        <img style={{ height: '55px', width: '55px' }} src={team?.logo_img} />
                                        <img style={{ width: '150px', height: '28px', marginRight: '15%', marginLeft: '4%' }} src={team.heavy} />
                                        <div>{team?.curr_wins} - {team?.curr_loss}</div>
                                        <div>·</div>
                                        <div>{team?.conf} {team?.divison}</div>
                                    </div>
                                    <div className='playbye'>
                                        <div className='playnext'>Next Week Matchup</div>
                                        <img style={{ height: '30px', width: '30px' }} src={team?.logo_img} />
                                        <div>Bye</div>
                                    </div>
                                </div>

                            ))}
                            {playoffData?.nfc_playoff_teams?.map((team, index) => (
                                <div className='playcardwrap'>
                                    <div className='playcard' key={index}>
                                        <span>{index + 5}</span>
                                        <img style={{ height: '55px', width: '55px' }} src={team?.logo_img} />
                                        <img style={{ width: '150px', height: '28px', marginRight: '15%', marginLeft: '4%' }} src={team.heavy} />
                                        <div>{team?.curr_wins} - {team?.curr_loss}</div>
                                        <div>·</div>
                                        <div>{team?.conf} {team?.divison}</div>
                                    </div>
                                    <div className='playbye'>
                                        <div className='playnext'>Next Week Matchup</div>
                                        <img style={{ height: '30px', width: '30px' }} src={team?.logo_img} />
                                        <div>Bye</div>
                                    </div>
                                </div>
                            ))}
                        </div>










                    </div>

                </div>
            }
        </div>
    )
}

export default Playoffs
