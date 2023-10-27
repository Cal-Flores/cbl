import React, { useEffect, useState } from 'react';
import { useDispatch, useSelector } from 'react-redux'
import './draft.css';
import { Link, Redirect, useHistory, useParams } from 'react-router-dom'


function DraftForm({ fighter }) {
    console.log('WEL U GET TO FIDDLE YOU GET DOWN TO', fighter)
    return (

        <div>
            <h1>Hello world</h1>
        </div >
    )
}


export default DraftForm
