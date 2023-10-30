import React from 'react';
import { NavLink, useHistory } from 'react-router-dom';
import { useSelector } from 'react-redux';
import ProfileButton from './ProfileButton';
import './Navigation.css';

function Navigation({ isLoaded }) {
	const sessionUser = useSelector(state => state.session.user);

	return (
		<div id='navcont'>
			<img style={{ width: '50px', height: '50px' }} src='https://static.www.nfl.com/image/upload/v1554321393/league/nvfr7ogywskqrfaiu38m.svg' />
			<div >
				<NavLink className='navlinks' exact to="/">Teams</NavLink>
			</div>
			<div >
				<NavLink className='navlinks' exact to="/fighters">Fighters</NavLink>
			</div>
			<div >
				<NavLink className='navlinks' exact to="/draft">Draft Class</NavLink>
			</div>
			<div >
				<NavLink className='navlinks' exact to="/standings">Standings</NavLink>
			</div>
			<div >
				<NavLink className='navlinks' exact to="/Schedule">Schedule</NavLink>
			</div>
			<div>
				<NavLink className='navlinks' exact to="/rankings">Rankings</NavLink>
			</div>
			<div>
				<NavLink className='navlinks' exact to="/">Tournaments</NavLink>
			</div>
		</div>
	);
}

export default Navigation;
