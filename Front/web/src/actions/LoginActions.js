import axios from 'axios'
import { API_END_POINT } from './api-end-point'

export function actionLogin(form) {

    return function (dispatch) {
        axios({
            method: 'POST',
            url: `${API_END_POINT}/login`,
            data: form
        }).then((response) => {
            if (response.data) {
                dispatch({type: "LOGIN", payload: {'user': form.username, 'token': 'none'}})
            } else {
                dispatch({type: "LOGIN", payload: null})
            }

        }).catch(function (error) {
            if (error) {
                dispatch({type: "LOGIN", payload: error.response})
            } else
                dispatch({ type: "LOGIN", payload: null })
        })
    }
}

