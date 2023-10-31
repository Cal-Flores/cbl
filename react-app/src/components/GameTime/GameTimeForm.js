import React, { useEffect, useState } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { useParams } from 'react-router-dom';

const GameTimeForm = () => {

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
        console.log('HERE IS SQUAD 1 DUAL INFOOOOOOO', dualInfo)
    }
    if (dualInfo?.team_2) {
        squadTwo = Object.values(dualInfo?.team_2).sort((a, b) => a.weight - b.weight)
        console.log('HERE IS SQUAD 2 FORMM', squadTwo)
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
        const dataToSend = allFightDetails.map((fight) => ({
            winner: fight.winner,
            loser: fight.loser,
            method: fight.method,
            round: fight.round
        }));

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
                        <div key={index}>
                            <h3>{squadOne[index]?.weight} lbs</h3>
                            <div>
                                <label>
                                    Winner:
                                    <select value={fight.winner} onChange={(e) => handleWinnerChange(e, index)}>
                                        <option value="">Select winner</option>
                                        <option value={squadOne[index]?.name}>{squadOne[index]?.name}</option>
                                        <option value={squadTwo[index]?.name}>{squadTwo[index]?.name}</option>
                                    </select>
                                </label>
                            </div>
                            <div>
                                <label>
                                    Method:
                                    <select value={fight.method} onChange={(e) => handleMethodChange(e, index)}>
                                        <option value="">Select method</option>
                                        <option value="KO">KO</option>
                                        <option value="TKO">TKO</option>
                                        <option value="SUB">SUB</option>
                                        <option value="DEC">DEC</option>
                                        <option value="M.DEC">M.DEC</option>
                                        <option value="S.DEC">S.DEC</option>
                                    </select>
                                </label>
                            </div>
                            <div>
                                <label>
                                    Round:
                                    <select value={fight.round} onChange={(e) => handleRoundChange(e, index)}>
                                        <option value="">Select method</option>
                                        <option value='1'>1</option>
                                        <option value="2">2</option>
                                        <option value="3">3</option>
                                    </select>
                                </label>
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
