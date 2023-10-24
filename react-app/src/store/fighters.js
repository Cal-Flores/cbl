const LOAD_FIGHTER = 'fighters/LOAD_FIGHTER'
const LOAD_ALL_FIGHTERS = 'fighters/LOAD_ALL_FIGHTERS'

//###################### ACTION CREATORS #############

const loadOne = (fighter) => {
    return {
        'type': LOAD_FIGHTER,
        fighter
    }
}

const loadAll = (fighters) => {
    return {
        'type': LOAD_ALL_FIGHTERS,
        fighters
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

export const getAllFighters = () => async dispatch => {
    const response = await fetch('/api/fighter/')

    if (response.ok) {
        const fighters = await response.json()
        console.log('elmo', fighters)
        dispatch(loadAll(fighters))
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
        case LOAD_ALL_FIGHTERS: {
            newState = { ...action.fighters }
            return newState
        }
        default:
            return state
    }
}

export default fightersReducer
