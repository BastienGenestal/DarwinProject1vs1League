let temp

switch (window.location.port) {
    case 80:
        temp = "http://45.76.34.20:8080"
    default:
        temp = "http://127.0.0.1:8080"
}
console.log("Server location: ", temp)
export const API_END_POINT = temp
