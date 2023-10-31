import React, { useEffect, useState } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { useParams } from 'react-router-dom';

const GameTimeForm = ({ scoreOne, scoreTwo }) => {

    const { id } = useParams();
    let [dualInfo, setDualInfo] = useState([])
    useEffect(() => {
        const fetchData = async () => {
            try {
                const response = await fetch(`/api/team/game/${id}`);
                if (!response.ok) {
                    throw new Error('Network response was not ok.');
                }
                const data = await response.json();
                setDualInfo(data.Dual_Stats);
            } catch (error) {
                console.error('Error fetching data:', error);
            }
        };
        fetchData();
    }, [id]);

    let squadOne;
    let squadTwo;
    if (dualInfo?.team_1) {
        squadOne = Object.values(dualInfo?.team_1).sort((a, b) => a.weight - b.weight)
    }
    if (dualInfo?.team_2) {
        squadTwo = Object.values(dualInfo?.team_2).sort((a, b) => a.weight - b.weight)
    }


    const [allFightDetails, setAllFightDetails] = useState(Array(10).fill({
        winner: '',
        method: '',
        round: '',
        loser: ''
    }));

    const handleWinnerChange = (e, index) => {
        const selectedWinner = e.target.value;
        const updatedDetails = [...allFightDetails];

        const fighterOneName = squadOne[index]?.name;
        const fighterTwoName = squadTwo[index]?.name;

        updatedDetails[index].winner = selectedWinner;
        updatedDetails[index].loser = selectedWinner === fighterOneName ? fighterTwoName : fighterOneName;

        setAllFightDetails(updatedDetails);
    };

    const handleMethodChange = (e, index) => {
        const updatedDetails = [...allFightDetails];
        updatedDetails[index] = { ...updatedDetails[index], method: e.target.value };
        setAllFightDetails(updatedDetails);
    };

    const handleRoundChange = (e, index) => {
        const updatedDetails = [...allFightDetails];
        updatedDetails[index] = { ...updatedDetails[index], round: e.target.value };
        setAllFightDetails(updatedDetails);
    };

    const handleSubmit = (e) => {
        e.preventDefault();

        // Extract only the necessary details to be sent to the backend
        const dataToSend = {
            // Add scoreOne and scoreTwo to the data being sent
            scoreOne: scoreOne,
            scoreTwo: scoreTwo,
            // Include other fight details (winner, loser, method, round) as needed
            fights: allFightDetails.map((fight) => ({
                winner: fight.winner,
                loser: fight.loser,
                method: fight.method,
                round: fight.round
            }))
        };

        fetch(`/api/team/gameFinish/${id}`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(dataToSend)
        })
            .then(response => {
                if (!response.ok) {
                    throw new Error('Network response was not ok.');
                }
                return response.json();
            })
            .then(data => {
                // Handle success response
                console.log('Data sent successfully:', data);
            })
            .catch(error => {
                console.error('Error sending data:', error);
            });
    };



    return (
        <div>
            {squadOne && squadTwo && (
                <form onSubmit={handleSubmit}>
                    {allFightDetails.map((fight, index) => (
                        <div className='formcont' key={index}>
                            <div className='squadweight'>{squadOne[index]?.weight} lbs</div>
                            <div className='sqform'>
                                <div>
                                    Winner:
                                </div>
                                <select className='squadselect' value={fight.winner} onChange={(e) => handleWinnerChange(e, index)}>
                                    <option value="">Select winner</option>
                                    <option value={squadOne[index]?.name}>{squadOne[index]?.name}</option>
                                    <option value={squadTwo[index]?.name}>{squadTwo[index]?.name}</option>
                                </select>
                            </div>
                            <div className='sqform'>
                                <label>
                                    Method:
                                </label>
                                <select className='squadselect' value={fight.method} onChange={(e) => handleMethodChange(e, index)}>
                                    <option value="">Select method</option>
                                    <option value="KO">KO</option>
                                    <option value="TKO">TKO</option>
                                    <option value="SUB">SUB</option>
                                    <option value="DEC">DEC</option>
                                    <option value="M.DEC">M.DEC</option>
                                    <option value="S.DEC">S.DEC</option>
                                </select>
                            </div>
                            <div className='sqform'>
                                <label>
                                    Round:
                                </label>
                                <select className='squadselect' value={fight.round} onChange={(e) => handleRoundChange(e, index)}>
                                    <option value="">Select Round</option>
                                    <option value='1'>1</option>
                                    <option value="2">2</option>
                                    <option value="3">3</option>
                                </select>
                            </div>
                        </div>
                    ))}
                    <button type="submit">Submit</button>
                </form>
            )}
        </div>
    );
}
export default GameTimeForm;
