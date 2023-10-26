import React, { useEffect, useState } from 'react';
import { useDispatch, useSelector } from 'react-redux'
import './draft.css';
import { Link, Redirect, useHistory, useParams } from 'react-router-dom'
import { getAllFighters } from '../../store/fighters';

function FreeAgents() {
    const dispatch = useDispatch()
    const history = useHistory()
    let allFighters = useSelector(state => state.fighters.All_Fighters)
    let freeAgents = allFighters?.filter(fighter => fighter.team_name == 'Free Agent')
    freeAgents?.sort((a, b) => a.weight - b.weight)
    console.log('free agents:', freeAgents)

    useEffect(() => {
        dispatch(getAllFighters())
    }, [dispatch])

    return (
        <div id='facont'>
            <h1 className='faheader'>FREE AGENTS</h1>
            <div className='freecont'>
                {freeAgents?.map(fighter => (
                    <div onClick={(e) => history.push(`/fighter/${fighter?.id}`)} key={fighter?.id} className='allfacard'>
                        <div className='child'>
                            <img src={fighter?.prof_img} style={{ height: '115px', width: '184px', borderBottom: '1px solid gray', marginBottom: '5%' }} />
                            {fighter?.nickname &&
                                <div className='allfnick'>"{fighter?.nickname.toUpperCase()}"</div>
                            }
                            {!fighter?.nickname &&
                                <div style={{ height: '13px' }}></div>
                            }
                            <div className='allfaname'>{fighter?.name.toUpperCase()}</div>
                            <div >{fighter?.weight}lb Division</div>
                        </div>
                        <button style={{ bottom: '0', height: '30px', width: '60px' }} className='profbtn'>DRAFT</button>
                    </div>
                ))}
            </div>
        </div >
    )
}


export default FreeAgents
