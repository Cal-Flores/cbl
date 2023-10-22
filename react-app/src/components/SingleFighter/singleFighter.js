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
    let tourWins;
    let tourLoss;
    let allMedals;
    if (tourMatches) {
        let matches = Object?.values(tourMatches)
        let wins = matches.filter(ele => ele.winner == fighter.name)
        tourWins = wins.length

        let loss = matches.filter(ele => ele.loser == fighter.name)
        tourLoss = loss.length
    }

    if (medals) {
        allMedals = Object?.values(medals)
    }
    console.log('heres my fighter', fighter)
    console.log('here are his matches', tourMatches)
    console.log('here are his medals', allMedals)
    console.log('here is the team info', team)

    useEffect(() => {
        if (fighterId) dispatch(getOneFighter(fighterId))
    }, [dispatch])

    return (
        <div id='fightercont'>
            <div>
                <div id='fighttags'>
                    <div className='fightpnt'>{fighter?.points} <span className='pts'>PTS</span></div>
                    <div className='nickname'>"{fighter?.nickname.toUpperCase()}"</div>
                    <div className='fightname'>{fighter?.name.toUpperCase()}</div>
                    <div className='fightweight'>{fighter?.weight}lb Division</div>
                    <div className='fightweight'>Tournament Record: {tourWins} - {tourLoss}</div>
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
            <div>
                <img src={fighter?.body_img} style={{ height: '490px', width: '322px' }} />
            </div>
            <div>
                <img style={{ width: '160px', height: '160px' }} src={team?.logo_img} />
                <div>{team?.name}</div>
                {allMedals?.map(medal => (
                    <div key={medal?.id}>{medal?.place} at {medal?.year} NCAA Championship</div>
                ))}
            </div>
        </div>
    )
}


export default SingleFighter
