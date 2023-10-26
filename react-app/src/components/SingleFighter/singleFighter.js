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
    const [seasonM, setseasonM] = useState(true)
    const [box, setBox] = useState('season')

    //############### usestates for switching the box on the right ######################
    const viewSeason = () => {
        setseasonM(false)
    }
    const viewTourn = () => {
        setseasonM(true)
    }

    const viewLastSeason = () => {
        setBox('season')
    }
    const viewLast = () => {
        setBox('last')
    }

    const viewMedal = () => {
        setBox('medal')
    }
    //####################### GRABBING RERLEVANT INFO FROM BACKEND ######################
    let fighter = useSelector(state => state.fighters.Fighter)
    let tourMatches = useSelector(state => state.fighters.Tour_Fights)
    let medals = useSelector(state => state.fighters.Medals)
    let team = useSelector(state => state.fighters.Team)
    let seasonMatches = useSelector(state => state.fighters.Season_Fights)


    let opp = useSelector(state => state.fighters.last_opp) //// GRABS LAST TOUR OPPONENT
    let seasonOpp = useSelector(state => state.fighters.last_season) //////  //// GRABS LAST SEASON OPPONENT
    let rightBox; // This variable is the div that changes based on state
    let tourMatchesArr; // all tournamnet matches are held here
    let seasonArr; // all season matches are held here
    let lastMatch; // this holds all the match deatails for TOURNAMNET
    let lastSeason; // this holds all the match details for SEASON
    let tourWins; // displays the total tour wins on the left side
    let tourLoss; // displays the total tour loss on the left side
    let allMedals; // holds all fighters medals
    let wins = 0; // for the display below grabs all tour wins
    let loss = 0; // for the display below grabs all tour losses
    let week = 0; // for the display below displays the week
    let season_wins = 0; // for the display below grabs all season wins
    let season_loss = 0; // for the display below grabs all season loss

    //########################## CHANGES THE OBJ TO ARR FOR TOUR AND SEASON MATCHES AND GRABS LAST MATCH ################
    if (seasonMatches) {
        seasonArr = Object.values(seasonMatches)
        lastSeason = seasonArr[seasonArr.length - 1]
    }
    if (tourMatches) tourMatchesArr = Object.values(tourMatches)

    if (tourMatches) {
        let matches = Object?.values(tourMatches)
        let wins = matches.filter(ele => ele.winner == fighter.name)
        tourWins = wins.length

        let loss = matches.filter(ele => ele.loser == fighter.name)
        tourLoss = loss.length

        lastMatch = matches[matches.length - 1]
    }
    //######################### GRABS ALL MEDALS FOR OBJ TO ARR ###################################
    if (medals) {
        allMedals = Object?.values(medals)
    }

    //########### console.logs for testing #########################################################
    // console.log('heres my fighter', fighter)
    // console.log('here are his matches', tourMatches)
    // console.log('here are his medals', allMedals)
    //console.log('here is the team info', team)
    //console.log('here is his last opp', opp)
    console.log('here is his last SEASON opp', seasonOpp)
    console.log('this is the last season match deatils', lastSeason)
    // console.log('last match', lastMatch)
    // console.log("here are the matches in array", tourMatchesArr)
    // console.log('current season matches are here', seasonArr)

    useEffect(() => {
        if (fighterId) dispatch(getOneFighter(fighterId))
    }, [dispatch])

    // ############################## conditionally renders the matches below ############################
    let contentDiv;
    if (seasonM == true) {
        contentDiv = (
            <div id='tourResults' >
                {seasonArr?.map(match => (
                    <div className='matchres' key={match?.id}>
                        {match?.winner == fighter?.name &&
                            <div className='frwin'>
                                <div className='frwinW'>W</div>
                                <div style={{ marginLeft: '6%', width: '300px' }}>{match?.loser}</div>
                                <div style={{ marginLeft: '2%', width: '100px' }}>{match?.method}</div>
                                {/* <div style={{ marginLeft: '6%', width: '250px' }}>{match?.match}</div> */}
                                <div style={{ marginLeft: '3%', width: '350px' }}>WEEK {week += 1}</div>
                                <div style={{ marginLeft: '3%', width: '100px', fontSize: '22px' }}>{season_wins += 1} - {season_loss}</div>
                            </div>
                        }
                        {match?.loser == fighter?.name &&
                            <div className='frloss'>
                                <div className='frlossL'>L</div>
                                <div style={{ marginLeft: '6%', width: '300px' }}>{match?.winner}</div>
                                <div style={{ marginLeft: '2%', width: '100px' }}>{match?.method}</div>
                                {/* <div style={{ marginLeft: '6%', width: '250px' }}>{match?.match}</div> */}
                                <div style={{ marginLeft: '3%', width: '350px' }}>WEEK {week += 1}</div>
                                <div style={{ marginLeft: '3%', width: '100px', fontSize: '22px' }}>{season_wins} - {season_loss += 1}</div>
                            </div>
                        }
                    </div>
                ))}
            </div>
        )
    } else {
        contentDiv = (
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
        )
    }

    // ################################### CONDITIONALLY RENDERS THE BOX ON THE RIGHT ######################################
    if (box == 'last') {
        rightBox = (
            <div className='lastopp'>
                <div className='oppdiv'>
                    <div onClick={viewLastSeason} className='boxtag'>LAST FIGHT</div>
                    <div onClick={viewLast} className='boxtag'>LAST TOURNAMENT</div>
                    <div onClick={viewMedal} className='boxtag'>VIEW MEDALS</div>
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
                    <div className='fightweight'>{lastMatch?.year} NCAA Championship</div>
                    <div className='fightweight'>{lastMatch?.match}</div>
                </div>
            </div>
        )
    } else if (box == 'medal') {
        rightBox = (
            <div className='lastopp'>
                <div className='oppdiv'>
                    <div onClick={viewLastSeason} className='boxtag'>LAST FIGHT</div>
                    <div onClick={viewLast} className='boxtag'>LAST TOURNAMENT</div>
                    <div onClick={viewMedal} className='boxtag'>VIEW MEDALS</div>
                </div>
                <div className='medaldiv'>
                    {allMedals?.map(medal => (
                        <div className='medalstxt' key={medal?.id}>{medal?.place} at {medal?.year} NCAA Championship</div>
                    ))}
                    {allMedals.length < 1 &&
                        <div className='medalstxt'>No Medals</div>
                    }
                </div>
            </div>
        )
    } else {
        rightBox = (
            <div className='lastopp'>
                <div className='oppdiv'>
                    <div onClick={viewLastSeason} className='boxtag'>LAST FIGHT</div>
                    <div onClick={viewLast} className='boxtag'>LAST TOURNAMENT</div>
                    <div onClick={viewMedal} className='boxtag'>VIEW MEDALS</div>
                </div>
                <div className='oppdiv'>
                    <img src={fighter?.prof_img} style={{ height: '108px', width: '173px' }} />
                    {seasonOpp?.prof_img &&
                        <div>
                            <img src={seasonOpp?.prof_img} style={{ height: '108px', width: '173px' }} />
                        </div>
                    }
                    {!seasonOpp?.prof_img &&
                        <div>
                            <img src={'../../../images/blank.png'} style={{ height: '108px', width: '173px' }} />
                        </div>
                    }
                </div>
                <div className='oppdiv2'>
                    <div className='fightweek'>WEEK {seasonArr?.length}</div>
                </div>
            </div>
        )
    }
    //#################################### END ################################################
    return (
        <div className='ultdiv'>
            <style>
                @import url('https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Molengo&family=Rye&display=swap');
            </style>
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
                        <div className='fightweight'>All-Time Record: {fighter?.all_win} - {fighter?.all_loss}</div>
                    </div>
                    <div className='reccont'>
                        <div className='wintxt'>
                            <div className='recwins'>{fighter?.wins}</div>
                            <div>Wins</div>
                        </div>
                        <div className='line'>

                        </div>
                        <div className='wintxt'>
                            <div className='recloss'>{fighter?.losses}</div>
                            <div>Losses</div>
                        </div>
                    </div>
                </div>
                <div id='bodyimg'>
                    <img src={fighter?.body_img} style={{ height: '490px', width: '322px' }} />
                </div>
                <div id='fighterteam'>
                    <img className='flogoteam' style={{ width: '120px', height: '120px' }} src={team?.logo_img} />
                    {rightBox}
                    <div>
                        {seasonM == false && <button className='seasonbtn' onClick={viewTourn}>View Season Fights</button>}
                        {seasonM == true && <button className='seasonbtn' onClick={viewSeason}>View Tournament Fights</button>}
                    </div>
                </div>
            </div >
            <div id='tourresbg' style={{ backgroundImage: "url(" + `${team?.background_img}` + ")" }}>
                <div className='seasonchange'>
                </div>
                <div>
                    {contentDiv}
                </div>
            </div>
        </div>
    )
}


export default SingleFighter
