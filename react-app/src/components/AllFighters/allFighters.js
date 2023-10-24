import React, { useEffect, useState } from 'react';
import { useDispatch, useSelector } from 'react-redux'
import './allFighters.css';
import { Link, Redirect, useHistory, useParams } from 'react-router-dom'
import { getAllFighters } from '../../store/fighters'


function AllFighters() {
    const dispatch = useDispatch()
    const history = useHistory()
    let allFighters = useSelector(state => state.fighters.All_Fighters)
    let imgFighters = allFighters?.filter(fighter => fighter?.prof_img.length > 0)
    console.log('zo-wee-mama', allFighters)

    useEffect(() => {
        dispatch(getAllFighters())
    }, [dispatch])

    return (
        <div>
            <div id='allfcont' >

                {imgFighters?.map(fighter => (
                    <div className='allfcard'>
                        <div className='child' style={{ height: '250px', width: '225px', zIndex: '2', position: 'absolute', backgroundColor: 'rgb(227, 224, 224)' }}>
                            <img src={fighter?.prof_img} style={{ height: '115px', width: '184px', borderBottom: '1px solid gray', }} />
                            {fighter?.nickname &&
                                <div className='allfnick'>"{fighter?.nickname.toUpperCase()}"</div>
                            }
                            <div className='allfname'>{fighter?.name.toUpperCase()}</div>
                            <div >{fighter?.weight}lb Division</div>
                            <div>12 - 5</div>
                            <div className='allfteam'>{fighter?.team_name.split(' ')[fighter?.team_name.split(' ').length - 1]}</div>
                        </div>
                        <div class='hoverbox' style={{ height: '250px', width: '225px', zIndex: '1' }}>
                            <div>{fighter?.name}</div>
                            <img style={{ height: '175px', width: '115px' }} src={fighter?.body_img} />
                        </div>
                    </div>
                ))}
            </div>
        </div >
    )
}

export default AllFighters;
