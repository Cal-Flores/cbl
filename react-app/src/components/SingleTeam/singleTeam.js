import React, { useEffect, useState } from 'react';
import { useDispatch, useSelector } from 'react-redux'
import { useParams, useHistory } from "react-router-dom";
import { getOneTeam } from '../../store/teams';
import './singleTeam.css';
import { cutOneFighter } from '../../store/fighters';


function SingleTeam() {
    const dispatch = useDispatch();
    const history = useHistory();
    const routeParams = useParams();
    const teamId = routeParams?.teamId

    let team = useSelector(state => state?.teams?.Team)
    let fighters = []
    fighters.push(team?.fly, team?.bantam, team?.phantam, team?.feather, team?.light, team?.cruiser, team?.welter, team?.middle, team?.light_heavy, team?.heavy)

    const cutPlayer = (id) => {
        console.log('im going to cut this ID', id)
        dispatch(cutOneFighter(id)).then(() => dispatch(getOneTeam(teamId)))
    }

    useEffect(() => {
        if (teamId) dispatch(getOneTeam(teamId))
    }, [dispatch])

    return (
        <div>
            <h1 className='teamname'><img src={team?.text} style={{ width: '300px', height: '100px' }} /></h1>
            <div id='fighterscont'>
                {fighters?.map(fighter => (
                    <div onClick={((e) => history.push(`/fighter/${fighter.id}`))} key={fighter?.id} id='teamssCard' style={{ backgroundImage: "url(" + `${team?.bg}` + ")", border: `5px solid ${team?.border}` }}>
                        <div>
                            <div className='fighterweight' >{fighter?.weight} lbs</div>
                        </div>
                        <div className='fstat'>
                            <div className='fimg'>
                                <img src={fighter?.prof_img} style={{ height: '135px', width: '217px', marginBottom: '5%' }} onError={(e) => { e.target.src = '../../../images/blank.png' }} />
                                <div className='fightername'>{fighter?.name}</div>
                            </div>
                            <div className='finforcont'>
                                <div className='finfo'>
                                    {/* <div className='fighterstat'>{fighter?.wins}-{fighter.losses}</div> */}
                                    <div className='fighterstat'>16-0</div>
                                    <div className='fighterstat'>{fighter?.points} pts</div>
                                </div>
                                <div>
                                    <button onClick={() => cutPlayer(fighter?.id)} style={{ height: '20px', width: '45px' }} class='teamBtn' >CUT</button>
                                </div>
                            </div>
                        </div>
                    </div>
                ))}
            </div>
        </div>
    )
}

export default SingleTeam;
