export default function LoginReducer(state = null, action) {

    switch (action.type) {
        case 'LOGIN':
            if (action.payload) {
                localStorage.setItem('token', `Bearer ${action.payload.token}`);
                localStorage.setItem('user', `${action.payload.user}`);
            }
            return action.payload;
        default:
            return state
    }
}

export const Login = (state) => state.Login;
