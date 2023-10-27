const LOAD_FIGHTER = 'fighters/LOAD_FIGHTER'
const LOAD_ALL_FIGHTERS = 'fighters/LOAD_ALL_FIGHTERS'
const LOAD_FEW_FIGHTERS = 'fighters/LOAD_FEW_FIGHTERS'
const SEARCH_FIGHTERS = 'fighters/SEARCH_FIGHTERS'
const DELETE_FIGHTER = 'fighters/DELETE_FIGHTER'
const DRAFT_FIGHTER = 'fighters/DRAFT_FIGHTER'
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

const loadFew = (fighters) => {
    return {
        'type': LOAD_FEW_FIGHTERS,
        fighters
    }
}



const fighterSearch = (fighters) => {
    return {
        'type': SEARCH_FIGHTERS,
        fighters
    }
}

const draftFighter = (draft) => {
    return {
        'type': DRAFT_FIGHTER,
        draft
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

export const cutOneFighter = (id) => async dispatch => {
    console.log('cut thunk activated')
    const response = await fetch(`/api/fighter/cut/${id}`)
    if (response.ok) {
        console.log('cut response was gucci')
        return;
    }
    console.log('cut wasnt cash money')
    return
}

export const addFighterTeam = (draft, setError) => async dispatch => {
    const response = await fetch(`/api/fighter/draft`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(draft)
    })

    if (response.status === 200) {
        const draft = await response.json()
        dispatch(draftFighter(draft))
        return draft
    } else if (response.status === 400) {
        const errorResponse = await response.json();
        // Handle the error and display it to the user
        setError(errorResponse.error); // Set the error message
    } else {
        // Handle other errors
        alert('An error occurred');
    }
}

export const getAllFighters = () => async dispatch => {
    const response = await fetch('/api/fighter/')

    if (response.ok) {
        const fighters = await response.json()
        dispatch(loadAll(fighters))
    }
}

export const getFightersByWeight = (weight) => async dispatch => {
    const response = await fetch(`/api/fighter/${weight}`)

    if (response.ok) {
        const fighters = await response.json()
        dispatch(loadFew(fighters))
    }
}

export const createSearch = (obj) => async dispatch => {
    const response = await fetch(`/api/fighter/search`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(obj)
    })
    if (response.ok) {
        const fighters = await response.json()
        dispatch(fighterSearch(fighters))
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
        case LOAD_FEW_FIGHTERS: {
            newState = { ...action.fighters }
            return newState
        }
        case SEARCH_FIGHTERS: {
            newState = { ...action.fighters }
            return newState
        }
        default:
            return state
    }
}

export default fightersReducer
