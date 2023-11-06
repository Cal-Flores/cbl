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
    const [showReleaseBtn, setShowReleaseBtn] = useState(null);

    let team = useSelector(state => state?.teams?.Team)
    console.log('heres team deputy', team)
    let fighters = []
    fighters.push(team?.fly, team?.bantam, team?.phantam, team?.feather, team?.light, team?.cruiser, team?.welter, team?.middle, team?.light_heavy, team?.heavy)

    const cutPlayer = (e, id) => {
        const isConfirmed = window.confirm(
            'Release this fighter? Once released, other teams will be able to draft this player in free agency.'
        );
        if (isConfirmed) {
            dispatch(cutOneFighter(id)).then(() => dispatch(getOneTeam(teamId)));
        } else {
            history.push(`/teams/${teamId}`)
        }
    }

    const tradePlayer = (e, id) => {
        const isConfirmed = window.confirm(
            'Trade this fighter? Other teams can begin sending offeres for this fighter'
        );
        if (isConfirmed) {
            fetch(`/api/fighter/trade/${id}`, {
                method: 'GET',
                headers: {
                    'Content-Type': 'application/json',
                },
            })
                .then((response) => response.json())
                .then((data) => {
                    console.log('Trade successful', data);
                    // Perform actions after a successful trade if needed
                })
                .catch((error) => {
                    console.error('Trade failed:', error);
                    // Handle error scenario
                });
        } else {
            history.push(`/teams/${teamId}`)
        }
    }

    useEffect(() => {
        if (teamId) dispatch(getOneTeam(teamId))
    }, [dispatch])

    return (
        <div>
            <h1 onClick={(e) => history.push(`/teams/stats/${team.id}`)} className='teamname'><img src={team?.text} style={{ width: '300px', height: '100px' }} /></h1>
            <div id='fighterscont'>
                {fighters?.map(fighter => (
                    <div key={fighter?.id} id='teamssCard' style={{ backgroundImage: "url(" + `${team?.bg}` + ")", border: `5px solid ${team?.border}` }}
                        onMouseEnter={() => setShowReleaseBtn(fighter?.id)}
                        onMouseLeave={() => setShowReleaseBtn(null)}
                    >
                        <div>
                            <div className='fighterweight' >{fighter?.weight} lbs</div>
                        </div>
                        <div className='fstat'>
                            <div onClick={((e) => history.push(`/fighter/${fighter.id}`))} className='fimg'>
                                <img src={fighter?.prof_img} style={{ height: '135px', width: '217px', marginBottom: '5%' }} onError={(e) => { e.target.src = '../../../images/blank.png' }} />
                                <div className='fightername'>{fighter?.name}</div>
                            </div>
                            <div className='finforcont'>
                                <div className='finfo'>
                                    {/* <div className='fighterstat'>{fighter?.wins}-{fighter.losses}</div> */}
                                    <div className='fighterstat'>{fighter?.wins} - {fighter?.losses}</div>
                                    <div className='fighterstat'>{fighter?.points} pts</div>
                                </div>

                                <button onClick={(e) => cutPlayer(e, fighter.id)} style={{ color: `${team?.border}`, border: `1px solid ${team?.border}`, visibility: showReleaseBtn === fighter?.id ? 'visible' : 'hidden', }} class='cutBtn' >RELEASE</button>
                                <button onClick={(e) => tradePlayer(e, fighter.id)} style={{ color: `${team?.border}`, border: `1px solid ${team?.border}`, visibility: showReleaseBtn === fighter?.id ? 'visible' : 'hidden', }} class='cutBtn' >TRADE</button>

                            </div>
                        </div>
                    </div>
                ))}
            </div>
        </div>
    )
}

export default SingleTeam;
