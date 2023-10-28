const LOAD_TEAMS = 'teams/LOAD_TEAMS'
const LOAD_TEAM = 'teams/LOAD_TEAM'
const SORT_TEAMS = 'teams/SORT_TEAMS'
const TEAM_DUALS = 'teams/TEAM_DUALS'

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
        default:
            return state
    }
}

export default teamsReducer
