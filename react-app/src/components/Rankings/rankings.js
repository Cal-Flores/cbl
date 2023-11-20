import React, { useEffect } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { getAllFighters } from '../../store/fighters';


function getFilteredFighters(allFighters, weight, limit = 12) {
    return allFighters
        ?.filter(fighter => fighter?.weight === weight)
        .sort((a, b) => {
            if (a.wins === b.wins) return b.points - a.points;
            return b.wins - a.wins;
        })
        .slice(0, limit);
}

function renderWeightClass(allFighters, weight, title) {
    const fighters = getFilteredFighters(allFighters, weight);
    return (
        fighters && (
            <div style={{ marginBottom: '2%', width: '335px', marginLeft: '3%', marginRight: '3%', color: 'rgb(88, 88, 88)' }}>
                <img
                    style={{ height: '135px', width: '217px', marginLeft: '25%', borderBottom: '1px solid gray' }}
               
                    src={fighters[0]?.prof_img}
                    alt={title}
                />
                <ol>
                    {fighters?.map(fighter => (
                        <div style={{ display: 'flex', flexDirection: 'row', marginBottom: '1.5%' }} key={fighter.id}>
                            <li style={{ width: '175px' }}>{fighter.name}</li>
                            <div style={{ width: '70px' }}>{fighter.points}pts</div>
                            <div>{fighter.wins} - {fighter.losses}</div>
                        </div>
                    ))}
                </ol>
            </div>
        )
    );
}

function Rankings() {
    const dispatch = useDispatch();
    const allFighters = useSelector(state => state.fighters.All_Fighters);

    useEffect(() => {
        dispatch(getAllFighters());
    }, [dispatch]);

    return (
        <div style={{ marginTop: '5%', marginLeft: '2%', marginLeft: '2%', width: '96%' }}>
            <div style={{ textAlign: 'center', marginBottom: '2%', fontSize: '30px' }}>FIGHTER RANKINGS</div>
            <div style={{ display: 'flex', flexDirection: 'row', flexWrap: 'wrap', justifyContent: 'space-evenly', }}>

                {renderWeightClass(allFighters, '125', 'Fly')}

                {renderWeightClass(allFighters, '133', 'Bantam')}

                {renderWeightClass(allFighters, '141', 'Phantam')}
                {renderWeightClass(allFighters, '149', 'Feather')}
                {renderWeightClass(allFighters, '157', 'Light')}
                {renderWeightClass(allFighters, '165', 'Cruiser')}
                {renderWeightClass(allFighters, '174', 'Welter')}
                {renderWeightClass(allFighters, '185', 'Middle')}
                {renderWeightClass(allFighters, '205', 'Light Heavy')}
                {renderWeightClass(allFighters, '285', 'Heavy')}
            </div>
        </div>
    );
}

export default Rankings;
