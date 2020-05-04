let temp

switch (window.location.port) {
    case 3000:
        temp = "http://127.0.0.1:8080"
    default:
        temp = "http://45.76.34.20:8080"
}
export const API_END_POINT = temp
