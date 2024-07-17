const API_BASE_URL = 'http://localhost:8000'

export const API_ENDPOINTS = {
    BASE: API_BASE_URL,
    // usersテーブル関連
    SIGNUP: `${API_BASE_URL}/users/signup/`,
    LOGIN: `${API_BASE_URL}/users/login/`,
    LOGOUT: `${API_BASE_URL}/users/logout/`,
    UPDATE_USER: `${API_BASE_URL}/users/update/`,
    DELETE_USER: `${API_BASE_URL}/users/delete/`,
    // diaryテーブル関連
    ADD_DIARY_DIARY: `${API_BASE_URL}/diaries/add/`,
    UPDATE_DIARY: `${API_BASE_URL}/users/update/`,
    DELETE_DIARY: `${API_BASE_URL}/users/delete/`,
}