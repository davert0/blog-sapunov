import { createSlice } from '@reduxjs/toolkit';
import * as thunks from './thunks';

const initialState = {
	isLoading: false,
	token: null,
	user: null,
	error: null
};

export const sessionSlice = createSlice({
	name: 'sessionSlice',
	initialState: initialState,
	reducers: {
		setIsLoading: (state, action) => ({
			...state,
			isLoading: action.payload,
		}),
		setUser: (state, action) => ({
			...state,
			user: action.payload,
		}),
		setToken: (state, action) => ({
			...state,
			token: action.payload,
		}),
		reset: () => initialState,
	},
});

export const actions = sessionSlice.actions;
export const sessionReducer = sessionSlice.reducer;
export { thunks };
