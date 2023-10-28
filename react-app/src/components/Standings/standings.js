import React, { useEffect, useState } from 'react';
import { useDispatch, useSelector } from 'react-redux'
import './standings.css';
import { getAllTeams } from '../../store/teams';
import { Link, Redirect, useHistory, useParams } from 'react-router-dom'


function Standings() {
    const dispatch = useDispatch()
    const history = useHistory()
    let teams = useSelector(state => state.teams.All_Teams)

    let nfcNorth = teams?.filter(team => team.conf == 'NFC' && team.divison == 'North').sort((a, b) => a.wins - b.wins)
    let nfcEast = teams?.filter(team => team.conf == 'NFC' && team.divison == 'East')
    let nfcSouth = teams?.filter(team => team.conf == 'NFC' && team.divison == 'South')
    let nfcWest = teams?.filter(team => team.conf == 'NFC' && team.divison == 'West')

    let afcNorth = teams?.filter(team => team.conf == 'AFC' && team.divison == 'North')
    let afcEast = teams?.filter(team => team.conf == 'AFC' && team.divison == 'East')
    let afcSouth = teams?.filter(team => team.conf == 'AFC' && team.divison == 'South')
    let afcWest = teams?.filter(team => team.conf == 'AFC' && team.divison == 'West')

    console.log('HERES THE STANDINGS', nfcNorth)
    const divisionLeader = (allTeams, conf, div) => {
        teams = allTeams.filter(team => team => team.conf == 'NFC' && team.divison == 'North').sort((a, b) => a.wins - b.wins)
    }


    useEffect(() => {
        dispatch(getAllTeams())
    }, [dispatch])
    return (
        <div style={{ marginTop: '200px' }}>
            <h1>STANDINGS</h1>

        </div>
    )
}

export default Standings;
