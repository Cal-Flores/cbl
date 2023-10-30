// Inside the GameTime component
import React from 'react';
import { useHistory, useLocation } from 'react-router-dom';


function GameTime(props) {
    const location = useLocation();
    const { state } = location;
    const dualInfo = state?.dualInfo;
    const team1Info = state?.team1Info;
    const team2Info = state?.team2Info;

    console.log('this game days dual Info', dualInfo);
    console.log('heres team 1', team1Info);
    console.log('heres team 2', team2Info);

    return (
        <div style={{ marginTop: '6%' }}>
            <h1>GAME DAY</h1>
        </div>
    );
}

export default GameTime;
