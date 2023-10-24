import React, { useEffect, useState } from 'react';
import { useDispatch, useSelector } from 'react-redux'
import './allFighters.css';
import { Link, Redirect, useHistory, useParams } from 'react-router-dom'
import { getAllFighters } from '../../store/fighters'


function AllFighters() {
    const dispatch = useDispatch()
    const history = useHistory()
    let allFighters = useSelector(state => state.fighters.All_Fighters)
    console.log('zo-wee-mama', allFighters)

    useEffect(() => {
        dispatch(getAllFighters())
    }, [dispatch])

    return (
        <h1 style={{ marginTop: '30%', fontSize: '100px', width: '1000px', color: 'blue' }}>All Fighters yeah</h1>
    )
}

export default AllFighters;
