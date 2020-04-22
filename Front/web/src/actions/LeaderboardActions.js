import axios from 'axios'
import { API_END_POINT } from './api-end-point'

export function actionGetLeaderboard() {

    return function (dispatch) {
        dispatch({type: "LEADERBOARD_IS_LOADING", payload: true})

        axios({
            method: 'GET',
            url: `${API_END_POINT}/leaderboard`
        }).then((response) => {
            if (response.data) {
                dispatch({type: "LEADERBOARD", payload: response.data})
            } else {
                dispatch({type: "LEADERBOARD", payload: null})
            }
            dispatch({type: "LEADERBOARD_IS_LOADING", payload: false})
        }).catch(function (error) {
            if (error) {
                dispatch({type: "LEADERBOARD", payload: error.response})
            } else
                dispatch({ type: "LEADERBOARD", payload: null })
            dispatch({type: "LEADERBOARD_IS_LOADING", payload: false})
        })
    }
}

