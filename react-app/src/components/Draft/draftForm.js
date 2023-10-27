import React, { useEffect, useState } from 'react';
import { useDispatch, useSelector } from 'react-redux'
import './draft.css';
import { Link, Redirect, useHistory, useParams } from 'react-router-dom'
import { getAllTeams, getOneTeam } from '../../store/teams';
import { addFighterTeam } from '../../store/fighters';

const containerStyle = {
    display: 'flex',
    flexDirection: 'column',
    alignItems: 'center',
};

const labelStyle = {
    marginBottom: '8px',
};

const selectStyle = {
    padding: '8px',
    marginBottom: '16px',
    borderRadius: '4px',
    border: '1px solid #ccc',
    width: '200px',
    fontSize: '16px',
};

const buttonStyle = {
    backgroundColor: '#007bff',
    color: 'white',
    padding: '12px 20px',
    border: 'none',
    borderRadius: '4px',
    cursor: 'pointer',
    fontSize: '18px',
};


function DraftForm({ fighter, closeModal }) {
    const dispatch = useDispatch()
    const history = useHistory()
    let teams = useSelector(state => state.teams.All_Teams)
    let teamOptions = teams?.map(team => team.name)
    let fighterId = fighter.id
    console.log('howdy', fighterId)


    let [weightClass, setWeightClass] = useState('');
    let [team, setTeam] = useState('');
    const [error, setError] = useState(null);



    // Options for the weight class select field
    const weightClassOptions = [
        '125', '133', '141', '149', '157',
        '165', '174', '185', '205', '285'
    ];

    // Options for the team select field
    useEffect(() => {
        dispatch(getAllTeams())
    }, [dispatch])


    // Event handlers to update the selected values
    const handleWeightClassChange = (event) => {
        setWeightClass(event.target.value);
    };

    const handleTeamChange = (event) => {
        setTeam(event.target.value);
    };

    // Submit handler to process the form data
    const handleSubmit = async (event) => {
        event.preventDefault();
        //You can access the selected values in weightClass and team state variabless
        let draft = {
            team,
            weightClass,
            fighterId
        }
        const success = await dispatch(addFighterTeam(draft, setError));
        if (success) {
            console.log('SUCESSSSSSSSS!')
            history.push(`/fighter/${fighterId}`)
        }
    };
    return (
        <form onSubmit={handleSubmit} style={containerStyle}>
            {error && <div className="error">{error}</div>} {/* Render error message */}
            {/* ...rest of your form */}
            <div>
                <label htmlFor="weightClass" style={labelStyle}>
                    Select Weight Class:
                </label>
                <select
                    id="weightClass"
                    value={weightClass}
                    onChange={handleWeightClassChange}
                    style={selectStyle}
                >
                    <option value="">-- Select Weight Class --</option>
                    {weightClassOptions.map(option => (
                        <option key={option} value={option}>
                            {option}
                        </option>
                    ))}
                </select>
            </div>

            <div>
                <label htmlFor="team" style={labelStyle}>
                    Select Team:
                </label>
                <select
                    id="team"
                    value={team}
                    onChange={handleTeamChange}
                    style={selectStyle}
                >
                    <option value="">-- Select Team --</option>
                    {teamOptions?.map(option => (
                        <option key={option} value={option}>
                            {option}
                        </option>
                    ))}
                </select>
            </div>

            <button type="submit" style={buttonStyle}>
                Submit
            </button>
        </form>
    );
}


export default DraftForm
