import { combineReducers } from 'redux'
import LoginReducer from './LoginReducer'

const rootReducer = combineReducers({
    Login: LoginReducer
})

export default rootReducer;