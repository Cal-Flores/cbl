import React, { useEffect, useState } from 'react';
import { useDispatch, useSelector } from 'react-redux'
import { Link, Redirect, useHistory, useParams } from 'react-router-dom'

function TradedFighters() {

    const history = useHistory()
    const [fighters, setFighters] = useState(null);

    useEffect(() => {
        const fetchPicks = async () => {
            try {
                const response = await fetch('/api/fighter/tradedFighters');
                if (response.ok) {
                    const data = await response.json();
                    const fightersArr = Object.values(data.Traded)
                    setFighters(fightersArr);
                } else {
                    console.error('Failed to fetch draft order');
                }
            } catch (error) {
                console.error('Error fetching data:', error);
            }
        };
        fetchPicks();
    }, []);

    useEffect(() => {
        console.log('HERE\'S THE TRADED FIGHTERS', fighters);
    }, [fighters]);

    return (
        <div id='facont'>
            <h1 className='faheader'>
                Trade Block
            </h1>
            <div className='falinks'>
                <div onClick={(e) => history.push('/order')} className='dorder'>Draft Order</div>
                <div onClick={(e) => history.push('/trades')} className='dorder'>Trades</div>
            </div>
            {fighters &&
                <div className='freecont'>
                    {fighters.map(fighter => (
                        <div key={fighter.id}>
                            <div>
                                <div style={{}} key={fighter?.id} className='allfacard'>
                                    <div onClick={(e) => history.push(`/fighter/${fighter?.id}`)} className='draftchild'>
                                        <img src={fighter?.prof_img} style={{ height: '115px', width: '184px', borderBottom: '1px solid gray', marginBottom: '5%' }} />
                                        {fighter?.nickname &&
                                            <div className='allfnick'>"{fighter?.nickname.toUpperCase()}"</div>
                                        }
                                        {!fighter?.nickname &&
                                            <div style={{ height: '13px' }}></div>
                                        }
                                        <div className='allfaname'>{fighter?.name.toUpperCase()}</div>
                                        <div style={{ marginBottom: '3%', fontWeight: 'bold' }}>{fighter?.team_name}</div>
                                        <div >{fighter?.weight}lb Division</div>
                                    </div>

                                </div>
                            </div>

                        </div>
                    ))}
                </div>
            }
        </div>
    )
}


export default TradedFighters;
