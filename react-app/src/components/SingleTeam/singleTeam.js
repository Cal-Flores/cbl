import React, { useEffect, useState } from 'react';
import { useDispatch, useSelector } from 'react-redux'
import { useParams, useHistory } from "react-router-dom";
import { getOneTeam } from '../../store/teams';
import './singleTeam.css';


function SingleTeam() {
    const dispatch = useDispatch();
    const history = useHistory();
    const routeParams = useParams();
    const teamId = routeParams?.teamId

    let team = useSelector(state => state?.teams?.Team)

    let fighters = []
    fighters.push(team?.fly, team?.bantam, team?.feather, team?.light, team?.welter, team?.middle, team?.light_heavy, team?.heavy)


    useEffect(() => {
        if (teamId) dispatch(getOneTeam(teamId))
    }, [dispatch])

    return (
        <div>
            <h1 className='teamname'><img src={team?.text} style={{ width: '300px', height: '100px' }} /></h1>

            <div id='fighterscont'>
                {fighters?.map(fighter => (
                    <div id='teamssCard' onClick={(e) => history.push(`/fighter/${fighter.id}`)} style={{ backgroundImage: "url(" + `${team?.bg}` + ")" }} key={fighter?.id}>
                        <div>
                            <div className='fighterweight' >{fighter?.weight} lbs</div>
                        </div>
                        <div className='fstat'>
                            <div className='fimg'>
                                <img src={fighter?.prof_img} style={{ height: '135px', width: '217px', marginBottom: '5%' }} />
                                <div className='fightername'>{fighter?.name}</div>
                            </div>
                            <div className='finfo'>
                                <div className='fighterstat'>16-0</div>
                                <div className='fighterstat'>96 pts</div>
                            </div>
                            {fighter?.medal > 0 &&
                                <div className='fighterstat'>{fighter?.medal}x All American</div>
                            }
                        </div>
                    </div>
                ))}
            </div>
        </div>
    )
}

export default SingleTeam;
