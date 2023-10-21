const LOAD_FIGHTER = 'fighters/LOAD_FIGHTER'

//###################### ACTION CREATORS #############

const loadOne = (fighter) => {
    return {
        'type': LOAD_FIGHTER,
        fighter
    }
}

//######################## Thunks ############################

export const getOneFighter = (id) => async dispatch => {
    const response = await fetch(`/api/fighter/fighter/${id}`)

    if (response.ok) {
        const fighter = await response.json()
        dispatch(loadOne(fighter))
    }
}

let initialState = {}
//######################## Reducer ##########################

const fightersReducer = (state = initialState, action) => {
    let newState = {}
    switch (action.type) {
        case LOAD_FIGHTER: {
            newState = { ...action.fighter }
            return newState
        }
        default:
            return state
    }
}

export default fightersReducer
