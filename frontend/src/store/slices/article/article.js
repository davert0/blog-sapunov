import { createSlice } from '@reduxjs/toolkit';
import * as thunks from "./thunks"

const initialState = {
	articles: [],
};

export const articleSlice = createSlice({
	name: 'articleSlice',
	initialState: initialState,
	reducers: {
		setArticles: (state, action) => ({
			...state,
			articles: action.payload,
		}),
		reset: () => initialState,
	},
});

export const actions = articleSlice.actions;
export const articleReducer = articleSlice.reducer;
export { thunks };
