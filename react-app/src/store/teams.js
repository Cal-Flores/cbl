const LOAD_TEAMS = 'teams/LOAD_TEAMS'

//################## Action Creators ######################

const loadAll = (teams) => {
    return {
        'type': LOAD_TEAMS,
        teams
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


let initialState = {}
//######################## Reducer ##########################

const teamsReducer = (state = initialState, action) => {
    let newState = {}
    switch (action.type) {
        case LOAD_TEAMS: {
            newState = { ...action.teams }
            return newState
        }
        default:
            return state
    }
}

export default teamsReducer
