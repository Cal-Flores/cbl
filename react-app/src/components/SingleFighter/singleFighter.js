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
    let tourWins;
    let tourLoss;
    let allMedals;
    let lastMatch;
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
    // console.log('heres my fighter', fighter)
    // console.log('here are his matches', tourMatches)
    // console.log('here are his medals', allMedals)
    // console.log('here is the team info', team)
    // console.log('here is his last opp', opp)
    // console.log('last match', lastMatch)

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
        </div>
    )
}


export default SingleFighter
