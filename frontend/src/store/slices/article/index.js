import { createSlice } from '@reduxjs/toolkit';


const initialState = {
	articles: [],
};

export const articleSlice = createSlice({
	name: 'articleSlice',
	initialState: initialState,
	reducers: {
		setArticles: (state, action) => ({
			...state,
			data: action.payload,
		}),
		reset: () => initialState,
	},
});

export const actions = articleSlice.actions;
export const articleReducer = articleSlice.reducer;
// export { thunks };
