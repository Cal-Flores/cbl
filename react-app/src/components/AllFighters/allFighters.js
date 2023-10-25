import React, { useEffect, useState } from 'react';
import { useDispatch, useSelector } from 'react-redux'
import './allFighters.css';
import { Link, Redirect, useHistory, useParams } from 'react-router-dom'
import { createSearch, getAllFighters, getFightersByWeight } from '../../store/fighters'


function AllFighters() {
    const dispatch = useDispatch()
    const history = useHistory()
    let allFighters = useSelector(state => state.fighters.All_Fighters)
    let searchedFighters = useSelector(state => state.fighters)
    let imgFighters = allFighters?.filter(fighter => fighter.prof_img.length > 0)
    let [active, setActive] = useState('all')
    const [search, setSearch] = useState('')

    console.log('hello all', searchedFighters)
    const getAll = async () => {
        dispatch(getAllFighters())
        setActive('all')
    }

    const getFly = async () => {
        dispatch(getFightersByWeight(125))
        setActive('125')
    }
    const getBantam = async () => {
        dispatch(getFightersByWeight(133))
        setActive('133')
    }
    const getFeather = async () => {
        dispatch(getFightersByWeight(149))
        setActive('149')
    }
    const getLight = async () => {
        dispatch(getFightersByWeight(157))
        setActive('157')
    }
    const getWelter = async () => {
        dispatch(getFightersByWeight(174))
        setActive('174')
    }
    const getMiddle = async () => {
        dispatch(getFightersByWeight(185))
        setActive('185')
    }
    const getLheavy = async () => {
        dispatch(getFightersByWeight(205))
        setActive('205')
    }
    const getHeavy = async () => {
        dispatch(getFightersByWeight(285))
        setActive('285')
    }

    const searcher = (e) => {
        e.preventDefault()
        let obj = {
            search
        }
        dispatch(createSearch(obj))
        setSearch('')
    }


    useEffect(() => {
        dispatch(getAllFighters())
    }, [dispatch])


    return (

        <div>
            <style>
                @import url('https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Molengo&family=Rye&display=swap');
            </style>
            <div id='allfcont'>
                <div className='allfnav'>
                    <div onClick={getAll} className={(active == 'all') ? 'activeNow' : 'navnums'}>All</div>
                    <div onClick={getFly} className={(active == '125') ? 'activeNow' : 'navnums'}>125</div>
                    <div onClick={getBantam} className={(active == '133') ? 'activeNow' : 'navnums'}>133</div>
                    <div onClick={getFeather} className={(active == '149') ? 'activeNow' : 'navnums'}>149</div>
                    <div onClick={getLight} className={(active == '157') ? 'activeNow' : 'navnums'}>157</div>
                    <div onClick={getWelter} className={(active == '174') ? 'activeNow' : 'navnums'}>174</div>
                    <div onClick={getMiddle} className={(active == '185') ? 'activeNow' : 'navnums'}>185</div>
                    <div onClick={getLheavy} className={(active == '205') ? 'activeNow' : 'navnums'}>205</div>
                    <div onClick={getHeavy} className={(active == '285') ? 'activeNow' : 'navnums'}>HWT</div>
                    <div style={{ width: '2000px', paddingLeft: '40%', paddingRight: '40%', marginBottom: '2%' }}>
                        <form onSubmit={searcher}>
                            <div>
                                <i style={{ position: 'absolute', marginTop: '.6%', marginLeft: '.8%', color: 'gray', fontSize: '13px' }} class="fa-solid fa-magnifying-glass"></i>
                                <input className='search' placeholder='Search Athletes' type='text' value={search} onChange={(e) => setSearch(e.target.value)} required />
                            </div>
                        </form>
                    </div>
                </div>
                {imgFighters?.map(fighter => (
                    <div key={fighter?.id} className='allfcard'>
                        <div className='child' style={{ height: '250px', width: '270px', zIndex: '2', position: 'absolute', backgroundColor: 'rgb(227, 224, 224)' }}>
                            <img src={fighter?.prof_img} style={{ height: '115px', width: '184px', borderBottom: '1px solid gray', }} />
                            {fighter?.nickname &&
                                <div className='allfnick'>"{fighter?.nickname.toUpperCase()}"</div>
                            }
                            <div className='allfname'>{fighter?.name.toUpperCase()}</div>
                            <div >{fighter?.weight}lb Division</div>
                            <div style={{ fontSize: '20px', fontWeight: 'bold' }}>12 - 5</div>
                        </div>
                        <div class='hoverbox' style={{ height: '250px', width: '270px', zIndex: '1' }}>
                            <div className='hboxleft'>
                                {fighter?.nickname &&
                                    <div className='allfnick'>"{fighter?.nickname.toUpperCase()}"</div>
                                }
                                <div className='allfname'>{fighter?.name}</div>
                                <div className='allfname'>{fighter?.team_name.split(' ')[fighter?.team_name.split(' ').length - 1]}</div>
                                <div className='allfteam'>{fighter?.points} Pts</div>
                                <button onClick={(e) => history.push(`/fighter/${fighter?.id}`)} className='profbtn'>FIGHTER PROFILE</button>
                            </div>
                            <div>
                                <img style={{ height: '175px', width: '115px', zIndex: '-1', paddingTop: '30px' }} src={fighter?.body_img} />
                            </div>
                        </div>
                    </div>
                ))}
            </div>
        </div >
    )
}

export default AllFighters;
