import React, { useEffect, useState } from 'react';
import { useDispatch, useSelector } from 'react-redux'
import './draft.css';
import { Link, Redirect, useHistory, useParams } from 'react-router-dom'
import { getAllFighters } from '../../store/fighters';
// imports for the modal
import { useModal } from "../../context/Modal";
import DraftForm from './draftForm';
import OpenModalButton from "../OpenModalButton";

const btnStyle = {
    border: 'none',
    backgroundColor: 'rgb(25, 25, 25)',
    fontSize: '12px',
    padding: '2%',
    color: 'white',
};

function FreeAgents() {
    const dispatch = useDispatch()
    const history = useHistory()
    let allFighters = useSelector(state => state.fighters.All_Fighters)
    let freeAgents = allFighters?.filter(fighter => fighter.team_name == 'Free Agent')
    freeAgents?.sort((a, b) => a.weight - b.weight)
    // console.log('free agents:', freeAgents)

    // must be imported to use the modal
    const { setModalContent, setOnModalClose } = useModal();

    // function created copy and paste
    const openCustomModal = () => {
        setModalContent(
            <DraftForm
                closeModal={() => setModalContent(null)} // Pass the closeModal function
            />
        );
        setOnModalClose(() => {
            console.log('Modal Closed');
        });
    };


    useEffect(() => {
        dispatch(getAllFighters())
    }, [dispatch])

    //onClick={(e) => history.push(`/fighter/${fighter?.id}`)}

    return (
        <div id='facont'>
            <h1 className='faheader'>FREE AGENTS</h1>
            <div className='freecont'>
                {freeAgents?.map(fighter => (
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
                                <div >{fighter?.weight}lb Division</div>
                            </div>
                            <OpenModalButton
                                className='protbtn'
                                modalComponent={DraftForm}
                                buttonText="DRAFT"
                                fighter={fighter} // Pass the fighter object directly
                                style={btnStyle}
                            />
                        </div>
                    </div>
                ))}
            </div>
        </div >
    )
}


export default FreeAgents
