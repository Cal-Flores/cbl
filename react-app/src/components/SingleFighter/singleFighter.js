import React, { useEffect, useState } from 'react';
import { useDispatch, useSelector } from 'react-redux'
import { useParams, useHistory } from "react-router-dom";
import './singleFighter.css';
import { getOneFighter } from '../../store/fighters';


function SingleFighter() {
    const dispatch = useDispatch();
    const history = useHistory();
    const routeParams = useParams();
    const fighterId = routeParams.fightId

    let fighter = useSelector(state => state.fighters.Fighter)
    let tourMatches = useSelector(state => state.fighters.Tour_Fights)
    let medals = useSelector(state => state.fighters.Medals)
    let team = useSelector(state => state.fighters.Team)
    let opp = useSelector(state => state.fighters.last_opp)
    let tourMatchesArr;
    if (tourMatches) tourMatchesArr = Object.values(tourMatches)
    let tourWins;
    let tourLoss;
    let allMedals;
    let lastMatch;
    let wins = 0;
    let loss = 0;
    if (tourMatches) {
        let matches = Object?.values(tourMatches)
        let wins = matches.filter(ele => ele.winner == fighter.name)
        tourWins = wins.length

        let loss = matches.filter(ele => ele.loser == fighter.name)
        tourLoss = loss.length

        lastMatch = matches[matches.length - 1]
    }

    if (medals) {
        allMedals = Object?.values(medals)
    }
    console.log('heres my fighter', fighter)
    console.log('here are his matches', tourMatches)
    console.log('here are his medals', allMedals)
    console.log('here is the team info', team)
    console.log('here is his last opp', opp)
    console.log('last match', lastMatch)
    console.log("here are the matches in array", tourMatchesArr)

    useEffect(() => {
        if (fighterId) dispatch(getOneFighter(fighterId))
    }, [dispatch])

    return (
        <div className='ultdiv'>
            <div style={{ backgroundImage: "url(" + `${team?.background_img}` + ")" }} className='topsliver'></div>

            <div id='fightercont'>
                <div id='left'>
                    <div id='fighttags'>
                        <div className='fightpnt'>{fighter?.points} <span className='pts'>PTS</span></div>
                        <div className='nickname'>
                            {fighter?.nickname &&
                                <div>"{fighter?.nickname.toUpperCase()}"</div>
                            }
                        </div>
                        <div className='fightname'>{fighter?.name.toUpperCase()}</div>
                        <div className='fightweight'>{fighter?.weight}lb Division</div>
                        <div className='fightweight'>Tournament Record: {tourWins} - {tourLoss}</div>
                        <div className='fightweight'>All-Time Record: 28 - 4</div>
                    </div>
                    <div className='reccont'>
                        <div className='wintxt'>
                            <div className='recwins'>{fighter?.tour_win}</div>
                            <div>Wins</div>
                        </div>
                        <div className='line'>

                        </div>
                        <div className='wintxt'>
                            <div className='recloss'>{fighter?.tour_loss}</div>
                            <div>Losses</div>
                        </div>
                    </div>
                </div>
                <div id='bodyimg'>
                    <img src={fighter?.body_img} style={{ height: '490px', width: '322px' }} />
                </div>
                <div id='fighterteam'>
                    <img className='flogoteam' style={{ width: '120px', height: '120px' }} src={team?.logo_img} />
                    <div className='lastopp'>
                        <div className='oppdiv'>
                            <div className='fightweight'>LAST FIGHT</div>
                            <div className='fightweight'>UFC</div>
                        </div>
                        <div className='oppdiv'>
                            <img src={fighter?.prof_img} style={{ height: '108px', width: '173px' }} />
                            {opp?.prof_img &&
                                <div>
                                    <img src={opp?.prof_img} style={{ height: '108px', width: '173px' }} />
                                </div>
                            }
                            {!opp?.prof_img &&
                                <div>
                                    <img src={'../../../images/blank.png'} style={{ height: '108px', width: '173px' }} />
                                </div>
                            }
                        </div>
                        <div className='oppdiv2'>
                            <div className='fightweight'>{lastMatch?.match}</div>
                            <div className='fightweight'>{lastMatch?.year} NCAA Championship</div>
                        </div>
                    </div>
                    <div>
                        {allMedals?.map(medal => (
                            <div className='fighterhistory' key={medal?.id}>{medal?.place} at {medal?.year} NCAA Championship</div>
                        ))}
                    </div>
                </div>
            </div >
            <div id='tourresbg' style={{ backgroundImage: "url(" + `${team?.background_img}` + ")" }}>
                <div id='tourResults' >
                    {tourMatchesArr?.map(match => (
                        <div className='matchres' key={match?.id}>
                            {match?.winner == fighter?.name &&
                                <div className='frwin'>
                                    <div className='frwinW'>W</div>
                                    <div style={{ marginLeft: '6%', width: '300px' }}>{match?.loser}</div>
                                    <div style={{ marginLeft: '2%', width: '100px' }}>{match?.method}</div>
                                    <div style={{ marginLeft: '6%', width: '250px' }}>{match?.match}</div>
                                    <div style={{ marginLeft: '3%', width: '350px' }}>NCAA Championship {match?.year}</div>
                                    <div style={{ marginLeft: '3%', width: '100px', fontSize: '22px' }}>{wins += 1} - {loss}</div>
                                </div>
                            }
                            {match?.loser == fighter?.name &&
                                <div className='frloss'>
                                    <div className='frlossL'>L</div>
                                    <div style={{ marginLeft: '7.3%', width: '300px' }}>{match?.winner}</div>
                                    <div style={{ marginLeft: '2%', width: '100px' }}>{match?.method}</div>
                                    <div style={{ marginLeft: '6%', width: '250px' }}>{match?.match}</div>
                                    <div className='ncaachamp' style={{ marginLeft: '3%', width: '350px' }}>NCAA Championship {match?.year}</div>
                                    <div style={{ marginLeft: '3%', width: '100px', fontSize: '22px' }}>{wins} - {loss += 1}</div>
                                </div>
                            }
                        </div>
                    ))}
                </div>
            </div>
        </div>
    )
}


export default SingleFighter
