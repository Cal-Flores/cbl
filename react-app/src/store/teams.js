const LOAD_TEAMS = 'teams/LOAD_TEAMS'
const LOAD_TEAM = 'teams/LOAD_TEAM'
const SORT_TEAMS = 'teams/SORT_TEAMS'
const TEAM_DUALS = 'teams/TEAM_DUALS'
const LOAD_SCHEDULE = 'teams/LOAD_SCHEDULE'
const ALL_DUALS = 'teams/ALL_DUALS'

//################## Action Creators ######################

const loadAll = (teams) => {
    return {
        'type': LOAD_TEAMS,
        teams
    }
}

const loadOne = (team) => {
    return {
        'type': LOAD_TEAM,
        team
    }
}

const loadDuals = (duals) => {
    return {
        'type': TEAM_DUALS,
        duals
    }
}
const loadSchedule = (duals) => {
    return {
        'type': LOAD_SCHEDULE,
        duals
    }
}
const allDuals = (duals) => {
    return {
        'type': ALL_DUALS,
        duals
    }
}

//######################## Thunks ############################

export const getAllTeams = () => async dispatch => {
    const response = await fetch(`/api/team/`)

    if (response.ok) {
        const teams = await response.json()
        dispatch(loadAll(teams))
    }
}

export const getOneTeam = (id) => async dispatch => {
    const response = await fetch(`/api/team/${id}`)

    if (response.ok) {
        const team = await response.json()
        dispatch(loadOne(team))
    }
}

export const teamStandings = (filteredTeams) => async dispatch => {

}

export const teamDuals = (id) => async dispatch => {
    const response = await fetch(`/api/team/duals/<int:id>`)

    if (response.ok) {
        const duals = await response.json()
        dispatch(loadDuals(duals))
    }
}

export const getSchedule = (week) => async dispatch => {
    const response = await fetch(`/api/team/schedule/${week}`)

    if (response.ok) {
        const duals = await response.json()
        dispatch(loadSchedule(duals))
    }
}

export const getAllSchedule = () => async dispatch => {
    const response = await fetch(`/api/team/schedule`)

    if (response.ok) {
        const duals = await response.json()
        dispatch(allDuals(duals))
    }
}

let initialState = {}
//######################## Reducer ##########################

const teamsReducer = (state = initialState, action) => {
    let newState = {}
    switch (action.type) {
        case LOAD_TEAMS: {
            newState = { ...action.teams }
            return newState
        }
        case LOAD_TEAM: {
            newState = { ...action.team }
            return newState
        }
        case TEAM_DUALS: {
            newState = { ...action.duals };
            return newState
        }
        case LOAD_SCHEDULE: {
            return {
                ...state, // Maintain the current state
                ...action.duals, // Merge in the newly loaded schedule data
            };
        }

        case ALL_DUALS: {
            newState = { ...action.duals };
            return newState
        }
        default:
            return state
    }
}

export default teamsReducer
