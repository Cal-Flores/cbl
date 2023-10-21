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

    useEffect(() => {
        if (fighterId) dispatch(getOneFighter(fighterId))
    }, [dispatch])

    return <div>
        <h4>{fighter?.name}</h4>
        <img src={fighter?.prof_img} />
    </div>
}


export default SingleFighter
